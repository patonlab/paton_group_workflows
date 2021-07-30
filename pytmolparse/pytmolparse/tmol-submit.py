#!/bin/usr/env python3
"""
Generate a submit script appropiate for the type of 
turbomole calculation 
"""
import argparse
import os
from pathlib import Path
import subprocess
import shlex

# ensure a proper import of pybel for openbabel v2 and v3
try:
    import pybel
except ImportError: 
    from openbabel import pybel

def create_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('jobtype',choices=['sp','opt','freq','ex','wlf','rpa'],
                        default='sp',
                        help=""" 'opt' does a geometry optimisation, 
                                 'num' and ao do frequency calculations, 
                                 'sp' calculates single-point energy, 
                                 'ex' calculates excitation energies, 
                                 'wlf' finds transition states, 
                                 'rpa' does a Random Phase Approximation calculation.""")
    parser.add_argument('-p','--processors',help="number of processors",
                        default=1,type=int)
    return parser

def write_hostfile(processors):
    with open('hostfile','w') as F: 
        F.write('\n'.join(['localhost',]*processors))

def modify_control_for_wlf():
    with open('control','r') as F: 
        txt = F.read()
    header = ['$woelfling',
              'ninter                     14',
              'ncoord                      2',
              'align                       0',
              'tangtyp                     0',
              'nactive                    14',
              'nactive1                     7',
              'nactive2                     8',
              'maxit                   200',
              'dlst   3.00000000000000',
              'thr  1.000000000000000E-004',
              'hessinit model',
              'tangents fixed',
              'method q']
    txt = '\n'.join(header) + '\n' + txt
    with open('control','w') as F: 
        F.write(txt)
def modify_files_for_ts():
    i = 0
    while True: 
        folder = Path('opt{i:03d}')
        if not folder.exists():
            break
        i += 1 
    p = subprocess.Popen(shlex.split(f'cpc {str(folder)}'),
                         sdtout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    os.chdir(str(folder))
    with open('control','r') as F: 
        txt = F.read() 
    txt = '$statpt\nitrvec 1\n' + txt
    with open('control','w') as F:
        F.write(txt)
    #with open('coord','r') as F:
    # Do stuff
    os.chdir('..')
    return folder
def create_coords_for_wlf():
    substrate = next(pybel.readfile('xyz','substrate.xyz'))
    product = next(pybel.readfile('xyz','product.xyz'))
    with open('coord','w') as F: 
        F.write(substrate.write('tmol'))
        F.write(product.write('tmol'))

def handle_num(submit_contents,processors):
    write_hostfile(processors)

    submit_contents.append('export HOSTS_FILE=$SDIR/hostfile')
    nohup_cmd = ' '.join(['nohup','NumForce',
                          '-cosmo','-ri',
                          '-central','-mfile',
                          '$HOSTS_FILE','>',
                          'NumForce.out','&'])
    submit_contents.append(nohup_cmd)
def handle_opt(submit_contents,*dummy): 
    submit_contents.append('nohup jobex -ri -c 300 > jobex.out &')
def handle_ts(submit_contents,*dummy):
    nohup_cmd = 'nohup jobex -ri -c 300 -trans -statpt > jobex.out &'
    submit_contents.append(nohup_cmd)
    new_folder = modify_files_for_ts()
def handle_sp(submit_contents,*dummy):
    submit_contents.append('nohup ridft > ridft.out &')
def handle_ex(submit_contents,*dummy):
    submit_contents.append('nohup escf > escf.out &')
def handle_ao(submit_contents,*dummy):
    submit_contents.append('nohup aoforce > aoforce.out &')
def handle_drc(submit_contents,*dummy):
    submit_contents.append('nohup DRC -c 100 -ri > DRC.out &')
def handle_wlf(submit_contents,*dummy):
    submit_contents.append('nohup woelfling-job > woelfling-job.out &')
    modify_control_for_wlf()

HANDLERS = {'num':handle_num,
            'opt':handle_opt,
            'ts':handle_ts,
            'sp':handle_sp,
            'ex':handle_ex,
            'ao':handle_ao,
            'drc':handle_drc,
            'wlf':handle_wlf}

def main():
    parser = create_parser()
    args = parser.parse_args()
    print(f'JobType : {args.jobtype}')
    print(f'Number of procs : {args.processors}')
    submit_filename = f'tmjob_{args.jobtype}'
    
    if args.jobtype in ['opt','ts','drc','mikko']:
        parallelization = f'export PARA_ARCH=MPI'
    elif args.jobtype in ['num','ao','sp','ex','woelf']: 
        parallelization = f'export PARA_ARCH=SMP'
    else:
        parallelization = ''


    turbodir = os.environ.get('TURBODIR',None)
    if turbodir is None: 
        print("""TURBODIR environment variable not found, Fill it manually in 
              the generated script""" )
        turbodir = ''
    
    submit_contents = ['#!/bin/bash -l',
                       'turbo=;',
                       '',
                       f'export TURBODIR={turbodir}',
                       'export PATH=$TURBODIR/scripts:$PATH',
                       'export PATH="${TURBODIR}/bin/`sysname`:${PATH}"',# Can this be removed ? 
                       'unset LANG',
                       'unset LC_CTYPE',
                       'SDIR=$PWD',
                       '',
                       parallelization,
                       r'source $TURBODIR/Config_turbo_env',
                       '',
                       f'numproc={args.processors}',
                       'export PARNODES=$numproc',
                       '']
    handler = HANDLERS[args.jobtype]
    handler(submit_contents,args.processors)
    submit_contents.append(f'touch {args.jobtype}-job_\$!')
    submit_contents.append('')

    with open(submit_filename,'w') as F: 
        F.write('\n'.join(submit_contents))


