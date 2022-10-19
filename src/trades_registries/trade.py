from dataclasses import dataclass, field
from datetime import datetime, time


@dataclass
class Trade:
    LocalPlayer: str = field(repr=False)
    LocalProducts: list
    LocalInstances: list = field(repr=False)
    LocalCurrencyId: int = field(repr=False)
    LocalCurrencyAmount: int
    RemotePlayer: str = field(repr=False)
    RemoteProducts: list
    RemoteInstances: list = field(repr=False)
    RemoteCurrencyId: int = field(repr=False)
    RemoteCurrencyAmount: int
    TradeGuid: str = field(repr=False)
    TradeGuidFormat: str = field(repr=False)
    TradeStartEpoch: str = field(repr=False)
    TradeEndEpoch: str = field(repr=False)

    def him_items(self):
        return self.RemoteProducts

    def my_items(self):
        return self.LocalProducts

    def my_credits(self):
        return self.LocalCurrencyAmount

    def him_credits(self):
        return self.RemoteCurrencyAmount

    def is_buy(self):
        return self.my_credits() > 0

    def is_sell(self):
        return self.him_credits() > 0

    def trade_start(self):
        return datetime.fromtimestamp(int(self.TradeStartEpoch))

    def trade_end(self):
        return datetime.fromtimestamp(int(self.TradeEndEpoch))

