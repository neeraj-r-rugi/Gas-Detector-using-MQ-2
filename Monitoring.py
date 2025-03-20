import serial
import time
from playsound import playsound


# Replace with the correct COM port
PORT = 'COM5'
BAUDRATE = 9600

try:
    # Open serial connection to HC-05
    ser = serial.Serial(PORT, BAUDRATE, timeout=1)
    print(f"Connected to GDAS")

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            if data == '1':
                print("Alert! Gas Leak Detected at GDAS - 1")
                playsound('./alert_sound.mp3')
        time.sleep(0.1)

except serial.SerialException as e:
    print("Serial error:", e)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Closed connection.")
