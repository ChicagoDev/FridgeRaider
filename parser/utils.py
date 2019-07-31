from pyld import jsonld
import json
from bs4 import BeautifulSoup
import requests


def retrieve_json_ld(url):
    """
    Request a webpage, find the JSON-LD within the DOM and return it as a raw string.

    :param url: Website that contains JSON-LD data within a script tag
    :return: String
    """

    try:
        website = requests.get(url)
        html = website.text
        soup = BeautifulSoup(html)

        linked_data_tag = soup.find_all('script', attrs={ "type": "application/ld+json" }, limit=1)
        ld_text = linked_data_tag[0].text

        return ld_text

    except:
        raise Exception('Error while Retrieving and Parsing JSON-LD')
