import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
  search_by_title,
  search_by_date,
  search_by_category,
  search_by_tag
)


def populate_db():
    news_num = input("Digite quantas notícias serão buscadas:")
    get_tech_news(news_num)


def get_by_title():
    title = input("Digite o título:")
    search_by_title(title)


def get_by_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    search_by_date(date)


def get_by_tag():
    tag = input("Digite a tag:")
    search_by_tag(tag)


def get_by_category():
    category = input("Digite a categoria:")
    search_by_category(category)


def get_top_news():
    top_5_news()


def get_top_categories():
    top_5_categories()


def end_script():
    print("Encerrando script")


def option_director(option):
    menu = [
      populate_db,
      get_by_title,
      get_by_date,
      get_by_tag,
      get_by_category,
      get_top_news,
      get_top_categories,
      end_script
    ]
    try:
        if not 0 <= int(option) <= 7:
            print("Opção inválida", file=sys.stderr)
        else:
            menu[int(option)]()

    except ValueError:
        print("Opção inválida", file=sys.stderr)


def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.")

    option = input()

    return option_director(option)