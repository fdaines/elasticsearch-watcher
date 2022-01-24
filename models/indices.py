REQUEST_CACHE_LIMIT = 200*1024*1024
QUERY_CACHE_LIMIT = 200*1024*1024

class index:
    def __init__(self, name, request_cache, query_cache):
        self.name = name
        self.request_cache = request_cache
        self.query_cache = query_cache
