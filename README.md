# esp-micropython

Build and install a micropython environment on esp board.

## Install package

```
pip3 install git+https://github.com/maekos/esp-micropython
```

## Usage

### Upload

1. You must connect your esp board to serial port. By default **device** is /dev/ttyUSB0 and baudrate is 115200.
2. Put your esp in program mode.
3. Erase the flash

```
esp erase -d /dev/ttyUSB0
```

4. Execute the following command:

```
esp upload -d /dev/ttyUSB0 -f esp8266-512k-20191220-v1.12.bin
```

Once finished micropython version 1.12 is already installed in your esp.
Otherwise you can choose another version of micropython from [here](https://micropython.org/download/esp8266/).

### Micropython

For run micropython you must execute in normal mode (this command by default get a device as /dev/ttyUSB0 and baudrate 115200)

```
esp mycropython
```

You shall see something like this:

```
$ esp micropython
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

---

# Flashing/uploading mode
Some ESP development boards don’t go into flashing/uploading mode automatically when uploading a new code.

This means that when you try to upload a new sketch to your ESP32, this fails to connect to your board, and you get the following error message:

```
esptool.py v2.8
Serial port /dev/ttyUSB0
Connecting........_____....._____....._____....._____....._____....._____....._____

A fatal error occurred: Failed to connect to Espressif device: Timed out waiting for packet header
```

## Holding the BOOT/FLASH button
One of the ways to solve this is holding-down the “BOOT/FLASH” button in your ESP board while uploading a new sketch at the same time. 

Credits [https://randomnerdtutorials.com](https://randomnerdtutorials.com/solved-failed-to-connect-to-esp32-timed-out-waiting-for-packet-header/)
