import utime


def send_cmd(uart, cmd, ack, timeout=5000):
    status = False
    current_time = utime.ticks_ms()

    uart.write(f"{cmd}\r\n")

    while (utime.ticks_ms() - current_time) < timeout:
        uart_data = uart.read()

        if uart_data is not None:
            # print(uart_data)

            try:
                if ack in uart_data.decode():
                    status = True

                    break
            except:
                pass

    return status
