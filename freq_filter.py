import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyaudio
import struct
import wave
import time
 

SAVE = 0.0			#Save > 0.0 ; time for recording	
TITLE = 'Test'	
FPS = 25.0
 
nFFT = 512
BUF_SIZE = 4 * nFFT
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

FREQ_TARGET = 20000		# Target frequency (Hz)
 
def process(stream,MAX_y):
  # Read n*nFFT frames from stream, n > 0
  N = max(stream.get_read_available() / nFFT, 1) * nFFT
  data = stream.read(N)
  # Unpack data, LRLRLR...
  y = np.array(struct.unpack("%dh" % (N * CHANNELS), data)) / MAX_y
  y_L = y[::2]
  y_R = y[1::2]
 
  Y_L = np.fft.fft(y_L, nFFT)
  Y_R = np.fft.fft(y_R, nFFT)
 
  # Sewing FFT of two channels together, DC part uses right channel's
  Y = abs(np.hstack((Y_L[-nFFT/2:-1], Y_R[:nFFT/2])))
  
  #	Lower kHz Limit = 15000 Hz -> Y[429]
  #
  fOi = Y[429:]
  #print fOi.argmax()
  #print time stamp
  if fOi.argmax() == 58 and fOi[58]>=1.00:
  	print "Amp:\t", fOi[58]
  	print "\tTime:\t",time.clock()
 
p = pyaudio.PyAudio()
# Used for normalizing signal. If use paFloat32, then it's already -1..1.
# Because of saving wave, paInt16 will be easier.
MAX_y = 2.0**(p.get_sample_size(FORMAT) * 8 - 1)
 
frames = None
wf = None

stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=BUF_SIZE)
while(1):
  process(stream,MAX_y)
stream.stop_stream()
stream.close()
p.terminate()
 