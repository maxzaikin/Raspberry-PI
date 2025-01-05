""" 
Project: Smart-House

Author: Maks V. Zaikin
Date: 06-Jan-2025
"""

import RPi.GPIO as GPIO
import time

class ADCReader:
    """ _summary_

    _extended_summary_
    """
    def __init__(self, cs_pin=17, clk_pin=18, dio_pin=27, channel=0):
        self.cs_pin = cs_pin
        self.clk_pin = clk_pin
        self.dio_pin = dio_pin
        self.channel = channel
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.cs_pin, GPIO.OUT)
        GPIO.setup(self.clk_pin, GPIO.OUT)
        GPIO.setup(self.dio_pin, GPIO.OUT)
        self.setup()

    def setup(self):
        
        GPIO.output(self.cs_pin, 1)

    def cleanup(self):
        
        GPIO.cleanup()

    def read(self):
       
        GPIO.output(self.cs_pin, 0)

        sel = int(self.channel > 1 & 1)
        odd = self.channel & 1

        
        GPIO.output(self.clk_pin, 0)
        GPIO.output(self.dio_pin, 1)
        time.sleep(0.000002)
        GPIO.output(self.clk_pin, 1)
        time.sleep(0.000002)

        # Режим Single End
        GPIO.output(self.clk_pin, 0)
        GPIO.output(self.dio_pin, 1)
        time.sleep(0.000002)
        GPIO.output(self.clk_pin, 1)
        time.sleep(0.000002)

        # Выбор канала
        GPIO.output(self.clk_pin, 0)
        GPIO.output(self.dio_pin, odd)
        time.sleep(0.000002)
        GPIO.output(self.clk_pin, 1)
        time.sleep(0.000002)
        GPIO.output(self.clk_pin, 0)
        GPIO.output(self.dio_pin, sel)
        time.sleep(0.000002)
        GPIO.output(self.clk_pin, 1)

        # Чтение данных
        dat1 = 0
        GPIO.setup(self.dio_pin, GPIO.IN)
        for _ in range(8):
            GPIO.output(self.clk_pin, 1)
            time.sleep(0.000002)
            GPIO.output(self.clk_pin, 0)
            time.sleep(0.000002)
            dat1 = (dat1 << 1) | GPIO.input(self.dio_pin)

        GPIO.output(self.cs_pin, 1)
        GPIO.setup(self.dio_pin, GPIO.OUT)
        return dat1
