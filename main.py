import contextlib
import wave
from math import floor
from os import remove
from time import sleep
from subprocess import call

# Location of PiFmRds executable
# Name of TTS Audio file
# Location of TTS Audio file
player_location = '~/PiFmRds/src/./pi_fm_rds'
audio_name = 'audio.wav'
audio_location = '/home/aditya/EmergencyBroadcast/' + audio_name


# broadcast: Str Nat Num Num
#  requires: * start >= 88
#            * end <= 107
def broadcast(what, multiplier, start, end):
    # TTS file generator
    call('pico2wave -w ' + audio_location + ' "' + what + '"', shell=True)

    # Duration of Audio
    with contextlib.closing(wave.open(audio_location, 'r')) as audio:
        frames = audio.getnframes()
        rate = audio.getframerate()
        duration = multiplier * (0.6 + (frames / rate))

    command = 'sudo timeout ' + str(duration) + ' ' + player_location + \
              ' -audio ' + audio_location + ' -freq '

    # Broadcasts one frequency at a time
    for freq in range(floor(start * 10), floor(end * 10) + 1):
        call(command + str(freq / 10), shell=True)

    # Clean-up of Audio file after broadcast is over
    remove(audio_location)


while True:
    text = input('\nEnter text to broadcast: ')

    try:
        start, end = map(float,
                         input('Start and end frequency of the broadcast (Press enter for default values): ').split())
    except ValueError:
        start = 88
        end = 107

    try:
        multiplier = int(input('Number of times to repeat message over one frequency: '))
    except ValueError:
        multiplier = 1

    # Prevents users to broadcast outside the FM radio's frequency range
    if start < 88:
        start = 88
    if end > 107:
        end = 107
    if multiplier < 1:
        multiplier = 1

    print('\nBeginning broadcast on ' + str(start) + 'MHz to ' + str(end) + 'MHz in...')
    for i in range(5, -1, -1):
        sleep(1)
        print(i)
    print('\nBroadcast Started!\n')

    # Broadcast starts here!
    broadcast(text, multiplier, start, end)

    # Choice of broadcasting again
    again = input('\nDo you want to broadcast again? (y/n): ')
    if 'y' == again.lower():
        print('\n')
        pass
    elif 'n' == again.lower():
        print('\nNo more broadcasts scheduled, exiting.\n')
        break
    else:
        print('\nIncorrect option, exiting.\n')
