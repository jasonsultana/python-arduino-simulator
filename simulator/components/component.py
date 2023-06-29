from abc import abstractmethod


class Component:
    pin: int
    
    @abstractmethod
    def digital_read(self) -> int:
        ...

    @abstractmethod
    def digital_write(self, pin: int, value: int):
        ...