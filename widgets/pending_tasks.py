from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from client.elasticsearch import get_plain_response

def display_pending_task_widget() -> Table:
    tasks = get_plain_response('_cat/pending_tasks')
    nodes_panel = Panel(
      Align.center(
          Align.center(tasks),
          vertical="top",
      ),
      box=box.ROUNDED,
      padding=(1, 2),
      title="[bold]Pending Tasks[/]",
      border_style="bright_yellow",
    )
    return nodes_panel
