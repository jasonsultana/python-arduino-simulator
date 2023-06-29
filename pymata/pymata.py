from simulator.messages.command_message import CommandMessage
import zmq
import json

class PyMata:
    INPUT = 0
    OUTPUT = 1
    
    ANALOG = 0
    DIGITAL = 1

    TONE_TONE = 0
    TONE_NO_TONE = 1

    def __init__(self, simulator_url, verbose: bool):
        self.url = simulator_url
        self.verbose = verbose

        context = zmq.Context()

        self.socket = context.socket(zmq.REQ)
        self.socket.connect(simulator_url)

    def reset(self):
        # do nothing
        pass

    def play_tone(self, pin, tone_command, frequency, duration):
        message = CommandMessage.create(pin, 'play_tone', f"cmd={tone_command}&frequency={frequency}&duration={duration}")
        self.__send_message(message)

    def set_pin_mode(self, pin, pin_mode, signal_type):
        message = CommandMessage.create(pin, 'pin_mode', pin_mode)
        self.__send_message(message)

    def digital_write(self, pin, value):
        message = CommandMessage.create(pin, 'digital_write', value)
        self.__send_message(message)

    def close(self):
        message = CommandMessage.create(pin=0, command_text='close', command_value=0)
        self.__send_message(message)

    def __send_message(self, message: CommandMessage):
        message_json = json.dumps(message)
        self.socket.send_string(message_json)
        self.socket.recv()
