""" 
Project: Smart-House

Author: Maks V. Zaikin
Date: 06-Jan-2025
"""
import sys
import time
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from core.light import SmartLight
from core.adc0834 import ADCReader
from core.smart_home import SmartHome

class LightObserver:
    def __init__(self, light, adc_reader):
        self.light = light
        self.adc_reader = adc_reader

    def update(self):
        """Обновляет состояние света в зависимости от значения ADC."""
        analog_value = self.adc_reader.read()
        print(f"Analog value: {255 - analog_value}")
        self.light.update_light_state(analog_value)

if __name__ == '__main__':
    try:
        # Создаем устройства
        light = SmartLight(pin=22)
        adc_reader = ADCReader(channel=0)

        # Создаем систему умного дома
        smart_home = SmartHome()

        # Добавляем наблюдателя
        light_observer = LightObserver(light, adc_reader)
        smart_home.add_device(light_observer)

        # Основной цикл
        while True:
            smart_home.update_devices()
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("Stopping program...")
        adc_reader.cleanup()
        light.cleanup()