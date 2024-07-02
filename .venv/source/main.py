#Import GUI stuff
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

"""
import RPi.GPIO as GPIO

GPIO.setwarnings(False) #omitir as mensagens do rasp
GPIO.setmode(GPIO.BOARD) #modo de trabalhar com a placa
GPIO.setup(12, GPIO.OUT) #último
GPIO.setup(16, GPIO.OUT) #meio
GPIO.setup(18, GPIO.OUT) #primeiro

GPIO.output(12,1)
GPIO.output(16,1)
GPIO.output(18,1)
"""



# TEXT BUTTONS
on = "TURN ON"
off = "TURN OFF"

#COLOR LABEL
on_label_color = '#008000'
off_label_color = '#ff4b2b'


# Label Border CSS Configuration
button_css = "border-radius: 7px; background: white; padding: 5px"

#A intance of a Janela contains the command used to renderize the GUI
class Janela(QMainWindow):
    def __init__(self):
        super(Janela, self).__init__()
        #renderize GUI
        loadUi("window.ui", self)
        self.init_components()

    def init_components(self):
        # PNEUMATIC POWER SOURCE
        self.pneumatic_pwr_source_label.setStyleSheet(f'background: {off_label_color};'
                                                      'color: white;'
                                                      'border-radius: 8px')
        self.pneumatic_pwr_source_button.setStyleSheet(button_css)

        # DOOR JAMED
        self.door_jamed_label.setStyleSheet(f'background: {off_label_color};'
                                            'color: white;'
                                            'border-radius: 8px')
        self.door_jamed_button.setStyleSheet(button_css)

        # DOOR HANDLE JAMED
        self.door_handle_jamed_label.setStyleSheet(f'background: {off_label_color};'
                                            'color: white;'
                                            'border-radius: 8px')
        self.door_handle_jamed_button.setStyleSheet(button_css)

        # POWER ASSIST
        self.power_assist_label.setStyleSheet(f'background: {off_label_color};'
                                                   'color: white;'
                                                   'border-radius: 8px')
        self.power_assist_button.setStyleSheet(button_css)

        # POWER ASSIST INDICATOR
        self.power_assist_indicator_label.setStyleSheet(f'background: {off_label_color};'
                                                   'color: white;'
                                                   'border-radius: 8px')
        self.power_assist_indicator_button.setStyleSheet(button_css)

        # POWER ASSIST FAILURE OPEN
        self.power_assist_failure_open_label.setStyleSheet(f'background: {off_label_color};'
                                                        'color: white;'
                                                        'border-radius: 8px')
        self.power_assist_failure_open_button.setStyleSheet(button_css)

        # SLIDE PRESSURE INDICATOR
        self.slide_pressure_indicator_label.setStyleSheet(f'background: {off_label_color};'
                                                           'color: white;'
                                                           'border-radius: 8px')
        self.slide_pressure_indicator_button.setStyleSheet(button_css)

        # POWER ASSIST FAILURE CLOSE
        self.power_assist_failure_close_label.setStyleSheet(f'background: {off_label_color};'
                                                          'color: white;'
                                                          'border-radius: 8px')
        self.power_assist_failure_close_button.setStyleSheet(button_css)


    #Called everytime one of the buttons of the screen is clicked
    #The method operates over the instance of the buttons that was clicked
    def auxiliar_method(self, btn, label):
        # Change the text of the button to "off"
        # Change the label background color to "green"
        if btn.text() == on:
            btn.setText(off)
            label.setStyleSheet(f'background: {on_label_color};'
                                'color: white;'
                                'border-radius: 8px')

        # Change the text of the button to "on"
        # Change the label background color to "red"
        else:
            btn.setText(on);
            label.setStyleSheet(f'background: {off_label_color};'
                                'color: white;'
                                'border-radius: 8px')



    #Executed when the button pneumatic_pwr_source is clicked
    @pyqtSlot()
    def on_pneumatic_pwr_source_button_clicked(self):
        self.auxiliar_method(self.pneumatic_pwr_source_button, self.pneumatic_pwr_source_label)

    # Executed when the button door_jamed is clicked
    @pyqtSlot()
    def on_door_jamed_button_clicked(self):
        self.auxiliar_method(self.door_jamed_button, self.door_jamed_label)

    # Executed when the button door_handle_jamed is clicked
    @pyqtSlot()
    def on_door_handle_jamed_button_clicked(self):
        self.auxiliar_method(self.door_handle_jamed_button, self.door_handle_jamed_label)

    # Executed when the button power_assist is clicked
    @pyqtSlot()
    def on_power_assist_button_clicked(self):
        self.auxiliar_method(self.power_assist_button, self.power_assist_label)

    # Executed when the button power_assist_indicator is clicked
    @pyqtSlot()
    def on_power_assist_indicator_button_clicked(self):
        self.auxiliar_method(self.power_assist_indicator_button, self.power_assist_indicator_label)

    # Executed when the button power_assist_failure_open is clicked
    @pyqtSlot()
    def on_power_assist_failure_open_button_clicked(self):
        self.auxiliar_method(self.power_assist_failure_open_button, self.power_assist_failure_open_label)

    # Executed when the button power_assist_failure_close is clicked
    @pyqtSlot()
    def on_power_assist_failure_close_button_clicked(self):
        self.auxiliar_method(self.power_assist_failure_close_button, self.power_assist_failure_close_label)

    # Executed when the button slide_pressure_indicator is clicked
    @pyqtSlot()
    def on_slide_pressure_indicator_button_clicked(self):
        self.auxiliar_method(self.slide_pressure_indicator_button, self.slide_pressure_indicator_label)


#Execute the program
if __name__ == "__main__":
    import sys
    app=QApplication(sys.argv)
    my_janela=Janela()
    my_janela.show()
    app.exec_()