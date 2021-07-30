#!/bin/usr/env python3
"""
Prints the Potential energy, Zero point energy, Enthalpy and Free energy
from turbomole calculations. 
"""

import os
import argparse
from pathlib import Path

from pytmolparse.classes import TurbomoleOutput

# ensure a proper import of pybel for openbabel v2 and v3 and disable the logger
try:
    import pybel
    pybel.ob.OBMessageHandler().SetOutputLevel(0)
except ImportError: 
    from openbabel import pybel
    pybel.ob.obErrorLog.SetOutputLevel(0)

def create_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folders',help='folders that contain the turbomole outputs',
                        nargs='+')
    parser.add_argument('-l','--listfile',help="""When enabled it will read the 
                        file provided and return the output of each folder listed 
                        in it in the same order and retaining the empty lines""",
                        action='store_true',default=False)
    parser.add_argument('-o','--outfile',help="""File to write the Data. If it
                        exists, the data will be appended, if not specified it will
                        print to the console""",default=None)
    parser.add_argument('-t','--temperature',help="""Temperature at which the 
                        thermochemistry values are desired in K""",
                        type=float,default=298.15) 
    parser.add_argument('-p','--pressure', help="""pressure at which the 
                        thermochemistry values are desired in MPa (for non-qh)""",
                        type=float,default=0.100)
    parser.add_argument('-s','--scaling-factor',dest='scaling_factor',help="""
                        scaling factor for thermochemistry calculations""",
                        default=1,type=float)
    parser.add_argument('-qh','--quasi-harmonic',dest='quasi_harmonic',help="""
                        Print Quasi-harmonic corrected thermochemistry values.
                        specify: """,action='store_true')
    parser.add_argument('-f','--frequency-cutoffs',dest='frequency_cutoffs',
                        nargs=2,default=(100,150), help="""Frequency thresholds
                        for qh thermochemistry.""",metavar=('LowFreq','HighFreq'))
    parser.add_argument('--freeh-exec',dest='freeh_exec',help="""Path 
                        to the freeh executable if it is not accesible by 
                        default""",default=None)
    parser.add_argument('--thermo-exec',dest='thermo_exec',help="""Path 
                        to the thermo executable (Grimme's script) if it is not 
                        accesible by default""",default=None)
    parser.add_argument('--show-SP',dest='show_SP',action='store_true',
                        default=False,help="""If enabled it will also display 
                        the potential energy of the SP""") 
    return parser
def write_2_file(File):
    """
    Creates a wrapper for appending text to a certain File. Assumes that each
    call is equivalent to writing a single line.
    """
    def Writer(txt):
        with open(File,'a') as OFile:
            OFile.write(txt)
            OFile.write('\n')
    return Writer


def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.listfile:
        with open(args.folders,'r') as F:
            folders = [line.strip() for line in F]
    else:
        folders = args.folders

    outfile = args.outfile
    if args.outfile is not None:
        outfile = os.path.abspath(args.outfile)
        WriteOutput = write_2_file(outfile)
    else:
        WriteOutput = print

    # Header to know which is each column
    LargestName = max([len(Path(folder).stem) for folder in folders])
    if args.show_SP: 
        msg_ini_1 = ' '*LargestName 
        msg_ini_1 += '           {: ^18}       ' + '           {: ^18}'
        msg_ini_2 = f'{{: ^{LargestName}}}' + '    {: ^14}'*4
        titles_2 = ('File','U','G','U','G')
    else:
        msg_ini_1 = ' '*LargestName + '    '
        msg_ini_1 += '       {: ^18}       ' + '    {: ^14}'
        msg_ini_2 = f'{{: ^{LargestName}}}' + '    {: ^14}'*3
        titles_2 = ('File','U','G','G')

    WriteOutput(msg_ini_1.format('opt','SP'))
    WriteOutput(msg_ini_2.format(*titles_2))

    # Format for filenames
    txt = filename_f =  f'{{: <{LargestName}}}'

    # Format for the numbers
    number_f = '{: 03.9f}'.format

    if args.show_SP:
        txt = filename_f + '    {: ^14}'*4  
    else: 
        txt = filename_f + '    {: ^14}'*3  

    # Actual parsing
    for folder in folders:
        if not folder: #In the case of an empty filename, write an empty line
            WriteOutput('')
            continue
        folder_p = Path(folder)
        if not folder_p.is_absolute(): 
            abs_folder_path = folder_p.absolute()
        else: 
            abs_folder_path = folder
        Name = folder_p.stem
        tmol_out = TurbomoleOutput(abs_folder_path,
                                   T=args.temperature,
                                   P=args.pressure,
                                   scale_factor=args.scaling_factor,
                                   qh_thermo=args.quasi_harmonic,
                                   fcutoffs=tuple(args.frequency_cutoffs))
        if args.freeh_exec is not None and not args.quasi_harmonic: 
            tmol_out.calc_thermo(os.path.abspath(args.freeh_exec))
        if args.thermo_exec is not None and args.quasi_harmonic: 
            tmol_out.calc_thermo(os.path.abspath(args.thermo_exec))
        items = [tmol_out.energy,tmol_out.zpe,tmol_out.enthalpy,tmol_out.gibbs]
        U,Z,H,G = items
        
        U_HB = None
        for subfolder in folder_p.iterdir(): 
            if subfolder.is_dir() and 'sp-energy' in subfolder.stem: 
                tmol_out_sp = TurbomoleOutput(subfolder.absolute())
                U_HB = tmol_out_sp.energy
        
        if G is not None and U_HB is not None:
            G_HB = number_f(U_HB + G - U)
        else:
            G_HB = ''

        if U is None: 
            U = ''
        else: 
            U = number_f(U)

        if G is None: 
            G = ''
        else: 
            G = number_f(G)

        if U_HB is None: 
            U_HB = ''
        else: 
            U_HB = number_f(U_HB)


        if args.show_SP: 
            WriteOutput(txt.format(Name,U,G,U_HB,G_HB))
        else:
            WriteOutput(txt.format(Name,U,G,G_HB))

if __name__ == '__main__': 
    main()
    