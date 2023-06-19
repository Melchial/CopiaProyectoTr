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

class TranslateNew(QRunnable):
    
    def __init__(self, img,mocr, translator,language, combN=False, combO=False, sliderNum=0):
        super(TranslateNew, self).__init__()
        self.imag1 = img
        self.setting = Settings()
        self.manga = MangaBag()
        self.handling = FileHandler()
        self.name = translator
        self.shouldCombN = combN
        self.shouldCombO = combO
        self.range = sliderNum * self.manga.getRatio(self.imag1[0]) + 4
        self.signals = Worker()
        self.directory = self.setting.cropText
        self.portions = (100 / len(self.imag1))/3
        self.cnt = 0
        self.mocr = mocr
        self.source = None if language == "auto" else language
        self.ratio = 1

    
    def LocateText(self, image):
        myDict = self.manga.get_text(image)
        if self.shouldCombN and self.shouldCombO:
            bound1 = rectanglesCO(myDict, "c")
            bound2 = combine_rectangles(bound1, self.range)
            overlap1 = rectanglesCO(bound2, "o")
            overlap = combine_overlapping_rectangles(overlap1)
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

            # finalRecpos={'C:/Users/zeraf/Documents/ProjectMangaTr/CopiaProyectoTr/007.jpg': 
            #              {'0': QRect(1486, 423, 130, 407), '1': QRect(1162, 1436, 721, 382),
            #                '3': QRect(335, 2066, 52, 216), '4': QRect(660, 2007, 186, 414), 
            #                '5': QRect(974, 2018, 73, 176), '6': QRect(1029, 2012, 125, 361),
            #                 '7': QRect(1558, 1925, 122, 315), '9': QRect(1726, 2273, 112, 454), 
            #                 '10': QRect(1145, 2664, 50, 30), '11': QRect(1181,663, 80, 164),
            #                  '12': QRect(906, 2564, 46, 94)}}  
              
            # print(type(finalRecpos))
            # print(finalRecpos)
                # self.cnt += self.portions
                # self.signals.progress.emit(self.cnt)

                
                # finalText = self.manga.get_japanese(self.image, self.mocr, gotten_text, self.directory)
                # self.cnt += self.portions
                # self.signals.progress.emit(self.cnt)
                # finalTextcopy = finalText.copy()
                # pprint(finalText)
            """
                #find the language on the first final text value
                if self.source == None and finalText != {}:
                    for y in list(finalText.values()):
                        if y != []:
                            self.source = langid.classify(y[0])[0]
                            break
                #
                
                newList = self.manga.translate(finalText, self.name, self.source)
                self.cnt += self.portions
                self.signals.progress.emit(self.cnt)
                # pprint(newList)
                addNewLine1 = self.manga.addNewLine(x, newList, gotten_text, cv2.FONT_HERSHEY_DUPLEX, fontSize, thickness)
                

                final = self.manga.write(self.image, gotten_text, addNewLine1, fontSize, thickness)
                myarray = np.array(final)
                image = qimage2ndarray.array2qimage(myarray)
                finalImg.append(image)
                self.cnt += self.portions
                backup.append((x, gotten_text, finalTextcopy))
                self.signals.progress.emit(self.cnt)
            """
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
