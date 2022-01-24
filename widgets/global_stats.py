from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from services.global_stats import get_global_stats

def display_global_stats_widget() -> Table:
    stats = get_global_stats()

    stats_table = Table.grid(padding=(0,0,0,1))
    stats_table.add_column(style="green", justify="right")
    stats_table.add_column(no_wrap=True)
    stats_table.add_row("Store Size", stats.store_size)
    stats_table.add_row("Search Open Context", stats.search_open_contexts)
    stats_table.add_row("Search Current Queries", stats.search_query_context)
    stats_table.add_row("Search Current Fetch", stats.search_fetch_current)
    stats_table.add_row("Search Current Scroll", stats.search_scroll_current)
    stats_table.add_row("Query Cache Size", stats.query_cache_memory_size)
    stats_table.add_row("Query Cache Evictions", stats.query_cache_evictions)
    stats_table.add_row("Fielddata Memory Size", stats.fielddata_memory_size)
    stats_table.add_row("Fielddata Evictions", stats.fielddata_evictions)
    stats_table.add_row("RequestCache Size", stats.request_cache_memori_size)
    stats_table.add_row("RequestCache Evictions", stats.request_cache_evictions)

    nodes_panel = Panel(
      Align.center(
          Align.center(stats_table),
          vertical="top",
      ),
      box=box.ROUNDED,
      padding=(1, 2),
      title="[bold]Global Stats[/]",
    )
    return nodes_panel
