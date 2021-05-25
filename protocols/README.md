This directory contains shared protocols 

** Visualizing FMOs in PyMol **

1. Load file.xyz to pymol.
2. Load file_homo.cube to pymol (which has been created using cubegen)
3. Command: run pymol_style.py
4. Command: BallnStick all
5. Command: Add_homo file_homo

Similar options can be done for visualizing lumo (Add_lumo) and spin (Add_spin). All that has to be done is change the cube files to the lumo or spin file.
