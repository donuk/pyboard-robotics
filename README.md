# pyboard-robotics
Robotic control helpers  for the pyboard

## Controlling the PyBoard
## Installing programs to the pyboard

If you attach the pyboard to the computer via usb it should show up as an external drive.

Copy folder lib on to the drive.

Copy one of the files from the projects folder onto the drive and call it main.py.

Now if you restart the board (unplugging and plugging it back in will do this or presing the reset button if you can reach it.

### Programming the board interactivley

The board can also be used interactively.  To do this connect it via usb to a computer running linux and in a terminal run the command:

    screen /dev/ttyACM0

Once connected the board will still be running the installed program.  If you hold ``<control>`` and press ``c``this should put the board in  interactive mode and you can type in python commands directly.

    >>> from lib.servo import *
    >>> servo1.forward()

To exit interactive mode you can use ``<control>`` and ``d``.  The board will reboot and begin running the main.py file again.

### Troubleshooting

You will probably need to install screen before the first use, on debian/ubuntu machines this can be done using:

    sudo apt install screen

The device name may also be different on some systems, you may be able to find it by running:

    ls /dev

And looking for devices with names beginning "ttyACM"

## Programming APIs
### Servo Shield

The servo shield allows the connectin of up to 4 servos.  By default servos are controlled by giving them an angle to move to.  They may also be modified to run as continuous motors, in which case they can be controlled using forward / backward / stop.

To use the servo shield the code must be imported:

    from lib.servo import *

You should now have access to the variables ``servo1``, ``ervo2``, ``servo3``, and ``servo4``

 Continous servos can be controlled with the methods forward, backward and stop.

e.g.

    servo1.forward()
    servo1.backward()
    servo1.stop()

The unmodified servos can also be controlled by giving them an angle in degrees

    servo3.angle(40)

