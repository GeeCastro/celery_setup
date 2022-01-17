import json


class Service:
    def __init__(self, att1: int) -> None:
        self.att1 = att1

    def multiply_by(self, multiplicand: int) -> int:
        return self.att1 * multiplicand

    def __json__(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    @staticmethod
    def load_json(json_string: str):
        deserialised = json.loads(json_string)
        return Service(att1=deserialised["att1"])
