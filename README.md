# GDAS: Gas Detection and Alert System

## Overview

The Gas Detection and Alert System (GDAS) is a highly modular and extensible solution designed to detect hazardous gas levels using the MQ-2 gas sensor and provide real-time alerts through local (buzzer and inbuilt Arduino LED) and remote (Bluetooth to a laptop GUI) mechanisms. Built with an Arduino UNO, HC-05 Bluetooth module, and a passive buzzer, GDAS ensures timely detection and notification of gas leaks, enhancing safety in environments prone to gas hazards, such as industrial settings, laboratories, or residential spaces.

The system's modular architecture allows seamless integration of additional components, such as LoRa modules for long-range communication, additional sensors, or alternative alert mechanisms. This extensibility makes GDAS adaptable to diverse use cases, from small-scale home monitoring to large-scale industrial deployments.

## Features

- **Real-Time Gas Detection**: Utilizes the MQ-2 gas sensor to detect hazardous gas levels (e.g., LPG, methane, smoke) with a threshold-based alert system.
- **Local Alerts**: Triggers a passive buzzer and the inbuilt Arduino LED (pin 13) when gas levels exceed safe limits (threshold: 300).
- **Remote Monitoring**: Streams alerts to a laptop via the HC-05 Bluetooth module, displayed on a PyQt5-based GUI.
- **Highly Modular and Extensible**: Designed for easy integration of additional modules, such as LoRa for long-range communication, multiple sensors, or alternative notification systems (e.g., Wi-Fi, GSM).
- **User-Friendly Interface**: A clean, responsive GUI with a console-style display for connection status and alerts.
- **Robust Error Handling**: Manages connection failures and serial communication errors with graceful termination.
- **Customizable**: Supports dynamic threshold adjustments and integration of new hardware or software components.

## Hardware Requirements

### Core Components
- **Arduino UNO**: Microcontroller for processing sensor data and controlling outputs, with inbuilt LED on pin 13 for visual alerts.
- **MQ-2 Gas Sensor**: Detects flammable gases (e.g., LPG, methane, smoke).
- **HC-05 Bluetooth Module**: Enables wireless communication with the monitoring laptop.
- **Passive Buzzer**: Provides audible alerts for local notification.
- **Jumper Wires and Breadboard**: For circuit connections.
- **Laptop/PC**: For running the Python-based GUI and receiving Bluetooth alerts.

### Optional (for Extensibility)
- **LoRa Module**: For long-range, low-power communication in remote or industrial settings.
- **Additional sensors** (e.g., MQ-3, MQ-7) for detecting other gases.
- **Wi-Fi or GSM modules** for alternative communication protocols.

## Software Requirements

### Required Software
- **Arduino IDE**: For uploading the `MES_GAS_SENSOR_CODE.ino` to the Arduino UNO.
- **Python 3.x**: For running the monitoring GUI and serial communication.

### Python Libraries
- **PyQt5**: For the graphical user interface.
- **pyserial**: For serial communication with the HC-05 module.
- **PyQt5.QtMultimedia**: For playing alert sounds.

### Operating System
- **Windows** (for Bluetooth COM port configuration) or any OS supporting PyQt5 and serial communication.

### Optional (for Extensibility)
- Libraries for LoRa communication (e.g., RadioHead for Arduino, pylora for Python).
- Libraries for additional protocols (e.g., ESP8266WiFi for Wi-Fi).

## Modularity and Extensibility

GDAS is designed with a modular architecture to facilitate easy expansion and customization:

### Hardware Modularity
- **LoRa Integration**: Add a LoRa module (e.g., SX1278) to enable long-range communication (up to several kilometers) for remote monitoring in areas without Bluetooth coverage. Connect the LoRa module to the Arduino's SPI pins and modify the firmware to transmit alerts via LoRa.
- **Multi-Sensor Support**: Incorporate additional gas sensors (e.g., MQ-3 for alcohol, MQ-7 for carbon monoxide) by connecting them to available analog pins and updating the Arduino code to process multiple sensor inputs.
- **Alternative Communication**: Replace or supplement the HC-05 with Wi-Fi (e.g., ESP8266) or GSM modules for internet-based or SMS alerts.

### Software Extensibility
- **Dynamic Thresholds**: Modify the Python GUI to allow users to adjust gas detection thresholds dynamically via input fields.
- **Data Logging**: Extend `Monitoring.py` to log sensor data and alerts to a file or database for historical analysis.
- **Custom Notifications**: Add support for email, push notifications, or cloud-based dashboards by integrating APIs or libraries like `smtplib` or `paho-mqtt`.

### Scalability
The system's decoupled design (Arduino for sensing, Python for monitoring) allows components to be independently upgraded or replaced, making it suitable for both prototyping and production environments.

## Installation and Setup

### Hardware Setup

#### Connect the MQ-2 Gas Sensor
1. Connect the MQ-2's VCC to Arduino's 5V pin.
2. Connect GND to Arduino's GND.
3. Connect the analog output (AOUT) to Arduino's A0 pin.

#### Connect the HC-05 Bluetooth Module
1. Connect VCC to Arduino's 5V pin.
2. Connect GND to Arduino's GND.
3. Connect TX to Arduino's pin 10 (RX).
4. Connect RX to Arduino's pin 11 (TX).

#### Connect the Buzzer
1. Connect the positive leg of the passive buzzer to Arduino's pin 6.
2. Connect the negative leg to Arduino's GND.

#### Utilize the Inbuilt LED
The inbuilt LED on Arduino's pin 13 is used for visual alerts; no external LED is required.

#### Optional (for LoRa or Other Modules)
- Connect a LoRa module to the Arduino's SPI pins (e.g., MOSI, MISO, SCK, CS) and configure it in the firmware.
- Add additional sensors to available analog or digital pins as needed.

#### Power the Arduino
Use a USB cable or external power source (7-12V) to power the Arduino.

### Software Setup

#### Arduino Code
1. Open `MES_GAS_SENSOR_CODE.ino` in the Arduino IDE.
2. Upload the code to the Arduino UNO.

#### Bluetooth Configuration (Windows)
1. Go to Settings > Devices > Bluetooth & other devices.
2. Enable Bluetooth and click "Add Bluetooth or other device".
3. Pair the HC-05 module (default password: 1234).
4. Navigate to More Bluetooth options > COM Ports.
5. Note the COM port assigned to "HC-05 SerialPort" (e.g., COM5).
6. Update the `PORT` variable in `Monitoring.py` with the correct COM port.

#### Python Environment
1. Install Python 3.x if not already installed.
2. Install required libraries:
   ```bash
   pip install pyqt5 pyserial
   ```
3. Ensure `alert_sound.wav` is in the same directory as `Monitoring.py` for audio alerts.

#### Optional (for LoRa)
Install LoRa libraries for Arduino (e.g., RadioHead) and Python (e.g., pylora) if integrating a LoRa module.

#### Run the GUI
Execute `Monitoring.py`:
```bash
python Monitoring.py
```
The GUI will display connection status and alerts.

## Usage

1. **Power On**: Connect the Arduino to a power source. The system initializes and begins monitoring gas levels.

2. **Gas Detection**:
   - The MQ-2 sensor continuously reads gas levels.
   - If the sensor value exceeds 300, the system:
     - Activates the buzzer and inbuilt LED for 5 seconds.
     - Sends an alert ('1') via Bluetooth to the GUI.

3. **GUI Monitoring**:
   - The GUI displays "Attempting Connection..." during initialization.
   - Upon successful connection, it shows "Connected to GDAS...".
   - If a gas leak is detected, the GUI displays "Alert! Gas Leak Detected at GDAS - 1" and plays `alert_sound.wav`.
   - Use the Clear Console button to reset the console display.
   - Use the Quit button to terminate the program gracefully.

4. **Error Handling**:
   - If the Bluetooth connection fails, the GUI displays an error message and terminates.
   - Press Ctrl+C to manually exit the program.

5. **Extending with LoRa**:
   - Configure the LoRa module to transmit alerts to a remote receiver.
   - Update the Arduino code to send sensor data via LoRa instead of or in addition to Bluetooth.
   - Modify the Python script to receive and process LoRa messages.

## File Structure

- **`MES_GAS_SENSOR_CODE.ino`**: Arduino code for reading MQ-2 sensor data, controlling the buzzer and inbuilt LED, and sending alerts via Bluetooth.
- **`Monitoring.py`**: Python script for serial communication with the HC-05 module and GUI updates.
- **`GUI.py`**: Python script defining the PyQt5-based graphical interface for displaying alerts and connection status.
- **`alert_sound.wav`**: Audio file for gas leak alerts (ensure it is in the same directory as `Monitoring.py`).

## Code Explanation

### Arduino Code (`MES_GAS_SENSOR_CODE.ino`)

#### Setup
- Initializes pins for the inbuilt LED (pin 13) and buzzer (pin 6).
- Configures serial communication for debugging (Serial) and Bluetooth (BT) at 9600 baud.

#### Loop
- Reads analog values from the MQ-2 sensor (pin A0).
- If the sensor value exceeds 300, triggers the `send_alert()` function, activates the buzzer and inbuilt LED for 5 seconds, and then deactivates them.
- Delays 1 second between readings to avoid overwhelming the serial buffer.

#### send_alert
- Prints a warning to the Serial Monitor.
- Sends '1' via Bluetooth to signal a gas leak.

#### Extensibility
The code can be modified to support additional sensors or communication modules (e.g., LoRa) by adding new pin definitions and transmission logic.

### Python Monitoring Script (`Monitoring.py`)

#### SerialWorker Class
- A QThread for non-blocking serial communication.
- Attempts to connect to the HC-05 module via the specified COM port.
- Emits signals for GUI updates (data_received, styling) and audio alerts (play_sound_signal).
- Handles connection errors and ensures proper cleanup.

#### Animation
Displays a "connecting" animation (dots) until a connection is established or fails.

#### Audio
Plays `alert_sound.wav` when a gas leak is detected.

#### Extensibility
The script can be extended to handle LoRa or other communication protocols by adding new receiver logic and signal handlers.

### GUI Script (`GUI.py`)

#### Window Setup
- Creates a PyQt5 window with a fixed size (800x600) and a cyan background.
- Uses a QVBoxLayout to arrange widgets vertically.

#### Widgets
- **Title Label**: Displays "GDAS Activity Console" with bold styling.
- **Text Box**: A read-only QPlainTextEdit for showing connection status and alerts.
- **Clear Button**: Clears the console to a default message.
- **Quit Button**: Terminates the application (hidden until needed).

#### Styling
- Uses Cascadia Code font and custom colors for a modern, professional look.
- Includes hover and pressed effects for buttons and scrollbars.

#### Extensibility
The GUI can be enhanced with additional controls (e.g., threshold sliders, sensor selection dropdowns) or support for displaying data from multiple sources.

## Limitations

- **Bluetooth Range**: Limited by the HC-05 module (typically 10 meters); LoRa modules can overcome this for long-range needs.
- **Single Sensor**: Currently supports one MQ-2 sensor; multi-sensor setups require code modifications.
- **Audio Dependency**: Requires `alert_sound.wav` for audio alerts.
- **Platform**: Bluetooth setup instructions are Windows-specific; Linux/Mac users may need to adjust COM port configurations.

## Future Improvements

- **LoRa Integration**: Implement LoRa for long-range, low-power communication in remote areas.
- **Multi-Sensor Support**: Extend the system to handle multiple sensors (e.g., MQ-3, MQ-7) for broader gas detection.
- **Mobile App Integration**: Develop a mobile app to receive alerts via Bluetooth or LoRa.
- **Dynamic Thresholds**: Add GUI controls to adjust gas detection thresholds dynamically.
- **Data Logging**: Log sensor readings and alerts to a file or database for analysis.
- **Cross-Platform Bluetooth**: Provide setup instructions for Linux and macOS.

## Troubleshooting

### Bluetooth Connection Fails
- Verify the HC-05 is paired and the correct COM port is set in `Monitoring.py`.
- Ensure the HC-05 is powered and within range.

### No Alerts on GUI
- Check the Arduino Serial Monitor for sensor values and ensure they exceed the threshold (300).
- Confirm the baud rate (9600) matches in both Arduino and Python scripts.

### No Audio
- Ensure `alert_sound.wav` is in the same directory as `Monitoring.py`.
- Verify system audio is enabled.

### GUI Freezes
- Restart the Python script and ensure no other applications are using the COM port.

### LoRa Integration Issues
- Verify LoRa module connections and ensure compatible libraries are installed.
- Check frequency bands (e.g., 915 MHz for North America, 868 MHz for Europe) match the region.

## License

This project is licensed under the GNU GPL V3.0 License. See the LICENSE file for details.
