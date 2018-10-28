import time
import rtmidi
from rtmidi.midiconstants import *

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print(available_ports)

if available_ports:
    midiout.open_port(2)
else:
    midiout.open_virtual_port("My virtual output")

print(NOTE_ON)
note_on = [NOTE_ON, 50, 15] # channel 1, middle C, velocity 112
note_off = [0x80, 60, 0]
midiout.send_message(note_on)
time.sleep(.5)
midiout.send_message(note_off)

del midiout
