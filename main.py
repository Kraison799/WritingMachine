import sys

from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtWidgets import (QWidget, QPlainTextEdit, QTextEdit,
                             QMainWindow, QAction, qApp, QApplication)
from PyQt5.QtGui import QColor, QPainter, QTextFormat, QPalette, QKeySequence, QFont

from tkinter.filedialog import askopenfilename

from tkinter import messagebox as mb
import tkinter as tk

import Compiler.Lexical.Lexer as Lexer

qtCreatorFile = "IDE.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor


    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)

    def paintEvent(self, event):
        self.codeEditor.lineNumberAreaPaintEvent(event)


class PlainTextEdit(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.lineNumberArea = LineNumberArea(self)
        Palette = QPalette()
        Palette.setColor(QPalette.Text, Qt.white)
        self.setPalette(Palette)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)
        self.updateLineNumberAreaWidth(0)

    def lineNumberAreaWidth(self):
        digits = 1
        max_value = max(1, self.blockCount())
        while max_value >= 10:
            max_value /= 10
            digits += 1
        space = 3 + self.fontMetrics().width('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)
        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()
        height = self.fontMetrics().height()

        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = str(blockNumber + 1)
                painter.setPen(Qt.black)
                painter.drawText(0, top, self.lineNumberArea.width(), height, Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    global nombrearch

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.b_load.clicked.connect(self.buttonClicked)
        self.b_save.clicked.connect(self.save)
        self.b_compile.clicked.connect(self.On_compile_click)
        self.b_run.clicked.connect(self.Run_code)

        self.errores.setStyleSheet("QPlainTextEdit { color: green}")
        self.errores.setReadOnly(1)
        self.errores.setMaximumHeight(150)

    def buttonClicked(self):
        try:
            global nombrearch
            nombrearch = askopenfilename(initialdir="/", title="Seleccione archivo",
                                         filetypes=(("txt files", "*.txt"), ("todos los archivos", "*.*")))
            if nombrearch != '':
                archi1 = open(nombrearch, "r", encoding="utf-8")
                contenido = archi1.read()
                archi1.close()
                codeEditor.setPlainText(contenido)
        except:
            print("Ningun archivo fue seleccionado")


    def save(self):
        global nombrearch

        try:
            if nombrearch != '':
                archi1 = open(nombrearch, "w", encoding="utf-8")
                archi1.write(codeEditor.toPlainText())
                archi1.close()
                mb.showinfo("Información", "Los datos fueron guardados en el archivo.")
        except:
            print("ERROR")
            ###mb.showinfo("Ocurrio un error, asegurese de haber cargado un archivo previamente")


    def Compile_start(self):
        ###Funcion para compilar
        print("compilado")

    def On_compile_click(self):

        ###Llamado de la compilacion y recibe la respuesta del compilador desde la funcion compile_start
        respuesta = "El codigo se compilo correctamente"

        self.errores.clear()
        self.errores.insertPlainText(respuesta)

    def Run_code(self):
        ### Envia el codigo compilado usando compile_start
        print("Ejecucion")
        Lexer.lex_test(codeEditor)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    codeEditor = PlainTextEdit()
    window.v_layout.addWidget(codeEditor)
    window.show()

    sys.exit(app.exec())
