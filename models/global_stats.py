import json

class GlobalStats:
    def __init__(self):
        self.store_size = None
        self.search_open_contexts = None
        self.search_query_context = None
        self.search_fetch_current = None
        self.search_scroll_current = None
        self.query_cache_memory_size = None
        self.query_cache_evictions = None
        self.fielddata_memory_size = None
        self.fielddata_evictions = None
        self.request_cache_memori_size = None
        self.request_cache_evictions = None
