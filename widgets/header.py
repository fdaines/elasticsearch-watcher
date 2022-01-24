from rich import box
from rich.align import Align
from rich.console import Group
from rich.panel import Panel
from rich.table import Table

from config import get_elasticsearch_url
from client.elasticsearch import get_plain_response

def display_information_widget() -> Table:
    nodes_panel = Panel(
      Align.center(
          Group(Align.center("Current Elasticsearch cluster: [bold green]" + get_elasticsearch_url() + "[/]"), Align.center(get_health_table())),
          vertical="top",
      ),
      box=box.ROUNDED,
      padding=(1, 2),
      title="[bold]ElasticSearch Cluster Watcher[/]",
      border_style="bright_green",
    )
    return nodes_panel

def get_health_table() -> Table:
    response = get_plain_response('_cat/health?v')
    lines = response.splitlines()

    table = Table(show_footer=False)
    column_names = lines[0].split()
    for c in column_names:
        table.add_column(c, no_wrap=True)

    healthData = lines[1].split()
    table.add_row(healthData[0],
    healthData[1],
    healthData[2],
    prettyStatus(healthData[3]),
        healthData[4],
        healthData[5],
        healthData[6],
        healthData[7],
        healthData[8],
        healthData[9],
        healthData[10],
        healthData[11],
        healthData[12],
        healthData[13],
    )

    return table

def get_health_info() -> Table:
    table = get_health_table()

    nodes_panel = Panel(
      Align.center(
          Align.center(table),
          vertical="top",
      ),
      box=box.ROUNDED,
      padding=(1, 2),
      title="[bold]Health Information[/]",
      border_style="bright_cyan",
    )
    return nodes_panel


def prettyStatus(status):
    if status == 'green':
        return "[bold green]"+status+"[/]"

    if status == 'yellow':
        return "[bold yellow]"+status+"[/]"

    return "[bold magenta]"+status+"[/]"
