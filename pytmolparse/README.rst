===========
pytmolparse
===========

------------------------------------------
A python interface for turbomole i/o files
------------------------------------------

This project contains an object oriented library with some basic classes to 
represent turbomole input and output files and to ensure proper format of 
turbomole files it interacts with some basic tools bundled with turbomole such 
as define or cosmoprep. It includes some basic scripts for generating input 
files, submit scripts and parsing the thermochemistry of outputs (interacting 
with freeh or Grimme's "thermo" script for quasi harmonic values).

Getting Started
---------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisites
.............

- python >= 3.6
- python library: setuptools
- library: openbabel 2.4 or openbabel >= 3.1
- python library: pybel
- Accesible environment variables for turbomole's "define", "freeh", "thermo" 

Installing pytmolparse and its scripts
......................................

Get the folder with the source code at a location of your preference 

.. code:: shell-session

   $ python -m pip install your/preference/location/pytmolparse/

*Installing with the -e option before pyssian will make that
all the changes in the source file will be effective without havin to reinstall*

Developed with
--------------

- python 3.7
- Ubuntu 16.04 LTS, 18.04 LTS and 20.04 LTS

Authors
-------

* **Raúl Pérez-Soto** - [rperezsoto](https://github.com/rperezsoto)
* **Santeri Aikonen** - [aikonens](https://github.com/aikonens)
