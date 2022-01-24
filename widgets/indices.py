from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from services.indices import get_indices_with_cache
from utils import convert_to_human_with_limits


REQUEST_CACHE_LIMIT = 200*1024*1024
QUERY_CACHE_LIMIT = 200*1024*1024

def get_indices_with_cache_widget() -> Table:
    indices = get_indices_with_cache()

    table = Table()
    table.add_column("Index", no_wrap=True)
    table.add_column("Request Cache", no_wrap=True, justify="right")
    table.add_column("Query Cache", no_wrap=True, justify="right")

    for i in indices:
        table.add_row(i.name,
            convert_to_human_with_limits(i.request_cache, REQUEST_CACHE_LIMIT),
            convert_to_human_with_limits(i.query_cache, QUERY_CACHE_LIMIT))

    nodes_panel = Panel(
      Align.center(
          Align.center(table),
          vertical="top",
      ),
      box=box.ROUNDED,
      padding=(1, 2),
      title="[bold]Indices that uses Cache[/]",
    )
    return nodes_panel
