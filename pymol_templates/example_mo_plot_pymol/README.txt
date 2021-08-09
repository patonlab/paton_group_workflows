1. Run Gaussian job to create *.chk file

2. Run Formchk to convert the *.chk file to a formatted checkpoint file
   formchk paracetamol.chk

3. Run Cubgen to create the cube file of the spin density
   cubegen 0 MO=HOMO paracetamol.fchk paracetamol_HOMO.cube 80 h   
 
3. create an *.xyz or *.pdb file of the molecule. Open this, along with the cube file (drag and drop or use the load command) in Pymol. 
   The easiest way is using open babel: obabel -ig09 paracetamol.log -oxyz > paracetamol.xyz

4. In Pymol, you will require the methods contained in patongrp_pymol_style.py. Either run this, or add it to your .pymolrc

5. To show the molecular orbital, type mo_plot paracetamol_HOMO, 0.002
   The number indicates the isovalue used, so experiment with different values!

6. Export the image as a *png file, remembering to ray-trace first:
ray; png fancy_image.png, dpi=600

