from rich.__main__ import make_test_card
from rich.console import Console
from rich import inspect
from rich.color import Color
import signal
import sys
import threading

color = Color.parse("red")
inspect(color, methods=True)


def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C')
forever = threading.Event()
forever.wait()
