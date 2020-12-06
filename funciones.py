def btc_price():
    import requests
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur")
    return(r.json()["bitcoin"]["eur"])

def get_btc_historical_data():
    import requests
    import pandas as pd
    from datetime import datetime
    from matplotlib import pyplot
    import seaborn as sns

    # Btc/ Eur price
    r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur")
    price_today = r.json()["bitcoin"]["eur"]


    # historical data

    historical_data_request = requests.get(
        "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart/range?vs_currency=eur&from=1199145600&to=1606780800")
    historical = historical_data_request.json()
    historical_price = historical_data_request.json()["prices"]
    btc_price_dt = pd.DataFrame(historical_price, columns=["time", "price"])
    btc_price_dt["time"] = btc_price_dt["time"].apply(lambda x: x / 1000)
    btc_price_dt["time"] = pd.to_datetime(btc_price_dt["time"], unit="s")

    # mergear market cap y volumen
    historical_market_caps = historical_data_request.json()["market_caps"]
    btc_market_cap_dt = pd.DataFrame(historical_market_caps, columns=["time", "market_cap"])
    btc_market_cap_dt["time"] = btc_market_cap_dt["time"].apply(lambda x: x / 1000)
    btc_market_cap_dt["time"] = pd.to_datetime(btc_market_cap_dt["time"], unit="s")
    btc_historical_data = pd.merge(btc_price_dt, btc_market_cap_dt, how="left", on="time")
    historical_market_volume = historical_data_request.json()["total_volumes"]
    historical_market_volume = pd.DataFrame(historical_market_volume, columns=["time", "volume"])
    historical_market_volume["time"] = historical_market_volume["time"].apply(lambda x: x / 1000)
    historical_market_volume["time"] = pd.to_datetime(historical_market_volume["time"], unit="s")
    btc_historical_data = pd.merge(btc_historical_data, historical_market_volume, how="left", on="time")

    # Representacion:
    btc_historical_data.set_index("time")
    return (btc_historical_data)

def btc_timeserie():
    import requests
    import pandas as pd
    from datetime import datetime
    from matplotlib import pyplot
    import seaborn as sns

    data = get_btc_historical_data()

    price_timeserie = sns.lineplot(x="time", y="price",
                 data=data)
    return(price_timeserie)