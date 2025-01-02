import time
import RPi.GPIO as GPIO
from typing import Callable, List
import heapq
from dataclasses import dataclass, field

# Определяем тип для callback-функций
Callback = Callable[[], None]

@dataclass(order=True)
class Task:
    scheduled: float  # Время выполнения задачи
    callback: Callback = field(compare=False)  # Функция, которая будет вызвана

class Scheduler:
    def __init__(self) -> None:
        self.tasks: List[Task] = []  # Очередь задач (хранится в виде кучи)
    
    def enter(self, after: float, callback: Callback) -> None:
        """
        Планирует выполнение задачи через заданное время.
        """
        scheduled_time = time.time() + after
        new_task = Task(scheduled_time, callback)
        heapq.heappush(self.tasks, new_task)
    
    def run(self) -> None:
        """
        Выполняет задачи в порядке их запланированного времени.
        """
        while self.tasks:
            now = time.time()
            next_task = heapq.heappop(self.tasks)
            delay = next_task.scheduled - now
            if delay > 0:
                time.sleep(delay)  # Ожидание до следующей задачи
            next_task.callback()  # Вызов callback

# Класс для управления LED
class LEDController:
    def __init__(self, pin: int) -> None:
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.HIGH)
    
    def turn_on(self) -> None:
        print("...LED ON")
        GPIO.output(self.pin, GPIO.LOW)
    
    def turn_off(self) -> None:
        print("LED OFF...")
        GPIO.output(self.pin, GPIO.HIGH)
    
    def cleanup(self) -> None:
        GPIO.output(self.pin, GPIO.HIGH)
        GPIO.cleanup()

# Основной код
if __name__ == "__main__":
    LedPin = 17
    led = LEDController(LedPin)
    scheduler = Scheduler()

    try:
        # Запланировать включение и выключение LED
        while True:
            scheduler.enter(0, led.turn_on)  # Включить LED
            scheduler.enter(0.5, led.turn_off)  # Выключить LED
            scheduler.run()
    except KeyboardInterrupt:
        print("Завершение работы...")
        led.cleanup()
