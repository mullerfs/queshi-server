import os
import click
from dotenv import load_dotenv
load_dotenv()

from app import create_app, db


env = os.getenv("FLASK_ENV") or "dev"
print(f"Active environment: * {env} *")
app = create_app(env)


app.app_context().push()


@app.cli.command("run")
def run():
    app.run()

@app.cli.command("init_db")
def init_db():
    print("Creating all resources.")
    db.create_all()

@app.cli.command("drop_all")
def drop_all():
    if input("Are you sure you want to drop all tables? (y/N)\n").lower() == "y":
        print("Dropping tables...")
        db.drop_all()


if __name__ == "__main__":
    app.cli()