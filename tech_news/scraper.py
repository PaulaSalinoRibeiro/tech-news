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
    selector = Selector(html_content)
    next_page = selector.css(".next::attr(href)").get()
    return next_page


def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = selector.css(".post-comments-simple h5::text").get() or 0
    summary = selector.xpath("string(//p)").get().strip()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css(".meta-category span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


if __name__ == "__main__":
    html_content = fetch(
        "https://blog.betrybe.com/noticias/bill-gates-e-cetico-sobre-criptomoedas-e-nfts-entenda-o-motivo/"
    )
    # print(scrape_novidades(html_content))
    # print(scrape_next_page_link(html_content))
    print(scrape_noticia(html_content))
