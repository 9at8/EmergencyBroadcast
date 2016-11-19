from subprocess import call

for freq in range(880, 1070):
    call('sudo timeout 10 ~/PiFmRds/src/./pi_fm_rds -audio ~/EmergencyBroadcast/lookdave.wav -freq ' + str(freq / 10),
         shell=True)
