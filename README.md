### PicoMotionDetector

Raspberry Pi Pico powered motion detector integrated with [MotionDetectionAPI](https://github.com/TheZodiaCC/MotionDetectionAPI)

---

#### Parts
- 1x Raspberry Pi Pico
- 1x PIR HC-SR501
- 1x Circuit board
- 2x 100 uF capacitors
- 1x USB-C connector
- 1x L7805ABV 5V voltage regulator
- 1x ESP8266 (ESP-12E)
- Some gold pin connectors
- Some connecting wires

##### For better detection results (less false positives) 
Use 100 uF capacitor connected in parallel between VCC and GND of PIR sensor.
Additionally if input voltage is below 7V (L78 voltage dropout is 2V), power circuit using 5V power supply not using voltage stabilizer.

#### Setup
1. Set WiFi network and [MotionDetectionAPI](https://github.com/TheZodiaCC/MotionDetectionAPI) details in `consts.py`/`NetworkConsts` and `consts.py`/`DetectorConsts`
2. If needed tweak `ESP8266Consts` and / or `DetectorConsts` for PIN ids.

#### Media

