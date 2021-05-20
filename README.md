Welcome to RSPGROUP on SUMMIT: congratulations - your path is set-up correctly!

The following scripts are available: 
- qstat_summit (monitor disk usage, queue status and jobs)
- qsub_summit (submit G16 and Orca jobs)
- ncisub_summit (submit NCIPlot jobs)
- qcosmo_summut (submit COSMO-RS jobs)
- AutoPrep (create input files from existing output files)
- RotMol (rotates molecules, creating new input files)

The following python modules are available (python -m module):
- goodvibes (thermochemical anaylsis) | https://github.com/bobbypaton/GoodVibes
- pyqrc (fast reaction coordinate) | https://github.com/bobbypaton/pyQRC
- pydftd3 (D3-dispersion corrections) | https://github.com/bobbypaton/pyDFTD3
- kinisot (kinetic isotope effects) | https://github.com/bobbypaton/Kinisot
- DBSTEP (steric parameters) | https://github.com/bobbypaton/DBSTEP
- ase (atomic simulation environment)

To activate a python environment where rdkit, openbabel etc are present:
- source activate DL_CPU (this may require edits to your .condarc file - ask RSP if this is an issue)

The following software is available:
- QChem 5.2 /projects/rpaton@colostate.edu/qchem
- Gaussian 16 rev C.01 - /projects/rpaton@colostate.edu/g16/g16
- Orca v4.2.1 - /projects/rpaton@colostate.edu/orca_4_2_1_linux_x86-64_openmpi216
- NBO v7 - /projects/rpaton@colostate.edu/nbo6/bin/gaunbo7
- NCIPlot v4 - /projects/rpaton@colostate.edu/nciplot/nciplot
- Turbomole v7.3 - /projects/rpaton@colostate.edu/turbomole/TURBOMOLE
- COSMOtherm v19 - /projects/rpaton@colostate.edu/turbomole/COSMOlogic/COSMOthermX19/COSMOtherm/BIN-LINUX/cosmotherm
- TeraChem 1.93P - /projects/rpaton@colostate.edu/TeraChem/bin/terachem 
- XTB v6.4.0 - /projects/rpaton@colostate.edu/xtb_6.4.0/bin/xtb
- CREST v2.11 - /projects/rpaton@colostate.edu/xtb_6.4.0/crest
- MECPRO - /projects/rpaton@colostate.edu/mecpro
- Jprogdyn - /projects/rpaton@colostate.edu/JPROGDYN 
- AMBER18 - /projects/rpaton@colostate.edu/amber18

- To see example usage: create a directory in your $PROJECTS folder and cd there, then type:
- RUNTEST all 
- This will submit several jobs. When finished, check they ran properly:
- CHECKTEST all
    
          ___       ___                 ___          ___                       ___                  
         /\  \     /\  \               /\  \        /\  \                     /\  \        _____    
        /::\  \   /::\  \       ___   /::\  \       \:\  \                   /::\  \      /::\  \   
       /:/\:\__\ /:/\:\  \     /\__\ /:/\:\  \       \:\  \                 /:/\:\  \    /:/\:\  \  
      /:/ /:/  //:/ /::\  \   /:/  //:/  \:\  \  _____\:\  \  ___     ___  /:/ /::\  \  /:/ /::\__\ 
     /:/_/:/  //:/_/:/\:\__\ /:/__//:/__/ \:\__\/::::::::\__\/\  \   /\__\/:/_/:/\:\__\/:/_/:/\:|__|
     \:\/:/  / \:\/:/  \/__//::\  \\:\  \ /:/  /\:\~~\~~\/__/\:\  \ /:/  /\:\/:/  \/__/\:\/:/ /:/  /
      \::/__/   \::/__/    /:/\:\  \\:\  /:/  /  \:\  \       \:\  /:/  /  \::/__/      \::/_/:/  / 
       \:\  \    \:\  \    \/__\:\  \\:\/:/  /    \:\  \       \:\/:/  /    \:\  \       \:\/:/  /  
        \:\__\    \:\__\        \:\__\\::/  /      \:\__\       \::/  /      \:\__\       \::/  /   
         \/__/     \/__/         \/__/ \/__/        \/__/        \/__/        \/__/        \/__/    


- REMINDER: NEW SSKY QUEUE: qsub_summit -p ssky-preemptable

