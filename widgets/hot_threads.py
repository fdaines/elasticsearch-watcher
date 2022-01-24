from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from services.hot_threads import get_hot_threads

def get_hot_threads_widget() -> Table:
    panel = Panel(
      Align.center(
          Align.center(get_hot_threads()),
          vertical="top",
      ),
      box=box.ROUNDED,
      padding=(1, 2),
      title="[bold]Hot Threads[/]",
      border_style="bright_red",
    )
    return panel
