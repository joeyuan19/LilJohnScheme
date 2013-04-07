import winsound
import time
freqs = [20000]			#Freq in Hz
Dur = 100 	# Set Duration To 1000 ms == 1 second

#for i in range(0,100,1):
while(1):
	for i in range(len(freqs)):
		print "Freq:\t",freqs[i]
		time.sleep(1.0)
		print "\tTime:\t",time.clock()
		winsound.Beep(freqs[i],Dur)
	