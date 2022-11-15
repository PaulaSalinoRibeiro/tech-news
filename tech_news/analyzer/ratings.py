from operator import itemgetter
from tech_news.database import search_news


def top_5_news():
    news = search_news({})
    result = sorted(news, key=itemgetter('comments_count'), reverse=True)
    if len(result) > 5:
        result = result[:5]

    return [(article["title"], article["url"])for article in result]


def top_5_categories():
    news = search_news({})
    categories = dict()
    for article in news:
        if article["category"] in categories:
            categories[article["category"]] += 1
        else:
            categories[article["category"]] = 1

    result = sorted(
      [(category, categories[category]) for category in categories],
      key=lambda x: (x[0], -x[1]))

    return [tup[0] for tup in sorted(result, key=lambda x: -x[1])][:5]