from rich import box
from rich.align import Align
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from time import sleep
import signal
import sys
import threading

from config import refreshTime, check_environment_variables
from widgets.global_stats import display_global_stats_widget
from widgets.header import display_information_widget
from widgets.hot_threads import get_hot_threads_widget
from widgets.indices import get_indices_with_cache_widget
from widgets.pending_tasks import display_pending_task_widget
from widgets.nodes import make_nodes_information_widget
from widgets.thread_pool import generate_thread_pool_widget


def signal_handler(received_signal, frame):
    sys.exit(0)


def createLayout() -> Layout:
    loading_panel = Panel(Align.center(
            Align.center("Loading..."),
            vertical="top",
        ),
        box=box.ROUNDED,
    )
    layout = Layout()
    layout.split(
        Layout(loading_panel, name="header", size=10),
        Layout(loading_panel, name="main_container"),
    )
    layout["main_container"].split_row(
        Layout(loading_panel, name="left_container", ratio=1),
        Layout(loading_panel, name="indices", ratio=1),
        Layout(loading_panel, name="right_container", ratio=1),
    )
    layout["right_container"].split(
        Layout(loading_panel, name="thread_pool"),
    )
    layout["left_container"].split(
        Layout(loading_panel, name="left_top_container", size=15),
        Layout(loading_panel, name="nodes", ratio=1),
        Layout(loading_panel, name="hot_threads", ratio=1),
    )
    layout["left_top_container"].split_row(
        Layout(loading_panel, name="stats"),
        Layout(loading_panel, name="pending_tasks"),
    )
    return layout


if __name__ == '__main__':
    check_environment_variables()
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    console = Console()
    console.clear()

    with console.pager():
        layout = createLayout()
        with Live(layout, screen=False):
            while True:
                layout["header"].update(display_information_widget())
                layout["stats"].update(display_global_stats_widget())
                layout["pending_tasks"].update(display_pending_task_widget())
                layout["nodes"].update(make_nodes_information_widget())
                layout["hot_threads"].update(get_hot_threads_widget())
                layout["indices"].update(get_indices_with_cache_widget())
                layout["thread_pool"].update(generate_thread_pool_widget())
                sleep(refreshTime)
