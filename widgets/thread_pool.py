from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from services.thread_pool import get_thread_pool_information

def generate_thread_pool_table() -> Table:
    info = get_thread_pool_information()

    table = Table(show_footer=False)
    table_centered = Align.center(table)
    table.add_column("Node name", no_wrap=True)
    table.add_column("Thread name", no_wrap=True)
    table.add_column("Active", no_wrap=True, justify="right")
    table.add_column("Queue", no_wrap=True, justify="right")
    table.add_column("Rejected", no_wrap=True, justify="right")

    for n in info:
        table.add_row(*n)

    return table

def generate_thread_pool_widget() -> Panel:
    table = generate_thread_pool_table()

    nodes_panel = Panel(
        Align.center(
            Align.center(table),
            vertical="top",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[bold]Thread Pool[/]",
        border_style="bright_blue",
    )
    return nodes_panel
