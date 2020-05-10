# esp201-micropython

Build and install a micropython environment on esp-201.

## Install package

```
pip3 install git+https://github.com/maekos/esp201-micropython
```

## Usage

### Upload

1. You must connect your device esp201 to serial port. By default **device** is /dev/ttyUSB0 and baudrate is 115200.
2. Put your esp201 in program mode.
3. Execute the following command:

```
esp201 upload -d /dev/ttyUSB0
```

Once finished micropython version 1.12 is already installed in your esp201.

### Micropython

For run micropython you must execute in normal mode (this command by default get a device as /dev/ttyUSB0 and baudrate 115200)

```
esp201 mycropython
```

You shall see something like this:

```
$ esp201 micropython
picocom v2.2

port is        : /dev/ttyUSB0
flowcontrol    : none
baudrate is    : 9600
parity is      : none
databits are   : 8
stopbits are   : 1
escape is      : C-a
local echo is  : no
noinit is      : no
noreset is     : no
nolock is      : no
send_cmd is    : sz -vv
receive_cmd is : rz -vv -E
imap is        : 
omap is        : 
emap is        : crcrlf,delbs,

Type [C-a] [C-h] to see available commands

```

Press enter, and that's all.
