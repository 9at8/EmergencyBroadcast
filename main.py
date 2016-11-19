from subprocess import call

for freq in range(880, 1070:
    call('timeout 10 ~/PiFmRds/src/./pi_fm_rds -freq ' + str(freq/10), shell=True)
