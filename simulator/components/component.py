from abc import abstractmethod


class Component:
    pin: int
    
    @abstractmethod
    def digital_read() -> int:
        ...

    @abstractmethod
    def digital_write(pin: int, value: int):
        ...