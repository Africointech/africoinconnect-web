import ccxt



markets = ccxt.exchanges


data = ['binance','kucoin','bybit','coinbase','kraken']


binance = ccxt.binance()
kucoin = ccxt.kucoin()
bybit = ccxt.bybit();

market_binance = binance.load_markets()
# print(list(market_binance.items())[:1])
# print(len(market_binance.keys()))
symbole = [item for item in market_binance if item.endswith('USDT')]
# print(symbole)
dogeb = binance.fetch_ticker('DOGE/USDT')['last']
dogek = kucoin.fetch_ticker('DOGE/USDT')['last']
print(dogeb)
print(dogek)
