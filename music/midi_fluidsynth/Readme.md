
## Installation
- sudo apt-get install fluidsynth
- pip install MIDIUtil

Following commands to generate midi, synthesize wav from it and play wav

1. Generate midi
python midi_gen.py
The above command will generate major-scale.mid file

2. fluidsynth -ni /usr/share/sounds/sf2/FluidR3_GM.sf2 major-scale.mid -F output.wav -g 1.5 -r 48000
This command will generate wav from output of 1

3. mplayer output.wav
