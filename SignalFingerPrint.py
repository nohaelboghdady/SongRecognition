# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'songRecognition.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication,QFileDialog
from PyQt5.uic import loadUi
import os
from librosa.feature.spectral import mfcc
from numpy import disp, float16
from scipy.io import wavfile
from scipy.signal import spectrogram
import librosa
import matplotlib.pyplot as plt
import PIL as Image
import imagehash
from imagehash import hex_to_hash
import glob
from glob import glob
import librosa.display
from PIL import Image
import imagehash
from imagehash import hex_to_hash
import numpy as np



class Ui_MainWindow( QDialog):
    def setupUi(self, MainWindow):
        
        self.inserted_song=''
        self.inserted_song_hash=0
        self.filePath='./Songs_wav'
        self.comparison_difference=[]
        self.similiraties = []
        self.listSongsPaths=[]
        self.spectograms=[]
        self.data=[]
        self.SampleRateList=[]
        self.featuresList=[]
        self.feature2=[]
        self.feature3=[]
        self.spectroHashList=[]
        self.featureHashList1=[]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 405)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Song1_FileName = QtWidgets.QLineEdit(self.centralwidget)
        self.Song1_FileName.setGeometry(QtCore.QRect(10, 30, 251, 20))
        self.Song1_FileName.setObjectName("Song1_FileName")
        self.Song1_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Song1_Browse.setGeometry(QtCore.QRect(280, 30, 101, 23))
        self.Song1_Browse.setObjectName("Song1_Browse")
        self.Song2_FileName = QtWidgets.QLineEdit(self.centralwidget)
        self.Song2_FileName.setGeometry(QtCore.QRect(10, 70, 251, 20))
        self.Song2_FileName.setObjectName("Song2_FileName")
        self.Song2_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Song2_Browse.setGeometry(QtCore.QRect(280, 70, 101, 23))
        self.Song2_Browse.setObjectName("Song2_Browse")
        self.Song2_Percentage = QtWidgets.QSlider(self.centralwidget)
        self.Song2_Percentage.setGeometry(QtCore.QRect(490, 70, 181, 22))
        self.Song2_Percentage.setOrientation(QtCore.Qt.Horizontal)
        self.Song2_Percentage.setObjectName("Song2_Percentage")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(120, 130, 401, 201))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(350)
        self.tableWidget.verticalHeader().setVisible(True)
        self.Mix_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Mix_Button.setGeometry(QtCore.QRect(540, 100, 75, 23))
        self.Mix_Button.setObjectName("Mix_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Song1_Browse.clicked.connect(lambda:self.browsefiles(self.Song1_Browse))
        self.Song2_Browse.clicked.connect(lambda:self.browsefiles(self.Song2_Browse))
        self.Mix_Button.clicked.connect(self.reading_and_hashing)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        
    def browsefiles(self,button):
        fname=QFileDialog.getOpenFileName(self, 'Open file','./')
        if button==self.Song1_Browse:
            self.Song1_FileName.setText(fname[0])
            self.inserted_song = fname[0]
            print(self.inserted_song)
        else:
            self.Song2_FileName.setText(fname[0])
   
    #file iteration
    def folderSongsPaths(self):
        for song in os.listdir(self.filePath):
            self.listSongsPaths.append(os.path.join(self.filePath,song))
        print(self.listSongsPaths)
        return 0
    
    def Hash(self,data):
        image=Image.fromarray(data)
        return imagehash.phash(image, hash_size=16).__str__()

    
    def creatingSongsSpectrogram(self):
        pass
        # self.folderSongsPaths() 
        # print(self.listSongsPaths)
        # print(len(self.listSongsPaths))
        # for song in self.listSongsPaths:
        #     sampleRate,data1=wavfile.read(song)
        #     self.SampleRateList.append(sampleRate)
        #     # print('11111111111')
        #     if len(data1)>60*sampleRate:
        #         data1=data1[0:60*sampleRate]
        #     self.data.append(data1)    
        #     frequence,time,specgram=spectrogram(data1,sampleRate)
        #     self.spectograms.append(specgram)
            
            
            # librosa.display.specshow(specgram)
            # plt.savefig('./Spectrogram/F1_Song1'+str(song).zfill(3) +'.png')
            # image=Image.open('./Spectrogram/F1_Song1'+str(song).zfill(3) +'.png')
            # specHashed=imagehash.phash(image)
            # self.spectroHashList.append(self.Hash(specgram))
            # print('specHash',self.spectroHashList)
            # self.spectroHashList.append(self.Hash(specgram.astype('float16')))
    
    def maps(self, inputValue: float, inMin: float, inMax: float, outMin: float, outMax: float):
        slope = (outMax-outMin) / (inMax-inMin)
        return outMin + slope*(inputValue-inMin)

    def extractFeatures(self):    
        # print('FFFFFFFFFFFFFFFFFFFFF')
        self.folderSongsPaths() 
        
        # self.data_dir='./Songs_wav/'
        # self.SpectroGram=glob(self.data_dir+'*.wav')
        count =0
        for song in self.listSongsPaths:
            data,sample_rate=librosa.load(song, duration = 60)
            
            mfccs = librosa.feature.mfcc(data, sr=sample_rate)
            # print(mfccs.shape)
            
            X = librosa.stft(data)
            Xdb = librosa.amplitude_to_db(abs(X))
            plt.figure(figsize=(14, 5))
            librosa.display.specshow(Xdb, sr=sample_rate, x_axis='time', y_axis='hz') 
            #If to pring log of frequencies  
            #librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
            plt.colorbar()
            plt.savefig('./Spectrogram1/F1_Song1_'+str(count).zfill(3) +'.png')
            
            
            librosa.display.specshow(mfccs)
            plt.savefig('./Feature1/F1_Song1_'+str(count).zfill(3) +'.png')
            count+=1
        
            
            self.featureHashList1.append(self.Hash(mfccs))
            print('Loading ', count)
            print(self.Hash(mfccs))
            feature=[]
        print('feature ',self.featureHashList1)
        
        #new song
        data,sample_rate=librosa.load(self.inserted_song , duration = 60)
        mfccs = librosa.feature.mfcc(data, sr=sample_rate)
        self.inserted_song_hash = self.Hash(mfccs)
        print(self.inserted_song_hash)
        
        
        for song in range(len(self.listSongsPaths)):
            self.comparison_difference.append(hex_to_hash(self.inserted_song_hash) - hex_to_hash(self.featureHashList1[song]))
            self.similiraties.append((1 - self.maps(self.comparison_difference[song], 0, 255, 0, 1) )* 100)
        
        for song in range(len(self.listSongsPaths)):
            print(self.listSongsPaths[song], ':', self.similiraties[song])

        

    def reading_and_hashing(self):
        # self.creatingSongsSpectrogram()
        # print('Finished Spectro Function')

        self.extractFeatures()
        print('Finished Feature Function')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Song1_Browse.setText(_translate("MainWindow", "Song1_Browse"))
        self.Song2_Browse.setText(_translate("MainWindow", "Song2_Browse"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "             Song-Name                  Similarity-Index"))
        self.Mix_Button.setText(_translate("MainWindow", "Mix"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




