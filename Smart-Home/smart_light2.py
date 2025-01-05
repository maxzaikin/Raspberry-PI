import time
import RPi.GPIO as GPIO
from typing import Callable, List
import heapq
from dataclasses import dataclass, field
import datetime
from __future__ import annotations

# Определяем тип для callback-функций
Callback = Callable[[], None]

@dataclass(order=True)
class Task:
    scheduled: float  # Время выполнения задачи
    callback: Callback = field(compare=False)  # Функция, которая будет вызвана

class Scheduler:
    """ 
    the Scheduler class is a heap queue, a List of Task objects kept in a specific order.
    """
    def __init__(self) -> None:
        self.tasks: List[Task] = []  # Очередь задач (хранится в виде кучи)

    def enter(self, after: float, callback: Callback) -> None:
        """
        enter method to add a new task to the queue.
 
        Arguments:
            after -- delay parameter representing the interval to wait before executing the callback task,
            callback -- a function to be executed at the correct time.
        """
        # TODO: Add validation checks for negative values and implement appropriate exceptions.
        #       Consider __post__init() for prevent dummy error cases
        scheduled_time = time.time() + after
        new_task = Task(scheduled_time, callback)
        heapq.heappush(self.tasks, new_task)

    def __call__(self) -> None:
        """
        The run() method removes items from the queue in order by the time they're
        supposed to be performed. If we're at (or past) the required time, then the value
        computed for delay will be zero or negative, and we don't need to wait; we can
        perform the callback immediately. If we're before the required time, then we need
        to sleep until the time arrives.
        
        it's essential to create an instance of a Scheduler class; it's the object that's callable, not the class.
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

    def format_msg(self, message: str) -> None:
        now = datetime.datetime.now()
        print(f"{now:%I:%M:%S}: {message}")

    def turn_on(self) -> None:
        self.format_msg('...LED ON')
        GPIO.output(self.pin, GPIO.LOW)

    def turn_off(self) -> None:
        print("LED OFF...")
        GPIO.output(self.pin, GPIO.HIGH)

    def cleanup(self) -> None:
        GPIO.output(self.pin, GPIO.HIGH)
        GPIO.cleanup()


#BUTTON_PIN = 18

#def button_pressed(channel: int) -> None:
#    """
#    Обработчик нажатия кнопки: добавляет задачи включения и выключения LED.
#    """
#    print("Кнопка нажата! Добавление событий в планировщик.")
#    current_time = time.time()
#    scheduler.enter(current_time + 1, led.turn_on)  # Включить через 1 секунду
#    scheduler.enter(current_time + 2, led.turn_off)  # Выключить через 2 секунды


if __name__ == "__main__":
    led_pin = 17
    led = LEDController(led_pin)
    scheduler = Scheduler()

    try:
        # Запланировать включение и выключение LED
        while True:
            scheduler.enter(0, led.turn_on)  # Включить LED
            scheduler.enter(0.5, led.turn_off)  # Выключить LED
            scheduler()
    except KeyboardInterrupt:
        print("Завершение работы...")
        led.cleanup()
