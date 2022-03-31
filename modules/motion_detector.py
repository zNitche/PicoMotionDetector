from machine import Pin
from modules.esp8266 import ESP8266
from consts import NetworkConsts, DetectorConsts
import time


class MotionDetector:
    def __init__(self):
        self.onboard_pin = Pin(25, Pin.OUT)

        self.esp8266 = ESP8266()

        self.onboard_pin.on()

    def init_wifi_connection(self):
        self.esp8266.startup()

        if self.esp8266.check_module():
            self.esp8266.connect_to_network(NetworkConsts.WIFI_SSID, NetworkConsts.WIFI_PASSWORD)

    def start_detector(self):
        self.init_wifi_connection()

        self.mainloop()

    def mainloop(self):
        while True:
            if self.esp8266.check_connection():
                self.esp8266.send_post('{"auth_token": "test_auth_token", "sensor": "test sensor"}',
                                      NetworkConsts.API_IP, NetworkConsts.API_PORT)

            time.sleep(DetectorConsts.UPDATE_RATE)
