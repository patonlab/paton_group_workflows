1. Run Gaussian job to create *.wfn file
   (this requires 'output=wfn' in the route line, and the desired name at the end of the input file)

2. Run NCI job to create the 2 *.cube files. 
   ## for SLURM: sbatch nci_slurm.sh paracetamol.nci
   ## On linux machines without SlURM: nohup nciplot paracetamol.nci > paracetamol.out &
 
3. create an *.xyz or *.pdb file of the molecule. Open this, along with the two cube files (either drag and drop or use the load command from within Pymol) in Pymol. 
   The easiest way is using open babel: obabel -ig09 paracetamol.log -oxyz > paracetamol.xyz

4. In Pymol, you will require the methods contained in patongrp_pymol_style.py. Either run this, or add it to your .pymolrc

5. To show the NCI surface, type nci paracetamol -3,3
   The numbers indicate the range of the colors used, so experiment with different values!

6. Export the image as a *png file, remembering to ray-trace first:
ray; png fancy_image.png, dpi=600

