# pyboard-robotics
Robotic control helpers  for the pyboard.  Latest code at https://github.com/donuk/pyboard-robotics

## Controlling the PyBoard
## Installing programs to the pyboard

If you attach the pyboard to the computer via usb it should show up as an external drive.

Copy folder lib on to the drive.

Copy one of the files from the projects folder onto the drive and call it main.py.

Now restart the board to start running the program.  Unplugging and plugging it back in will do this or presing the reset button if you can reach it.

### Programming the board interactivley

The board can also be used interactively.  To do this connect it via usb to a computer running linux and in a terminal run the command:

    screen /dev/ttyACM0

If you have problems with this command, please see the troubleshooting section below.

Once connected the board may still be running the installed program.  If you hold ``<control>`` and press ``c``this should put the board in interactive mode which should look like this:

```
MicroPython v1.9.4-85-gdf9b7e8f on 2018-05-24; PYBv1.1 with STM32F405RG
Type "help()" for more information.
>>> 
```
You can then type in python commands directly.

```
>>> from lib.servo import *
>>> servo1.forward()
```

To exit interactive mode you can use ``<control>`` and ``d``.  The board will reboot and begin running the main.py file again.

## Programming APIs
### Servo Shield

The servo shield allows the connectin of up to 4 servos.  By default servos are controlled by giving them an angle to move to.  They may also be modified to run as continuous motors, in which case they can be controlled using forward / backward / stop.

To use the servo shield the code must be imported:

    from lib.servo import *

You should now have access to the variables ``servo1``, ``servo2``, ``servo3``, and ``servo4``

 Continous servos can be controlled with the methods forward, backward and stop.

e.g.

    servo1.forward()
    servo1.backward()
    servo1.stop()

The unmodified servos can also be controlled by giving them an angle in degrees

    servo3.degrees(40)

## Technical stuff
### Troubleshooting interactive use

You will probably need to install screen before the first use, on debian/ubuntu machines this can be done using:

    sudo apt install screen

The device name may also be different on some systems, you may be able to find it by running:

    ls /dev

And looking for devices with names beginning "ttyACM"

Different Linux versions have different permissions for the ttyACM devices.  You may need to make sure your user has read and write permissions on the device.  This can be done using chmod:

    sudo chmod a+rw /dev/ttyACM0

Or by adding your user to the group which owns the device, this is `dialout` on my debian system, you can check this by running `ls -l /dev/ttyACM0`.  On my debian system you can add yourself to the group by running `sudo usermod -aG dialout don` (you'd need to replace don with your username) and then logging out and back in again.

### Using pip to install libraries

You can't install packages directly as the board cannot access the internet so you need to install them on an internet connected computer then copy them across.

On Linux you can use micropython:

```
$ sudo apt install micropython
$ micropython -m upip install -p lib/pip micropython-contextlib
```

This would install the library `micropython-contextlib` to the directory `lib/pip`.  You would now need to copy that directory onto the board to a location where python can find it (`lib/pip` should work, this is configured in `lib/pip_path.py`).
