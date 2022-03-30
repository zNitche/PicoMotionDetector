from consts import NetworkConsts, ESP8266Consts
import uart_utils
import time
from machine import UART, Pin


class ESP8266:
    def __init__(self):
        self.state_pin = Pin(ESP8266Consts.STATE_PIN_ID, Pin.OUT)
        self.reset_pin = Pin(ESP8266Consts.RESET_PIN_ID, Pin.OUT)

        self.uart = UART(ESP8266Consts.UART_ID, ESP8266Consts.UART_BAUDRATE)

    def startup(self):
        self.state_pin.on()

        self.reset_pin.off()

        time.sleep(2)
        self.reset_pin.on()

    def check_module(self):
        return uart_utils.send_cmd(self.uart, "AT", "ready")

    def connect_to_network(self):
        uart_utils.send_cmd(self.uart, "AT+CWQAP", "OK")
        uart_utils.send_cmd(self.uart, f'AT+CWJAP="{NetworkConsts.WIFI_SSID}","{NetworkConsts.WIFI_PASSWORD}"', "OK")
        uart_utils.send_cmd(self.uart, "AT+CWMODE=1", "OK")
        uart_utils.send_cmd(self.uart, "AT+CIPMODE=0", "OK")

    def check_connection(self):
        return uart_utils.send_cmd(self.uart, f'AT+PING="{NetworkConsts.API_IP}"', "OK")

    def send_post(self):
        pass
