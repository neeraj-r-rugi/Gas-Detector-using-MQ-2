from PyQt5.QtCore import QTimer, QThread
import GUI as gui
import serial
import time
from PyQt5.QtMultimedia import QSound
import time
from PyQt5.QtCore import pyqtSignal, QObject
# Replace with the correct COM port
PORT = 'COM5'
BAUDRATE = 9600

dot_count = 0
connction_attempt = False

def connecting_animation():
    global connection_attempt
    global dot_count
    if connction_attempt == True:
        animation_timer.stop()
        return
    dot_count = (dot_count + 1) % 4
    gui.update_text(f"Attempting Connection{'.'*dot_count}")
    
def play_audio():
    QSound.play("alert_sound.wav")

class SerialWorker(QThread): # Signal to Alert Function in GUI
    styling = pyqtSignal(str)
    data_received = pyqtSignal(str)  # Signal to send data safely to UI
    play_sound_signal = pyqtSignal()

    def run(self):
        global connction_attempt
        try:
            ser = serial.Serial(PORT, BAUDRATE, timeout=1)
            time.sleep(5)
            connction_attempt = True
            self.styling.emit("Attempting Connection...\n-> Connected to GDAS...")
            print(f"Connected to GDAS..")

            while True:  
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()
                    if data == '1':
                        self.data_received.emit("Alert! Gas Leak Detected at GDAS - 1")
                        self.play_sound_signal.emit()

                time.sleep(0.1)

        except serial.SerialException as e:
            connction_attempt = True
            self.styling.emit("Attempting Connection...")
            self.data_received.emit(f"Connection Failed! Please check Bluetooth Module:\n{e}")
            gui.quit_program()

        except KeyboardInterrupt:
            connction_attempt = True
            self.data_received.emit("Exiting...")

        finally:
            if 'ser' in locals() and ser.is_open:
                ser.close()
                self.data_received.emit("Closed Connection...")
            else:
                self.data_received.emit("Connection Failure Occurred. Program Terminated.")




animation_timer = QTimer()
animation_timer.timeout.connect(connecting_animation)
animation_timer.start(250)

# serial_thread = run_serial_thread()
serial_worker = SerialWorker()
serial_worker.data_received.connect(gui.add_text)
serial_worker.play_sound_signal.connect(play_audio)   # Ensure GUI updates from the main thread
serial_worker.styling.connect(gui.update_text)
serial_worker.start()

gui.window.show()
gui.sys.exit(gui.app.exec())
