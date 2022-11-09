from tech_news.database import search_news
import datetime


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(new["title"], new["url"]) for new in news]


def search_by_date(date):
    try:
        date_formmat = datetime.datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        news = search_news({"timestamp": {"$regex": date_formmat}})
        return [(new["title"], new["url"]) for new in news]
    except ValueError:
        raise ValueError("Data inválida")


def search_by_tag(tag):
    pass


def search_by_category(category):
    pass


# if __name__ == "__main__":
#     print(search_by_title("BACANA"))
#     search_by_date("2022-04-07")
#     search_by_date(["Tecnologia", "TECNOLOGIA", "Esportes", "Aloha"])
