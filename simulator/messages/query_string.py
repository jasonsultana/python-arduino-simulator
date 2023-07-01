class QueryString:
    @staticmethod
    def find(qs: str, param: str) -> str:
        parts = qs.split('&')

        for part in parts:
            if part.find(param) > -1:
                return part.replace(f"{param}=", "")
            
        return None
    
    @staticmethod
    def builder():
        return QueryStringBuilder()

class QueryStringBuilder:
    def __init__(self):
        self.__qs = None

    def add(self, param, value):
        if self.__qs is None:
            self.__qs = f"{param}={value}"
        else:
            self.__qs += f"&{param}={value}"

        return self
    
    def build(self):
        return self.__qs