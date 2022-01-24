import json
import os
import sys
import validators

from rich.prompt import Confirm, Prompt

with open('config.json') as config_file:
    data = json.load(config_file)

nodesConfig = data['nodes']
threadPoolConfig = data['thread_pool']
refreshTime = data['refresh_time']

def get_elasticsearch_url():
    return os.getenv('ELASTICSEARCH_HOST')

def get_elasticsearch_apikey():
    return os.getenv('ELASTICSEARCH_APIKEY')

def check_environment_variables():
    if get_elasticsearch_url() == None or get_elasticsearch_url() == "":
        print("ELASTICSEARCH_HOST environment variable has not been defined or is empty.")
        if Confirm.ask("Do you want to setup the ELASTICSEARCH_HOST environment variable", default="y"):
            host = Prompt.ask("Please provide a single endpoint for ElasticSearch Cluster")
            if validators.url(host) is not True:
                print("ElasticSearch Host is not a valid URL.")
                sys.exit(1)

            if not host.endswith('/'):
                host = host + '/'

            os.environ['ELASTICSEARCH_HOST'] = host
            print(os.getenv("ELASTICSEARCH_HOST"))
            if Confirm.ask("Do you want to setup an APIKEY for ElasticSearch Cluster"):
                os.environ['ELASTICSEARCH_APIKEY'] = Prompt.ask("Please provide the APIKEY for ElasticSearch Cluster")
        else:
            sys.exit(1)
