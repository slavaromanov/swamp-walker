import time
from abc import ABC
from types import FunctionType
from datetime import timedelta
from enum import Enum
from time import sleep


second = 1


class ToadState(Enum):
    Live = 'LIVE'
    NeedForHelp = 'NFH'


class Condition(ABC):
    pass


class Timer(ABC):
    name: str
    time_to_next: timedelta

    def condition(self) -> bool:
        pass

    # TODO: return None?
    def do(self) -> None:
        pass

    # TODO: return None?
    def __listen(self) -> None:
        pass


class ToadInfo(object):
    wallet: int
    state: ToadState
    happines: int
    # eat_timer: Timer
    # dungeon_timer: Timer
    # work_timer: Timer
    # clan_regards_timer: Timer
    # marriage_regards_timer: Timer


class Eat(Timer):
    def __init__(self, time_to_next: timedelta):
        self.name = 'EAT'
        self.time_to_next = time_to_next
        self.__listen()

    def __listen(self) -> None:
        while True:
            if self.condition():
                self.do()
            time.sleep(second)

    def condition(self) -> bool:
        return self.time_to_next.seconds == 0

    def do(self) -> None:
        return

