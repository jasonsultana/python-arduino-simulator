class PyMata:
    INPUT = 0
    OUTPUT = 1
    
    ANALOG = 0
    DIGITAL = 1

    def __init__(self, simulator_url, verbose: bool):
        self.url = simulator_url
        self.verbose = verbose

    def set_pin_mode(self, pin, pin_mode, signal_type):
        # todo
        pass

    def digital_write(self, pin, value):
        # todo
        pass

    def close(self):
        # todo
        pass