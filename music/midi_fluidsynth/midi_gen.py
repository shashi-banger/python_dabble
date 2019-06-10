from midiutil import MIDIFile
#degrees = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number

# http://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
degrees = [62, 64, 66, 67, 69, 71, 73, 74] # MIDI note number
track = 0
channel = 0
time = 0 # In beats
duration = 1 # In beats
tempo = 100 # In BPM
volume = 100 # 0-127, as per the MIDI standard
MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
# automatically created)

# Program number set using https://www.midi.org/specifications/item/gm-level-1-sound-set
MyMIDI.addProgramChange(track, channel, time, 21)
MyMIDI.addTempo(track,time, tempo)
for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1
with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
