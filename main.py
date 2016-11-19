from subprocess import call

for freq in range(88.0, 107.9, 0.1):
    call('timeout 10 ~/PiFmRds/src/./pi_fm_rds -freq ' + str(freq), shell=True)