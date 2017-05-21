# -*- coding: UTF-8 -*-

import numpy as np
import  matplotlib.pyplot as plt
from scipy.io import wavfile
import wavio
import wave as _wave
import tempfile
import os

class audioFileAnalysis:
    """docstring for audioFile."""
    def __init__(self, filePath):
        # call method loadData
        self.fe, self.sig, self.fmax = None, None, None
        self.filePath = filePath
        self.loadData()

        # default Nfft, Nwin, winTyp
        self.Nwin = 512
        self.Nfft = self.Nwin
        self.over = 0.5
        self.Nwin = int(self.over * self.Nfft)
        self.f, self.t = [], []

    def loadData(self):
        """loadData(self)
        Loads audioFile as a numpy array whose value is
        contained between [-1,1]"""

        # reads file and gets main information
        _file = _wave.open(self.filePath)
        self.getFileNFO(_file)
        _file.close()

        # computes additionnal informations
        self.Te = 1./self.Fe
        self.fmax = self.Fe / 2

        self.updateVectors()

    def getFileNFO(self, _file):
        self.Fe = _file.getframerate()
        self.Nch = _file.getnchannels()
        self.N = _file.getnframes()
        self.Nfft = self.N
        self.sig = _file.readframes(self.N)



    def updateVectors(self):
        # timeVector
        self.t = np.arange(self.N) * self.Te
        # frequencyVector
        self.f = np.linspace(-self.fmax, self.fmax, num=self.Nfft)

    def plot(self, dimension='time'):
        plt.figure()
        plt.plot(self.t, self.sig)


class pyplotLabels:
    """docstring for pyplotLabels."""
    def __init__(self, plotType, title=''):
        self.plotType = plotType
        self.x, self.y, self.title = None, None, None

        if self.plotType == "time":
            self.x = "Time (s)"
            self.y = "Amplitude"
            self.title = "Temporal representation"

        if self.plotType == "freq":
            self.x = "Frequency (Hz)"
            self.y = "Amplitude"
            self.title = "Spectral representation"
