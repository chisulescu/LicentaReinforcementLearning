import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QMessageBox , QMainWindow, QAction, QFileDialog, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Trading bot'
        self.left = 10
        self.top = 40
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox

        # self.box = QLineEdit(self)
        # self.textbox.move(10, 10)
        # self.textbox.resize(280, 40)


        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create textbox2

        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 100)
        self.textbox2.resize(280, 40)

        self.button = QPushButton('Load data', self)
        self.button.move(20, 160)
        self.button.clicked.connect(self.on_load_data)

        # Create a button in the window
        self.button = QPushButton('Start', self)
        self.button.move(20, 200)
        self.button.clicked.connect(self.on_click)

        self.show()






    def on_load_data(self):
        # self.openFileNameDialog()
        # self.openFileNamesDialog()
        self.saveFileDialog()


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text() + self.textbox2.text()
        QMessageBox.question(self, 'Incepem', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)

        if fileName:

            print(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())