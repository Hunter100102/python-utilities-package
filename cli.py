import click
from utilities.file_utils import read_json, write_json, read_csv, write_csv
from utilities.api_utils import fetch_data
from rich import print

@click.group()
def cli():
    """Python Utilities CLI"""
    pass

@click.command()
@click.argument("url")
def get_api_data(url):
    """Fetch data from an API"""
    data = fetch_data(url)
    print(data)

@click.command()
@click.argument("json_file")
def read_json_file(json_file):
    """Read JSON file"""
    data = read_json(json_file)
    print(data)

@click.command()
@click.argument("csv_file")
def read_csv_file(csv_file):
    """Read CSV file"""
    data = read_csv(csv_file)
    print(data)

cli.add_command(get_api_data)
cli.add_command(read_json_file)
cli.add_command(read_csv_file)

if __name__ == "__main__":
    cli()
