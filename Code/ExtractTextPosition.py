from PyQt5.QtCore import QRunnable, pyqtSignal, QObject,QPoint,QRect
from FileHandling import FileHandler
from Configer import Settings
from loguru import logger

import cv2

from RectangleManipulation import *
from Translation import MangaBag

class Worker(QObject):
    result = pyqtSignal(object)
    stored = pyqtSignal(object)
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    booleans = pyqtSignal(object)
    lang = pyqtSignal(str)
    
    textPos = pyqtSignal(object)

class ExtractTextPosi(QRunnable):
    
    def __init__(self, img,mocr, combN=False, combO=False, sliderNum=2):
        super(ExtractTextPosi, self).__init__()
        self.imag1 = img
        self.setting = Settings()
        self.manga = MangaBag()
        self.handling = FileHandler()
        # self.name = translator
        self.shouldCombN = combN
        self.shouldCombO = combO
        self.range = sliderNum * self.manga.getRatio(self.imag1[0]) + 4
        self.signals = Worker()
        self.directory = self.setting.cropText
        self.portions = (100 / len(self.imag1))/3
        self.cnt = 0
        self.mocr = mocr
        # self.source = None if language == "auto" else language
        self.ratio = 1

    
    def LocateText(self, image):
        myDict = self.manga.get_text(image)
        # print(myDict)
        # print(self.shouldCombN)
        # print(self.shouldCombO)
        if self.shouldCombN and self.shouldCombO:
            # print(myDict)
            bound1 = rectanglesCO(myDict, "c")
            # print(bound1)
            print(self.range)
            bound2 = combine_rectangles(bound1, self.range)
            # print(bound2)
            overlap1 = rectanglesCO(bound2, "o")
            # print(overlap1)
            overlap = combine_overlapping_rectangles(overlap1)
            # print(overlap)
            return overlap
        elif self.shouldCombN and not(self.shouldCombO):
            bound3 = rectanglesCO(myDict, "c")
            bound4 = combine_rectangles(bound3, self.range)
            return bound4
        elif self.shouldCombO and not(self.shouldCombN):
            overlap3 = rectanglesCO(myDict, "o")
            overlap4 = combine_overlapping_rectangles(overlap3)
            return overlap4
        else:
            return myDict


    def run(self):
        finalImg = []
        backup = []
        finalRecpos ={}
        try:
            for x in self.imag1:
                
                fontSize, thickness = self.manga.getFontSizeThickness(x)
                self.img1 = cv2.imread(r"{}".format(x))
                self.image = cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGB)
                gotten_text = self.LocateText(self.image)
                # pprint(gotten_text)
                # print(type(gotten_text))
                # print(gotten_text)
                # print(type(x))
                # print(x)
                finalsq = {}
                for i in gotten_text:
                    x1 = QPoint(gotten_text[i][0][0],gotten_text[i][0][1])
                    y1 = QPoint(gotten_text[i][1][0],gotten_text[i][1][1])
                    finalsq[i]=QRect(x1,y1).normalized()
                finalRecpos[x]=finalsq

            
        except:
            logger.exception("ERROR")
            self.signals.finished.emit()
        else:
            self.signals.textPos.emit(finalRecpos)
            self.signals.result.emit(finalImg)
            # self.signals.stored.emit(backup)
            # self.signals.booleans.emit([self.name, self.shouldCombN, self.shouldCombO, self.range])
            # self.signals.lang.emit(self.source)
            # self.signals.finished.emit()
            #print(addNewLine1)
            

        finally:
            print("deleting files")
            self.handling.deleteFiles(self.directory)
