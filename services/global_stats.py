import json

from client.elasticsearch import get_json_response
from models.global_stats import GlobalStats

def get_global_stats():
    response = get_json_response('_stats?human')
    stats = from_json(response["_all"]["total"])

    return stats

def from_json(json_object):
    item = GlobalStats()
    item.store_size = json.dumps(json_object["store"]["size"])
    item.search_open_contexts = json.dumps(json_object["search"]["open_contexts"])
    item.search_query_context = json.dumps(json_object["search"]["query_current"])
    item.search_fetch_current = json.dumps(json_object["search"]["fetch_current"])
    item.search_scroll_current = json.dumps(json_object["search"]["scroll_current"])
    item.query_cache_memory_size = json.dumps(json_object["query_cache"]["memory_size"])
    item.query_cache_evictions = json.dumps(json_object["query_cache"]["evictions"])
    item.fielddata_memory_size = json.dumps(json_object["fielddata"]["memory_size"])
    item.fielddata_evictions = json.dumps(json_object["fielddata"]["evictions"])
    item.request_cache_memori_size = json.dumps(json_object["request_cache"]["memory_size"])
    item.request_cache_evictions = json.dumps(json_object["request_cache"]["evictions"])

    return item
