from consts import ESP8266Consts
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

    def connect_to_network(self, ssid, password):
        uart_utils.send_cmd(self.uart, "AT+CWQAP", "OK")
        uart_utils.send_cmd(self.uart, f'AT+CWJAP="{ssid}","{password}"', "OK")
        uart_utils.send_cmd(self.uart, "AT+CWMODE=1", "OK")
        uart_utils.send_cmd(self.uart, "AT+CIPMODE=0", "OK")

    def check_connection(self):
        return uart_utils.send_cmd(self.uart, "AT+CIFSR", "OK")

    def check_connection_with_host(self, host_ip):
        return uart_utils.send_cmd(self.uart, f'AT+PING="{host_ip}"', "OK")

    def send_post(self, payload, destination_ip, destination_port):
        connected = uart_utils.send_cmd(self.uart, f'AT+CIPSTART="TCP","{destination_ip}",{destination_port}', "OK")

        if connected:
            post_data = f"POST /api/notify HTTP/1.1\r\nHost: {destination_ip}\r\nContent-Type: application/json\r\nContent-Length: {str(len(payload))}\r\n\r\n{payload}\r\n"

            uart_utils.send_cmd(self.uart, f"AT+CIPSEND={str(len(post_data))}", ">")
            uart_utils.send_cmd(self.uart, post_data, "OK")
