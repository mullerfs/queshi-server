from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import AssetSchema
from .service import AssetService
from .model import Asset
from .interface import AssetInterface

api = Namespace("Asset", description="Manage Asset Information")  


@api.route("/")
class AssetResource(Resource):
    """Assets"""

    @responds(schema=AssetSchema(many=True))
    def get(self) -> List[Asset]:
        """Get all Assets"""

        return AssetService.get_all()

    @accepts(schema=AssetSchema, api=api)
    @responds(schema=AssetSchema)
    def post(self) -> Asset:
        """Create a Single Asset"""

        return AssetService.create(request.parsed_obj)


@api.route("/<int:assetId>")
@api.param("assetId", "Asset ID")
class AssetIdResource(Resource):
    @responds(schema=AssetSchema)
    def get(self, assetId: int) -> Asset:
        """Get Single Asset"""

        return AssetService.get_by_id(assetId)

    def delete(self, assetId: int) -> Response:
        """Delete Single Asset"""
        from flask import jsonify

        id = AssetService.delete_by_id(assetId)
        return jsonify(dict(status="Success", id=id))

    @accepts(schema=AssetSchema, api=api)
    @responds(schema=AssetSchema)
    def put(self, assetId: int) -> Asset:
        """Update Single Asset"""

        changes: AssetInterface = request.parsed_obj
        Asset = AssetService.get_by_id(assetId)
        return AssetService.update(Asset, changes)