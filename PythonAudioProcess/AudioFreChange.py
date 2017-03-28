from AudioLib.MyFunctions import *

M = input('Please Rnter a New M for dividing the Audio Sequence:')
inputfile = '/home/ubuntu-mm/Downloads/Audio.wav'
outputfile = '/home/ubuntu-mm/Desktop/Audio.wav'
downsampleAudio(inputfile, outputfile, M)
wavplay(outputfile)
x_in = readAudio(inputfile)
In_DFT = DFT(x_in)
In_IDFT = IDFT(In_DFT)
print 'The sequences of the Audio:',x_in
print 'The spectrume of the Audio:',In_DFT
print 'The sequence after IDFT is:',In_IDFT.real
