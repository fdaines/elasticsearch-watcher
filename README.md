# elasticsearch-watcher
Tool to watch some ElasticSearch information

ElasticSearch Watcher is a simple tool to visualize

## Getting Started

### Run app locally

#### Prerequisites
- Python 3.6+

#### Environment variables
*elasticsearch-watcher* uses the following environment variables:

| Variable Name        | Description                                                                                                      |
| -------------------- |:-----------------------------------------------------------------------------------------------------------------|
| ELASTICSEARCH_HOST   | This is the URL to the ElasticSearch host REST API                                                               |
| ELASTICSEARCH_APIKEY | This value is optional and is required only if yout ElasticSearch host requires an APIKEY to access the REST API |

If the previous environment variables were not setted up, then *elasticsearch-watcher* will ask for them.

#### Run application
```
docker build --no-cache --rm -t elasticsearch-watcher .
```

#### Run inside docker container

1. Build a Docker image using the `Dockerfile` file
```
docker build --no-cache --rm -t elasticsearch-watcher .
```

2. Launch a Docker container (mapping env values)
If you run the container in this way, then elasticsearch-watcher will ask for the host and apikey
```
docker run -it elasticsearch-watcher
```

You can pass environment values when starting the docker container, but I think this way is not secure
```
docker run -e ELASTIC_SEARCH_HOSTS="" -e ELASTIC_SEARCH_APIKEY="" -it elasticsearch-watcher
```

## Maintainers

[Francisco Daines](https://github.com/fdaines)
