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
   ```python
   import triax320_control # this is not necessarily needed actually
   from triax320_control.instruments.spex750m import triax320 as triax320
   ```
3. Initialize Instance
   ```python
   beast = triax320()
   ```
4. Calibrate Motors. It is best to reset all motors at the beginning and zero the wavelength.
   ```python
   beast.motor_init() # this zeroes the slits and the grating
   beast.calibrate(0) # this sets the current wavelength to 0 without moving the motor
   ```
5. Now you are free to have fun with the Monochromator. Useful commands include set_wl(), rel_move() and slits. For a detailed documentation of all commands, see         https://wanglib.readthedocs.io/en/latest/instruments/spex750m.html

## Examples
```python
beast = triax320()
beast.motor_init()
beast.calibrate(0)

beast.slits = 100 # opens both entrance and exit slit to 100. I have yet to find out what unit that is and what the maximum is.
beast.set_wl(550) # set wavelength to a lovely green at 550nm. There should be green light now at the exit. If not, check if you have opened the manual shutter.
beast.rel_move(100) # move the wavelength relatively a 100nm. There should be red light now.
beast.wl # query current wavelength
beast.rel_move(-200) # move the wavelength to the lower end. There should be somewhat blue light now.
```
