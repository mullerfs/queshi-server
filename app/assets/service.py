from app import db
from typing import List
from .model import Asset
from .interface import AssetInterface


class AssetService:
    @staticmethod
    def get_all() -> List[Asset]:
        return Asset.query.all()

    @staticmethod
    def get_by_id(asset_id: int) -> Asset:
        return Asset.query.get(asset_id)

    @staticmethod
    def update(asset: Asset, Asset_change_updates: AssetInterface) -> Asset:
        asset.update(Asset_change_updates)
        db.session.commit()
        return asset

    @staticmethod
    def delete_by_id(asset_id: int) -> List[int]:
        asset = Asset.query.filter(Asset.asset_id == asset_id).first()
        if not asset:
            return []
        db.session.delete(asset)
        db.session.commit()
        return [asset_id]

    @staticmethod
    def create(new_attrs: AssetInterface) -> Asset:
        print(new_attrs)
        new_asset = Asset(new_attrs)
        new_asset.create()
        return new_asset