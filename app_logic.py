from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes import TramStop

def run_app():
    app = QApplication([])
    
    # Set the color and font for all widgets
    app.setStyleSheet("QWidget { background-color: #00174C; color: white; font-family: Roboto; }")
    
    # Create a widget for user to input the name of the tram stop
    searched_name = QLineEdit()
    
    # Create a button widget for submitting the input
    submit_button = QPushButton("Wyświetl")
    
    # Create a layout to arrange the widgets vertically
    layout = QVBoxLayout()
    layout.addWidget(searched_name)
    layout.addWidget(submit_button)
    
    # Create a QWidget to hold the layout
    widget = QWidget()
    widget.setLayout(layout)
    
    # Create a text widget to display the output
    output_text = QTextEdit()
    layout.addWidget(output_text)
    
    # Define a function to handle the button click event
    def handle_submit():
        tram_stop = TramStop(searched_name.text())
        stop_info = tram_stop.get_stop_info()
        output_text.append(stop_info)  # Append the output to the QTextEdit widget
        
    # Connect the button's clicked signal to the handle_submit function
    submit_button.clicked.connect(handle_submit)
    
    widget.show()
    
    app.exec_()

