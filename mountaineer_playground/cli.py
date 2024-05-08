from click import command, option
from mountaineer.cli import handle_runserver, handle_watch, handle_build
from mountaineer.database.cli import handle_createdb
from mountaineer.io import async_to_sync

from mountaineer_playground import models
from mountaineer_playground.config import AppConfig


@command()
@option("--port", default=5006, help="Port to run the server on")
def runserver(port: int):
    handle_runserver(
        package="mountaineer_playground",
        webservice="mountaineer_playground.main:app",
        webcontroller="mountaineer_playground.app:controller",
        port=port,
    )


@command()
def watch():
    handle_watch(
        package="mountaineer_playground",
        webcontroller="mountaineer_playground.app:controller",
    )


@command()
def build():
    handle_build(
        webcontroller="mountaineer_playground.app:controller",
    )


@command()
@async_to_sync
async def createdb():
    _ = AppConfig() # type: ignore

    await handle_createdb(models)