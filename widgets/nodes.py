from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from services.nodes import get_nodes_information
from config import nodesConfig

def make_nodes_information_widget() -> Panel:
    table = generate_table()

    nodes_panel = Panel(
        Align.center(
            Align.center(table),
            vertical="top",
        ),
        box=box.ROUNDED,
        padding=(1, 1),
        title="[bold]Elasticsearch Nodes Information[/]",
        border_style="bright_blue",
    )
    return nodes_panel

def generate_table() -> Table:
    nodes_list = get_nodes_information()

    table = Table(show_footer=False)
    table_centered = Align.center(table)
    table.add_column("Node name", no_wrap=True)
    table.add_column("Heap", no_wrap=True)
    table.add_column("RAM", no_wrap=True)
    table.add_column("CPU", no_wrap=True)
    table.add_column("L.1m", no_wrap=True)
    table.add_column("L.5m", no_wrap=True)
    table.add_column("L.15m", no_wrap=True)

    NODES_DATA = []
    for n in nodes_list:
        NODES_DATA.append(to_data_table(n))
    for n in NODES_DATA:
        table.add_row(*n)

    return table

def to_data_table(node):
    return [
        node.name,
        format_value(node.heap, nodesConfig["heap_limit"]),
        format_value(node.ram, nodesConfig["ram_limit"]),
        format_value(node.cpu, nodesConfig["cpu_limit"]),
        format_value(node.load1, nodesConfig["loads_limit"]),
        format_value(node.load5, nodesConfig["loads_limit"]),
        format_value(node.load15, nodesConfig["loads_limit"]),
    ]

def format_value(value, limit):
    if value <= limit:
        return str(value)
    return "[bold magenta]"+str(value)+"[/]"
