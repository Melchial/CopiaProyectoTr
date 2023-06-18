from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, QPoint, QRect, QRectF, pyqtSignal
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor, QTextOption, QFont, QCursor
from loguru import logger
import decimal
import copy

class Image(QtWidgets.QLabel):

    def __init__(self, parent):
        super(Image, self).__init__(parent=parent)
        self.setPixmap(QtGui.QPixmap(":/newPrefix/whiteBG.jpg"))
        self.img = None
        self.image = QPixmap(":/newPrefix/whiteBG.jpg")
        self.begin = QPoint()
        self.end = QPoint()
        self.flag = False
        self.pages = {}
        self.pagesRect = {}
        self.connectDict = {}
        self.translated = {}
        self.japanese = {}
        self.color = {
            "White" : QColor(255, 255, 255),
            "Black" : QColor(0, 0, 0),
            "Red" : QColor(255, 0, 0),
            "Blue" : QColor(0, 0, 255),
            "Green" : QColor(0, 255, 0)
        }
        self.bg = "White"
        self.textColor = "Red"
        self.fontNum = 6
        self.rect = True
        self.scaledDict = {}
        self.erase = False
        self.nContCuad = 0
        self.isPressed = False
        self.factX = 1
        self.factX = 1

    def actContCuad(self):
        ov = []
        for ind in self.pages[self.img]:
            ov.append(int(ind))
        self.nContCuad=max(ov)

    def updateContCuad (self):
        long = len(self.pages[self.img])
        var = [].extend(range(0,long))      
        inner = []
        over = []
        
        for ind in self.pages[self.img]:
          if ind.int() not in var:
              over.append(ind.int())
        for ind in var:
            if ind in self.pages[self.img]:
                inner.append(ind)
        

    def actfactor (self):
        pixWidth = self.image.width()
        pixHeight = self.image.height()
        self.factX =  float(self.frameGeometry().width())/float(pixWidth)
        self.factY = float(self.frameGeometry().height())/float(pixHeight)        

    def rectFactor (self, qRect, invers=False):
        factX = self.factX
        factY = self.factY
        if invers:
            factX = float(1)/factX
            factY = float(1)/factY    
        newX = int(qRect.x() * factX)
        newY = int(qRect.y() * factY)
        newWidth = int(qRect.width() * factX)
        newHeight = int(qRect.height() * factY)
        qRectNew = QRect( newX,newY,newWidth,newHeight)
        # print(factX)
        # print(factY)
        return(qRectNew)

    def refactor (self):
        if self.pages != {}:
            print("refactor")
            if self.pagesRect == {}:
                # print("copia todo")
                # print(self.pages)
                # print(self.pagesRect)
                self.pagesRect = copy.deepcopy(self.pages)
                # print(self.pagesRect)
            # print(self.pages)
            # print(self.pagesRect)
            self.actfactor()
            self.pagesRect[self.img] = copy.deepcopy(self.pages[self.img])         
            # print(self.factX)
            # print(self.factY)
            for f in self.pagesRect[self.img]:
                # print(self.pagesRect[self.img][f])
                self.pagesRect[self.img][f] = self.rectFactor(self.pages[self.img][f])

            # print(self.pages)
            # print(self.pagesRect)
            # print(ImgX)
            # qQuadRe =QRect(newx,newy,neww,newh)
            # print(qQuadRe)
            # return(qQuadRe)

    @logger.catch
    def paintEvent(self, event):
        super().paintEvent(event)
        print("paint event")
        # print(self.pages)
        # print(self.pagesRect)
        if self.flag and self.img != None:
            if self.erase:
                self.changeCursor()
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))
            qp = QPainter(self)
            qp.setPen(QPen(self.color[self.textColor], 2, Qt.SolidLine))
            # self.setPixmap(self.image)
            if self.rect:
                # rects = []
                if self.pages != {}:
                    if self.pagesRect == {}:
                        self.refactor()     
                    for f in self.pagesRect[self.img]:
                        if self.pagesRect[self.img][f]!= self.pages[self.img][f] or self.pagesRect[self.img][f] == None :
                            
                            self.refactor()
                            # rects.append(self.pages[self.img][f])
                            # print(type(self.pages[self.img][f]))
                            # print(self.pages[self.img][f])
                            # rect = self.refactor(QRect(self.pages[self.img][f]).normalized())
                        qp.drawRects(self.pagesRect[self.img][f])
                    # print(rects)
                    # qp.drawRects(rects)
            if self.connectDict != {} and self.translated != {}:
                for index, words in enumerate(self.translated[self.connectDict[self.img]]):
                    a, b, c, d, = self.pages[self.img][index].getRect()
                    if self.bg != "None":
                        qp.fillRect(self.pages[self.img][index], self.color[self.bg])
                    qp.setFont(QFont("Comic Sans MS",self.fontNum));
                    option = QTextOption()
                    option.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    qp.drawText(QRectF(a, b, c, d), words, option)

            if not self.begin.isNull() and not self.end.isNull():
                # a=1
                qp.drawRect(QRect(self.begin, self.end).normalized())
            # self.setPixmap(self.image)
        # print (type(self.pages))
        # print (self.pages)

    def mousePressEvent(self, event):
        if self.flag and self.img != None:
            self.isPressed=True
            if self.erase:
                self.changeCursor()
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))
                self.begin = self.end = event.pos()
                self.update()
        super().mousePressEvent(event)
            # print(type(self.pages[self.img]))
            # print(self.pages[self.img])
   
   
    @logger.catch
    def resizeEvent(self, event):
        if self.flag and self.img != None:
            # self.refactor()
            super().resizeEvent(event)

    @logger.catch
    def mouseMoveEvent(self, event):
        if self.flag and self.img != None:
            if self.erase:
                self.changeCursor()
                self.end = event.pos()
                self.update()
                nL = []
                p1 = self.end.x()
                p2 = self.end.y()
                print(p1)
                print(p2)
                if self.pages[self.img] != []:
                    # for index, rect in enumerate(self.pages[self.img]):
                    #     x, y, w, h = rect.getRect()
                    #     if p1 >= x and p1 <= x+w and p2 >= y and p2 <= y+h:
                    #         nL.append((self.img, index))
                    for index in self.pages[self.img]:
                        x, y, w, h = self.rectFactor(self.pages[self.img][index]).getRect()
                        if p1 >= x and p1 <= x+w and p2 >= y and p2 <= y+h:
                            nL.append((self.img, index))
                    
                    for img, index in nL:
                        print(index)
                        del self.pages[img][index]
                        self.refactor()
                    self.actContCuad()
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))
                self.end = event.pos()
                self.update()
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.flag and self.img != None:
            
            if self.erase:
                self.changeCursor()
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))
                r = QRect(self.begin, self.end).normalized()
                # self.pages[self.img].append(r) #se modifica a una dict en lugar de una lista
                
                self.nContCuad +=1
                self.pages[self.img][f"{self.nContCuad}"]=self.rectFactor( QRect(self.begin,self.end) ,True)
                self.begin = self.end = QPoint()
                self.refactor()
                self.update()
                self.isPressed=False
        super().mouseReleaseEvent(event)
    
    def changeCursor(self):
        cursor = QPixmap(":/newPrefix/eraser.png")
        cursorScaled = cursor.scaled(QtCore.QSize(35, 35), Qt.KeepAspectRatio)
        currCursor = QCursor(cursorScaled, -1, -1)
        self.setCursor(currCursor)