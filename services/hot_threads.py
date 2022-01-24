from client.elasticsearch import get_plain_response
from models.hot_threads import node

def get_hot_threads():
    response = get_plain_response('_nodes/hot_threads')
    return parse_hot_threads(response)

def parse_hot_threads(response):
    lines = response.splitlines()
    array = []
    current = None
    for s in lines:
        if s.startswith("::: "):
            current = node(s)
        if s.startswith("   ") and s.find("cpu usage by thread") >= 0:
            current.add_usage(s)
        if s == "":
            array.append(current)

    hot_threads = []
    for item in array:
        if len(item.usages) > 0:
            hot_threads.append("[bold white]"+item.name+"[/bold white]")
            for u in item.usages:
                hot_threads.append("[bold yellow]"+u+"[/bold yellow]")
            hot_threads.append("\n")

    return "\n".join(hot_threads)
