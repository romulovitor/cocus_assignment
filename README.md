#Overview

This repository contains the scripts corresponding to the test proposed by Cocus.

###Prerequisites

    Python >= 3.7.1
    Virtualenv >= 20.0.35

###Deploy
    
    1 - Clone this repository ( '$ git clone https://github.com/romulovitor/cocus_assignment.git ' )
    2 - Get in the project ( '$ cd cocus_assignment ')
    3 - Create venv using Makefile ('$ make venv ')
    4 - Activate the virtual dependencies ('$ source venv/bin/activate ')    
    5 - Run to create the environment of development ('$ make install ')
    6 - Run script ('$ python <scritp_name> ')
    7 - Run test ('$ pytest tests ') # Incomplete
    8 - Run coverage ('$ coverage run -m pytest ')
