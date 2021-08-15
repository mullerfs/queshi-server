def register_routes(api, app, root="api"):
    from app.assets import register_routes as attach_assets
    
    # Add routes
    attach_assets(api, app, root)