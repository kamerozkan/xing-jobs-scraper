"""Run xing-jobs-scraper on Apify and print the results. pip install apify-client"""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {'queries': ['python developer'], 'location': 'Berlin', 'maxItems': 20}
run = client.actor("kamerozkan/xing-jobs-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
