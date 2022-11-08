import requests
import time
from parsel import Selector


def fetch(url):
    try:
        time.sleep(1)
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text

        return None
    except requests.Timeout:
        return None


def scrape_novidades(html_content):
    selector = Selector(html_content)
    new_list = selector.css(".cs-overlay-link::attr(href)").getall()
    return new_list


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    html_content = fetch("https://blog.betrybe.com/")
    print(scrape_novidades(html_content))
