from machine import Pin
from modules.esp8266 import ESP8266
from consts import NetworkConsts, DetectorConsts
import time


class MotionDetector:
    def __init__(self):
        self.onboard_led = Pin(25, Pin.OUT)
        self.motion_sensor = Pin(DetectorConsts.SENSOR_PIN_ID, Pin.IN, Pin.PULL_DOWN)

        self.esp8266 = ESP8266()

        self.onboard_led.on()

    def init_wifi_connection(self):
        if self.esp8266.check_module():
            self.esp8266.connect_to_network(NetworkConsts.WIFI_SSID, NetworkConsts.WIFI_PASSWORD)

        else:
            self.esp8266.startup()

    def start_detector(self):
        self.esp8266.startup()
        self.init_wifi_connection()

        self.mainloop()

    def mainloop(self):
        while True:
            if self.motion_sensor.value():
                if self.esp8266.check_connection():
                    if self.esp8266.check_connection_with_host(NetworkConsts.API_IP):
                        self.esp8266.send_post(
                            '{"auth_token": "' + DetectorConsts.API_AUTH_TOKEN + '", "sensor": "' + DetectorConsts.DETECTOR_NAME + '"}',
                            NetworkConsts.API_IP, DetectorConsts.API_ENDPOINT_PATH, NetworkConsts.API_PORT)

                else:
                    self.init_wifi_connection()

            time.sleep(DetectorConsts.UPDATE_RATE)
