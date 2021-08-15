from mypy_extensions import TypedDict


class AssetInterface(TypedDict, total=False):
    id : int 
    operation : str
    ticker : str
    ticker_type : str
    strategy: str
    amount: float
    entry_price : float
    entry_date : str
    currency: str
    exchange: str
    house: str