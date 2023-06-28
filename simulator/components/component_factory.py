from .led.led import Led
from .component import Component
from ..messages.setup_message import ComponentMessage


class ComponentFactory:
    @staticmethod
    def create_component(component: ComponentMessage) -> Component:
        if component.name == 'led':
            return Led(component.pin, component.x, component.y)