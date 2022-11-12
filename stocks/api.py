import yfinance as yf


def yf_with_params(tickers: list[str], period: str, interval: str = "1d"):

    output = yf.download(
        tickers=",".join(tickers),
        period=period,
        interval=interval,
        group_by="ticker",
        prepost=False
    )

    return output