import uvicorn

from typer import Typer

cli = Typer()


@cli.command()
def runserver():
    uvicorn.run("app.app:app", reload=True)


if __name__ == '__main__':
    cli()
