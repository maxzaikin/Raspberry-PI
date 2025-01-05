""" 
Project: Smart-House

Author: Maks V. Zaikin
Date: 06-Jan-2025
"""

import RPi.GPIO as GPIO

class SmartLight:
    """ _summary_

    _extended_summary_
    """

    def __init__(self, pin):
        self.pin= pin
        self.led_val= None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)
        self.led_val= GPIO.PWM(self.pin, 2000)
        self.led_val.start(0)

    def set_brightness(self, value):
        """set_brightness _summary_

        _extended_summary_

        Arguments:
            value -- _description_
        """

        if value > 250:
            duty_cycle= value * 100 /255
        else:
            duty_cycle= 0

        self.led_val.ChangeDutyCycle(duty_cycle)

    def cleanup(self):
        """cleanup _summary_

        _extended_summary_
        """

        self.led_val.stop()
        GPIO.cleanup()