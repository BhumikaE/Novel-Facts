from newsapi import NewsApiClient
import pprint

# Init
newsapi = NewsApiClient(api_key="821c0a6bbde847dd8d9414542d2ad9c7")

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='coronavirus',
#                                          country='in')

all_articles = newsapi.get_everything(
    q="cure AND coronavirus AND ginger",
    from_param="2020-05-03",
    to="2020-06-02",
    language="en",
    sort_by="publishedAt",
)

# /v2/sources
sources = newsapi.get_sources()
print(all_articles["articles"][0]["content"])
