from json import loads, JSONDecodeError, dumps
from re import sub
from trades_registries.trade import Trade


class TradeJson:
    def __init__(self, path):
        self.path = path
        self.content = self.load()

    def load(self):
        with open(self.path, "r", encoding="utf8") as file:
            return file.read()

    def get_trade(self) -> Trade:
        return Trade(**self.get_json())

    def save(self):
        with open(self.path, "w", encoding="utf8") as file:
            file.write(self.content)

    def fix(self):
        self.content = sub(r"(\".*\": \".*\")\n\t\t\"", r'\g<1>,\n\t\t"', self.content)
        self.save()

    def get_json(self):
        try:
            json = loads(self.content)[0]
        except JSONDecodeError:
            self.fix()
            json = loads(self.content)[0]
        return json
