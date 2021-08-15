from .model import Asset  # noqa
from .schema import AssetSchema  # noqa

BASE_ROUTE = "assets"


def register_routes(api, app, root="api"):
    from .controller import api as asset_api

    api.add_namespace(asset_api, path=f"/{root}/{BASE_ROUTE}")