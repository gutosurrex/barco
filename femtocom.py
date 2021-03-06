import os
import serial
import sys
import pprint
import cmd
import time
# import urwid

def get_serial_port():
    return "/dev/" + os.popen("dmesg | egrep ttyACM | rev | cut -c -7 | rev | head -n 1").read().strip()

ser = serial.Serial(sys.argv[1], 9600, timeout=1)

pp = pprint.PrettyPrinter(indent=4)

bytesToRead = ser.inWaiting()
try:
    output = ser.read(bytesToRead)
except ValueError:
    print 'Nothing to read at start...'

def question():
    return urwid.Pile([urwid.Edit(('I say', u"Enter command:\n"))])

def answer(name):
    ser.write(name + '\n')
    time.sleep(.8)
    bytesToRead = ser.inWaiting()
    try:
        output = ser.read(bytesToRead)
    except ValueError:
        print 'Did not manage to read output'
        #continue
    return urwid.Text(('I say', output))



while True:
    command = raw_input('>')
    #print 'Received the following command (type, commmand)'
    #print type(command)
    #pp.pprint(command)
    if command == 'exit':
        break
    ser.write(command + '\n')
    time.sleep(.8)
    bytesToRead = ser.inWaiting()
    print(bytesToRead)
    try:
        output = ser.read(bytesToRead)
        #output = ser.readline()
    except ValueError:
        print 'Did not manage to read output'
        continue

    print output

ser.close()





