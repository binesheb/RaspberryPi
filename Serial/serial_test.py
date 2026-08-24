"""
Simple Raspberry Pi UART send/receive example.

Defaults to the primary serial alias exposed by current Raspberry Pi OS. Adjust
`PORT` and serial parameters for the connected device.
"""

import time

import serial

PORT = "/dev/serial0"
BAUDRATE = 9600


def main():
    print("Starting program")

    try:
        with serial.Serial(
            PORT,
            baudrate=BAUDRATE,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1,
        ) as ser:
            time.sleep(1)
            ser.write(b"Hello World\r\n")
            ser.write(b"Serial Communication Using Raspberry Pi\r\n")
            ser.write(b"By: Embedded Laboratory\r\n")
            print("Data Echo Mode Enabled")

            while True:
                data = ser.read(1)
                if data:
                    print(data.decode(errors="replace"), end="", flush=True)
    except KeyboardInterrupt:
        print("\nExiting Program")
    except serial.SerialException as exc:
        print(f"Serial error: {exc}")


if __name__ == "__main__":
    main()
