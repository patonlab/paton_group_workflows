import setuptools

__version__ = '0.0.0'

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'pytmolparse',
  version = __version__,
  packages = ['pytmolparse',],
  description = """ Basic scripts for parsing and generating turbomole inputs
                using python. Based on Santeri's bash scripts for turbomole """,
  author = 'Raúl Pérez-Soto',
  author_email = 'rperezsoto.research@gmail.com',
  long_description=long_description,
  long_description_content_type="text/x-rst",
  url = 'https://github.com/bobbypaton/rspgrp_summit',
  keywords = ['compchem', 'turbomole','parser'],
  classifiers = ['License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8',
                 'Programming Language :: Python :: 3.9',
                 ],
  install_requires=['setuptools','pathlib','numpy', 'pyssian'],
  extras_require={'plotting functions':'matplotlib'},
  python_requires='>=3.6',
  include_package_data=True,
  scripts = ['pytmolparse/tmol-thermo.py',
             'pytmolparse/tmol-thermo-sp.py',
             'pytmolparse/tmol-thermo-keywords.py',
             'pytmolparse/tmol-input.py',
             'pytmolparse/tmol-submit.py'],
  project_urls={'Bug Reports': 'https://github.com/bobbypaton/rspgrp_summit/issues',
                'Source': 'https://github.com/bobbypaton/rspgrp_summit/pytmolparse',
               },
)
