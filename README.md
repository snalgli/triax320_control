# triax320_control

Hopefully soon a Python 3 compatible control software for the Triax320 Monochromator based on wanglib by T. Baldwin (https://github.com/baldwint/wanglib).
Work in progress

## Doku Triax320 Monochromator


using wanglib package. needs python 2, doesnt work on python3!
installing python 2 using a virtual environment, for example anaconda or pyenv

anaconda:
    conda create --name py2 python=2.7.18
    conda activate py2
    
    
check for used serial port:
    mac: ls /dev/tty.usb*
    linux: usually /dev/ttyUSB0 or /dev/ttyUSB1
    
important: stepsize has to be correct in spex750m.py line 100 (16.7 for triax320 without microstep option, 500 with option, 4000 for spex750m)