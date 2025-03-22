import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

def clear_text(text):
    text_box.setPlainText("-> Console Cleared.")


def update_text(text):
    text_box.clear()
    text = "-> " + text
    text_box.setPlainText(text)

def add_text(text):
    text = "-> " + text
    text_box.appendPlainText(text)



# Initializing window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("GDAS")
#window.setFixedSize(1440, 810)
window.resize(800, 600)
window.setStyleSheet("background-color: #00ddff;")

# Setting up Grid
grid = QVBoxLayout()
grid.setAlignment(Qt.AlignTop| Qt.AlignHCenter)
grid.setSpacing(20)  # 20 pixels between widgets


# Title Label
title_label = QLabel("GDAS Activity Console")
title_label.setAlignment(Qt.AlignCenter)
title_label.setStyleSheet("""
    padding-left:5px;
    padding-right:5px;
    color: black; 
    font-size: 30px; 
    font-weight: 900;
    font-family: Cascadia Code;
    border: 3px solid black;
    border-radius: 10px;
    background-color: #f7347c;
    """)


# Text Box 
text_box = QPlainTextEdit("-> Preparing connection...")
text_box.setFixedSize(800, 600)  # Adjust size
text_box.setStyleSheet(
    """
    QPlainTextEdit{
    font-size: 20px; 
    font-family: Cascadia Code; 
    font-weight: 900;
    padding-top: 5px;
    background-color: white;
    border: 4px solid black;
    border-radius: 10px;
    padding-left: 5px;
    padding-right: 5px;
    }
    
    QScrollBar:vertical {
    border: none;
    background: #f0f0f0;
    width: 12px;
    margin: 2px 0 2px 0;
    }

    QScrollBar::handle:vertical {
        background: #e31e70;
        min-height: 20px;
        border-radius: 6px;
    }

    QScrollBar::handle:vertical:hover {
        background: #e34688;
    }

    QScrollBar::handle:vertical:pressed {
        background: #eb176f;
    }
    QTextEdit:hover {
    border: 4px solid black; /* Changes color on hover */
    }
        """)
#text_box.setAlignment(Qt.AlignCenter)
text_box.setReadOnly(True)
text_box.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

# Clear Button
button = QPushButton("Clear Console")
button.setFixedSize(180, 60)
button.setStyleSheet(
    """
        QPushButton{background-color: #e31e70;
        font-family: Cascadia Code;
        color: solid black;
        font-size: 17px;
        font-weight: 1000;
        border: 4px solid black;
        border-radius: 10px;}

        QPushButton:hover{
        background-color: #e34688;
        }

        QPushButton:pressed{
        background-color: #eb176f;
        }
    """)
button.clicked.connect(clear_text)

quit_button =QPushButton("Quit")
quit_button.setFixedSize(180, 60)
quit_button.setStyleSheet(
    """
        QPushButton{background-color: #e31e70;
        font-family: Cascadia Code;
        font-size: 17px;
        font-weight: 1000;
        border: 4px solid black;
        border-radius: 10px;}

        QPushButton:hover{
        background-color: #e34688;
        }

        QPushButton:pressed{
        background-color: #eb176f;
        }
    """)
quit_button.clicked.connect(lambda: app.exit())
quit_button.hide()

def quit_program():
    button.hide()
    quit_button.show()

    
    

# Placing Widgets
grid.addWidget(title_label, alignment= Qt.AlignTop)
grid.addWidget(text_box, alignment= Qt.AlignTop)
grid.addWidget(button, alignment= Qt.AlignTop | Qt.AlignHCenter)
grid.addWidget(quit_button, alignment= Qt.AlignTop | Qt.AlignHCenter)
# Set layout
window.setLayout(grid)



# Show window
if __name__ == "__main__":
    window.show()
    sys.exit(app.exec())
