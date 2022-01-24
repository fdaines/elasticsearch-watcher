from client.elasticsearch import get_json_response
from models.indices import index

def get_indices_with_cache():
    response = get_json_response('_stats?human')
    total = response["_all"]["total"]
    indicesDictionary = response["indices"]

    indices = []
    for key, value in indicesDictionary.items():
        if value["total"]["query_cache"]["memory_size_in_bytes"] > 0 or value["total"]["request_cache"]["memory_size_in_bytes"] > 0:
            indices.append(index(key,
              value["total"]["request_cache"]["memory_size_in_bytes"],
              value["total"]["query_cache"]["memory_size_in_bytes"]),
            )

    indices = sorted(indices, key=lambda n: n.request_cache, reverse=True)

    return indices
