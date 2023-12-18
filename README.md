# triax320_control

Hopefully soon a Python 3 compatible control software for the Triax320 Monochromator based on wanglib by T. Baldwin (https://github.com/baldwint/wanglib).
Work in progress

Everything related to controlling the Triax320 is now functional under Python 3. What will happen to the rest is unclear at this point, but there is no intention to work on it for the moment.

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

## Quick Start Guide:
1. Prerequisites
   - Python environment with Python 3. Numpy and PySerial are needed packages that typically have to be installed manually.
2. When in a py3 environment, first import the package. At the moment, the triax320 class should be imported directly, so it is easier to use.
   '''python
   import triax320_control
   from triax320_control.instruments.spex750m import triax320 as triax320
   '''
4. Initialize Instance
   beast = triax320()
5. Calibrate Motors. It is best to reset all motors at the beginning and zero the wavelength.
   beast.motor_init() #this zeroes the slits and the grating
   beast.calibrate(0) # this sets the current wavelength to 0 without moving the motor
6. Now you are free to have fun with the Monochromator. Useful commands include set_wl(), rel_move() and slits. For a detailed documentation of all commands, see         https://wanglib.readthedocs.io/en/latest/instruments/spex750m.html
