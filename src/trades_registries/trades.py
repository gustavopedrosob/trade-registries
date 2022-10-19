from trades_registries.trade_json import TradeJson
from trades_registries.trade import Trade
from pathlib import Path
from os import listdir


class Trades:
    def __init__(self, trades: list[Trade]):
        self.trades = trades

    @staticmethod
    def from_trade_folder(path: str = str(Path.home()) + "\\AppData\\Roaming\\bakkesmod\\bakkesmod\\data\\TradeLogger\\"):
        files = filter(lambda name: name.endswith(".json"), listdir(path))
        return Trades([TradeJson(path + file).get_trade() for file in files])
