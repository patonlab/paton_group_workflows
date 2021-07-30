#!/bin/usr/env python3
"""
Generates the input files for tmol calculations either starting from coord files
or from xyz files. 
"""

# MARIJ is used as default. Use RIJK only 
# with double hybrids. def2 diffusion augmented basis sets use RI-K auxilary basis
# sets as RI-J auxilary basis sets with scftol 1d-16 threshold. RIcore 200 MB is 
# enough for (m)GGA functionals and often for hybrids too. RPA uses alot of 
# memory, so set MaxCore and RIcore to 1000. Use at least grid m4 to eliminate 
# noise in frequency calculations. The fine cavity works only with single-point 
# calculations.

import os
import argparse

from pytmolparse.classes import TurbomoleInput, BasisSet

def create_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('folders',help="""Folders with coordinate files 
                        to generate the inputs""",default='TPSS',nargs='*')
    parser.add_argument('-f','--functional',help="Functional",default='TPSS')
    parser.add_argument('-bs','--basis',help="Basis-set",default='def2-SVP')
    parser.add_argument('-bsf','--basisfile',help='Basis set file',default=None)
    parser.add_argument('-d','--dispersion',help="Dispersion",
                        default='off',choices=['off','on','bj','d4'])
    parser.add_argument('-c','--charge',help="Charge",
                        default=0,type=int)
    parser.add_argument('-u','--multiplicity',help="Multiplicity",
                        default=1,type=int)
    parser.add_argument('-s','--epsilon',help="Dielectric Constant",
                        default='gas')
    parser.add_argument('-g','--grid',help="Grid",default='m4',
                        choices=['1','2','3','4','5','6','7','m3','m4','m5'])
    parser.add_argument('-m','--maxcore',help="Maximum memory per core in MB",
                        default=200, type=int)
    parser.add_argument('-rm','--ricore',help="RIcore", type=int,
                        default=200)
    parser.add_argument('-ired','--iredundant',action='store_false',default=True,
                        help='Turn off redundant internal coordinates',
                        dest='disable_ired')
    parser.add_argument('-fine','--fine',help="Enable fine cavity for COSMO-RS",
                        default=False, action='store_true')
    parser.add_argument('--disable-input',dest='disable_input',default=False,
                        help="""Disables the creation of an 'input_command' file
                        with the command used to run this script """,
                        action='store_true') 
    return parser
def parse_arguments(parser):
    args = parser.parse_args()
    if args.fine: 
        args.fine = 'fine'
    return args

def main(): 
    parser = create_parser()
    args = parse_arguments(parser)
    cwd = os.getcwd()
    for folder in args.folders: 
        if args.basisfile is not None: 
            basisset = BasisSet.from_file(args.basisfile)
            basis = basisset.basis
            auxbasis = basisset.auxbasis
            ecp = basisset.ecp
        else:
            basis = args.basis
            auxbasis = None
            ecp = None
        input_generator = TurbomoleInput(folder,
                                        functional=args.functional,
                                        basis=basis,
                                        auxbasis=auxbasis,
                                        ecp=ecp,
                                        dispersion=args.dispersion,
                                        charge=args.charge,
                                        multiplicity=args.multiplicity,
                                        grid=args.grid,
                                        epsilon=args.epsilon,
                                        maxcore=args.maxcore,
                                        ricore=args.ricore,
                                        disable_ired=args.disable_ired,
                                        cavity=args.fine)
        input_generator.generate()
        if not args.disable_input:
            input_generator.write_input_command()

if __name__ == '__main__':
    main()