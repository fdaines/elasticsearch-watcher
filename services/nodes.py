from rich import box
from rich.align import Align
from rich.panel import Panel
from rich.table import Table

from client.elasticsearch import get_plain_response
from models.nodes import node
from config import nodesConfig

def get_nodes_information():
    response = get_plain_response('_cat/nodes?h=ip,name,heap.percent,ram.percent,cpu,load_1m,load_5m,load_15m,node.role,master')
    node_lines = response.splitlines()
    nodes_list = []
    for n in node_lines:
        nx = parse_from_line(n)
        if nx.name not in nodesConfig["exclude_nodes"]:
            nodes_list.append(nx)
    nodes_list = sorted(nodes_list, key=lambda n: n.name)
    return nodes_list

def parse_from_line(node_line):
    tokens = node_line.split()

    item = node()
    item.name = tokens[1]
    if len(tokens)>2:
        item.heap = int(tokens[2])
    if len(tokens)>3:
        item.ram = int(tokens[3])
    if len(tokens)>4:
        item.cpu = int(tokens[4])
    if len(tokens)>5:
        item.load1 = float(tokens[5])
    if len(tokens)>6:
        item.load5 = float(tokens[6])
    if len(tokens)>7:
        item.load15 = float(tokens[7])

    return item
