import requests
import time
from parsel import Selector
from tech_news.database import create_news


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


def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    news = []
    page = 0

    while page < amount:
        html_content = fetch(url)
        link_news_by_page = scrape_novidades(html_content)

        for link in link_news_by_page:
            if page == amount:
                break
            new = scrape_noticia(fetch(link))
            news.append(new)
            page += 1

        url = scrape_next_page_link(html_content)

    create_news(news)
    return news


# if __name__ == "__main__":
#     # print(get_tech_news(4))
