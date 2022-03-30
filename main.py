from modules.esp8266 import ESP8266
from consts import NetworkConsts


def main():
    esp8266 = ESP8266(NetworkConsts.WIFI_SSID, NetworkConsts.WIFI_PASSWORD)

    esp8266.startup()

    if esp8266.check_module():
        print("Module UP")

        esp8266.connect_to_network()

        if esp8266.check_connection():
            print("Connected To WiFi Network")

            if esp8266.check_connection_with_host(NetworkConsts.API_IP):
                print("Sending detection data")

                esp8266.send_post('{"auth_token": "test_auth_token", "sensor": "test sensor"}',
                                  NetworkConsts.API_IP, NetworkConsts.API_PORT)


if __name__ == '__main__':
    main()
