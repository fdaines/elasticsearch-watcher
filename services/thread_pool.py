from client.elasticsearch import get_plain_response
from config import threadPoolConfig
from models.thread_pool import thread_pool_info

include_threads = threadPoolConfig["include_threads"]
include_nodes = threadPoolConfig["include_nodes"]
exclude_nodes = threadPoolConfig["exclude_nodes"]

def item_should_be_added(item):
    should_be_added = False
    if len(include_threads)==1 and include_threads[0]=="*":
        should_be_added = True
    if len(include_nodes)==1 and include_nodes[0]=="*":
        should_be_added = True
    if item.node_name in exclude_nodes:
        should_be_added = False
    if len(include_threads)>0 and include_threads[0]!="*" and item.thread_name not in include_threads:
        should_be_added = False

    return should_be_added

def get_thread_pool_information():
    response = get_plain_response('_cat/thread_pool?s=node_name')
    nodes = response.splitlines()
    info_list = []

    for n in nodes:
        nx = thread_pool_info(n)
        if item_should_be_added(nx):
            info_list.append(nx.toDataTable())

    return info_list
