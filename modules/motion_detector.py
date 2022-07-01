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

        self.debug_mode = False

    def print_debug(self, message):
        if self.debug_mode:
            print(message)

    def init_wifi_connection(self):
        self.print_debug("Starting ESP8266...")

        if self.esp8266.check_module():
            self.print_debug("Connecting to network...")
            self.esp8266.connect_to_network(NetworkConsts.WIFI_SSID, NetworkConsts.WIFI_PASSWORD)

        else:
            self.print_debug("ESP8266 Startup...")
            self.esp8266.startup()

    def start_detector(self):
        self.print_debug("Starting Detector...")

        self.esp8266.startup()
        self.init_wifi_connection()

        self.mainloop()

    def mainloop(self):
        self.print_debug("Started Detector...")

        while True:
            if self.motion_sensor.value():
                self.print_debug("Movement detected...")

                if self.esp8266.check_connection():
                    self.print_debug("Connected with network...")

                    if self.esp8266.check_connection_with_host(NetworkConsts.API_IP):
                        self.print_debug("Connected with target API...")

                        self.esp8266.send_post(
                            '{"auth_token": "' + DetectorConsts.API_AUTH_TOKEN + '", "sensor": "' + DetectorConsts.DETECTOR_NAME + '"}',
                            NetworkConsts.API_IP, DetectorConsts.API_ENDPOINT_PATH, NetworkConsts.API_PORT)

                        self.print_debug("Sent payload...")

                else:
                    self.init_wifi_connection()

            time.sleep(DetectorConsts.UPDATE_RATE)
