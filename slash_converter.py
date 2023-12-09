import sys
import pyperclip
from pathlib import PureWindowsPath
from PyQt6.QtGui import QTextOption 
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QTextEdit, QPushButton


class SlashConverter(QWidget):
    def __init__(self, parent : QWidget=None):
        super().__init__(parent)

        self.input_group_box = QGroupBox('input', self)
        self.output_group_box = QGroupBox('output', self)

        self.input_text_edit = QTextEdit(self)
        self.input_text_edit.setAcceptRichText(False)
        self.input_text_edit.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)
        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setAcceptRichText(False)
        self.output_text_edit.setWordWrapMode(QTextOption.WrapMode.WrapAnywhere)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.input_text_edit)
        self.input_group_box.setLayout(hbox1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.output_text_edit)
        self.output_group_box.setLayout(hbox2)

        self.convert_btn = QPushButton('/', self)
        self.dbl_splash_btn= QPushButton('\\\\', self)
        h_btn_box = QHBoxLayout()
        h_btn_box.addWidget(self.convert_btn)
        h_btn_box.addWidget(self.dbl_splash_btn)

        self.copy_btn = QPushButton('Copy to clipboard', self)

        mainLayout = QVBoxLayout(self)
        self.setLayout(mainLayout)
        mainLayout.addWidget(self.input_group_box)
        mainLayout.addLayout(h_btn_box)
        mainLayout.addWidget(self.output_group_box)
        mainLayout.addWidget(self.copy_btn)

        self.convert_btn.clicked.connect(self.slot_convert_splash)
        self.dbl_splash_btn.clicked.connect(self.slot_add_double_splash)
        self.copy_btn.clicked.connect(self.slot_copy_to_clipboard)

        self.resize(400, 200)
        self.setWindowTitle('Slash Converter')

    def slot_convert_splash(self):
        text = self.input_text_edit.toPlainText()
        if text:
            cur_path = PureWindowsPath(text)
            self.output_text_edit.setPlainText(cur_path.as_posix())
        return

    def slot_add_double_splash(self):
        text = self.input_text_edit.toPlainText()
        if text:
            cur_path = PureWindowsPath(text)
            temp = str(cur_path).replace('\\', "\\\\")
            self.output_text_edit.setPlainText(temp)
        return
    
    def slot_copy_to_clipboard(self):
        pyperclip.copy(self.output_text_edit.toPlainText())
        return


if __name__ == "__main__":
    a = QApplication(sys.argv)
    widget = SlashConverter()
    widget.show()
    a.exec()