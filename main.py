from trades_registries.trades import Trades
from json import dump

trades = Trades.from_trade_folder()
new_dict = [trade.__dict__ for trade in trades.trades]

with open('sample_trade.json', 'w') as file:
    dump(new_dict, file)
