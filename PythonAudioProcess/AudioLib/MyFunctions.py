import numpy as np
from scipy.signal import resample, blackmanharris, triang
from scipy.fftpack import fft, ifft, fftshift
import math, copy, sys, os
from scipy.io.wavfile import write, read
from sys import platform
from numpy import *
import subprocess

###############################################################################################################

# Math Number Functions Collection!

###############################################################################################################
def isPower2(num):
        """
        Check if num is power of two
        """
        return ((num & (num - 1)) == 0) and num > 0

def sinc(x, N):
        """
        Generate the main lobe of a sinc function (Dirichlet kernel)
        x: array of indexes to compute; N: size of FFT to simulate
        returns y: samples of the main lobe of a sinc function
        """

        y = np.sin(N * x/2) / np.sin(x/2)                  # compute the sinc function
        y[np.isnan(y)] = N                                 # avoid NaN if x == 0
        return y

###############################################################################################################

# Single Processing Functions Collection!

###############################################################################################################

INT16_FAC = (2**15)-1
INT32_FAC = (2**31)-1
INT64_FAC = (2**63)-1
norm_fact = {'int16':INT16_FAC, 'int32':INT32_FAC, 'int64':INT64_FAC,'float32':1.0,'float64':1.0}

def wavread(filename):
        """
        Read a sound file and convert it to a normalized floating point array
        filename: name of file to read
        returns fs: sampling rate of file, x: floating point array
        """

        if (os.path.isfile(filename) == False):                  # raise error if wrong input file
                print("Input file does not exist. Make sure you computed the analysis/synthesis")

        fs, x = read(filename)

        if (len(x.shape) !=1):                                   # raise error if more than one channel
                raise ValueError("Audio file should be mono")

        if (fs !=44100):                                         # raise error if more than one channel
                raise ValueError("Sampling rate of input sound should be 44100")

        #scale down and convert audio into floating point number in range of -1 to 1
        x = np.float32(x)/norm_fact[x.dtype.name]
        return fs, x
def wavplay(filename):
        """
        Play a wav audio file from system using OS calls
        filename: name of file to read
        """
        if (os.path.isfile(filename) == False):                  # raise error if wrong input file
                print("Input file does not exist. Make sure you computed the analysis/synthesis")
        else:
                if sys.platform == "linux" or sys.platform == "linux2":
                    # linux
                    subprocess.call(["aplay", filename])

                elif sys.platform == "darwin":
                        # OS X
                        subprocess.call(["afplay", filename])
                elif sys.platform == "win32":
                        if winsound_imported:
                                winsound.PlaySound(filename, winsound.SND_FILENAME)
                        else:
                                print("Cannot play sound, winsound could not be imported")
                else:
                        print("Platform not recognized")
def wavwrite(y, fs, filename):
        """
        Write a sound file from an array with the sound and the sampling rate
        y: floating point array of one dimension, fs: sampling rate
        filename: name of file to create
        """

        y *= INT16_FAC                               # scaling floating point -1 to 1 range signal to int16 range
        y = np.int16(y)                              # converting to int16 type
        write(filename, fs, y)
def readAudio(inputFile):
	"""
	Input:
		inputFile: the path to the wav file      
	Output:
		The function should return a numpy array that contains 10 samples of the audio.
	"""
	fs, x = wavread(inputFile)
	samples = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],'float32')
	for i in range(10):
		samples[i] = x[50000+i]
	return samples

def hopSamples(x,M):
	'''
	Comment for function hopSamples()
	'''
	N = len(x)
	index = 0
	axis = 0
	i = 0
	j = 0
	while i<=N-1:
		i = i + M
		j = j + 1
	Res = linspace(-1.0,1.0,j)
	while axis<=j-1:
		Res[axis] = x[index]
		index = index + M
		axis = axis + 1
	return Res
def minMaxAudio(inputfile):
	'''
	'''
	List = [0, 0]
	fs, x = wavread(inputfile)
	List[0] = min(x)
	List[1] = max(x)
	return List
def downsampleAudio(inputfile, outputfile, M):
	"""
	Inputs:
	inputFile: file name of the wav file (including path)
	        M: downsampling factor (positive integer)
	"""
	F,y = read(inputfile)
	fs, x = wavread(inputfile)
	len_x = len(x)
	DownSam = hopSamples(x, M)
	fs1 = (int)(fs*len(DownSam)/len_x)
	wavwrite(DownSam, fs1, outputfile)
def DFT(x):
	"""
	Input:
		x (numpy array) = input sequence of length N
	Output:
		The function should return a numpy array of length N
		X (numpy array) = The N point DFT of the input sequence x
	"""
	N = len(x)
	real = np.zeros(N)
	imag = np.zeros(N)
	for i in range(N):
		for j in range(N):
			real[i] += x[j]*np.cos(-2*np.pi*i*j/N)
			imag[i] += x[j]*np.sin(-2*np.pi*i*j/N)
	Res = 1j*imag + real
	return Res
def IDFT(X):
	"""
	Input:
		X (numpy array) = frequency spectrum (length N)
	Output:
		The function should return a numpy array of length N 
		x (numpy array) = The N point IDFT of the frequency spectrum X
	"""
	N = len(X)
	real = np.zeros(N)
	imag = np.zeros(N)
	for i in range(N):
		for k in range(N):
			param1 = X[k].real
			param2 = X[k].imag
			sin = np.sin(2*np.pi*i*k/N)
			cos = np.cos(2*np.pi*i*k/N)
			real[i] += param1*cos-param2*sin
			imag[i] += param1*sin+param2*cos
	Res = 1j*imag/N + real/N
	return Res
def DWT(x,Type):
	"""
	Input:
	Output:
	"""
	L = len(x)
	Size = 50
	TransRes = np.zeros([Size,Size])
	if Type=='Haar':
		for a in range(Size):
			for t in range(Size):
				for n in range(L):
					index = (float)((n-t)/(a+0.01))
					if (index>0 and index<=0.5): Fai = 1
					if (index>0.5 and index<=1): Fai = -1
					else : Fai = 0
					TransRes[a][t] += x[n]*Fai/np.sqrt(a)
	if Type=='MexicanHat':
                for a in range(Size):
                        for t in range(Size):
                                for n in range(L):
					index = (float)((n-t)/(a+0.01))
					index2 = pow(index,2)
                                        Fai = (1-index2)*np.exp(index2/2)
                                        TransRes[a][t] += x[n]*Fai/np.sqrt(a)
	return TransRes

###############################################################################################################

# String Processing Functions Collection!

###############################################################################################################

def OnlyCharNum(s,oth=''):
    s2 = s.lower();
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'');
    return s;
###############################################################################################################

# Calculate the biggest common divide factor of N1 and N2

###############################################################################################################
def gcd(N1, N2):
    Min = min(N1, N2)
    Res = 1
    for d in range(1, Min+1):
        if divmod(N1, d)[1] == 0 and divmod(N2, d)[1] == 0:
            Res = d
    return Res
