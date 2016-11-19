import contextlib
import wave
from subprocess import call

player_location = '~/PiFmRds/src/./pi_fm_rds'
audio_name = 'audio.wav'
audio_location = '/home/aditya/EmergencyBroadcast/' + audio_name


def broadcast(what, multiplier):
    call('pico2wave -w ' + audio_location + ' "' + what + '"', shell=True)

    with contextlib.closing(wave.open(audio_location, 'r')) as audio:
        frames = audio.getnframes()
        rate = audio.getframerate()
        duration = 0.2 + multiplier * frames / rate

    command = 'sudo timeout ' + str(duration) + ' ' + player_location + \
              ' -audio ' + audio_location + ' -freq '

    for freq in range(880, 1070):
        call(command + str(freq / 10), shell=True)


broadcast('Hello World! This is a great thing, let us see if this works lol.', 1)
