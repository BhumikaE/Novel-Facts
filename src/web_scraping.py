from bs4 import BeautifulSoup  # BeautifulSoup is in bs4 package
from urllib.request import Request, urlopen
import ssl
import pandas as pd
import pickle


ssl._create_default_https_context = ssl._create_unverified_context


class Web:
    def __init__(self):
        pass

    def scraping_for_fake_news_data(self):
        scraped_data = []
        for i in range(1, 467):
            x = str(i)
            main_page_url = (
                "https://www.poynter.org/ifcn-covid-19-misinformation/page/" + x + "/"
            )
            print("Page number being scraped is: " + x + "/466")

            req = Request(main_page_url, headers={"User-Agent": "Mozilla/5.0"})
            webpage = urlopen(req).read()

            soup = BeautifulSoup(webpage, "html.parser")
            rows = [
                tag["href"]
                for tag in soup.find_all(
                    "a",
                    {
                        "class": "button entry-content__button entry-content__button--smaller"
                    },
                )
            ]

            for row in rows:
                inner_page_url = row
                req2 = Request(inner_page_url, headers={"User-Agent": "Mozilla/5.0"})
                webpage_new = urlopen(req2).read()
                soup2 = BeautifulSoup(webpage_new, "html.parser")
                created_by = soup2.find_all("p", {"class": "entry-content__text"})
                headline = soup2.find("h1", {"class": "entry-title"})
                explanation = soup2.find(
                    "p",
                    attrs={
                        "class": "entry-content__text entry-content__text--explanation"
                    },
                )
                url3 = soup2.find(
                    "a",
                    {
                        "class": "button entry-content__button entry-content__button--smaller"
                    },
                )["href"]
                if not url3.startswith("http"):
                    url3 = ""
                all_text = (
                    created_by[0].text
                    + "\n"
                    + created_by[1].text
                    + headline.text
                    + explanation.text
                    + "\n"
                    + url3
                )
                all_text = all_text.replace("|", "")
                scraped_data.append(all_text)

        return scraped_data

    def save_to_data_frame(self, scraped_list):
        regex = (
            r"Fact-checked by:(?P<Source>[A-Za-z ].*)\n"  # 2 capital letters
            r"(?P<date>\d{4}/\d{2}/\d{2})\s+"
            r"(?P<Country>[A-Za-z].*)\n"
            r"(?P<Status>[A-Za-z ].*): "
            r"(?P<FakeNews>.*).\t\t"
            r"(?P<Explanation>[A-Za-z ].*).\n"
            r"(?P<Url>.*)"
        )

        data_set = pd.Series(scraped_list)
        df = pd.DataFrame(data_set.str.extract(regex))
        df.to_excel(r"./Data/ScrapedFakeNewsData.xlsx", index=False)

        return df

    def fetch_fake_news_data_set(self):
        data = self.scraping_for_fake_news_data(self)
        df = self.save_to_data_frame(self, data)
        return df

    def get_saved_news_data(self):
        self.df = pd.read_excel("./Data/ScrapedFakeNewsData.xlsx")
        # print(df)
        return self.df

    def get_full_news_data(self, results):

        # test = self.df.loc[self.df['FakeNews'].isin([results[0][0],results[0][1],results[0][2]])]
        test = self.df.loc[self.df["FakeNews"] == results[0][0]]
        # row = self.df.loc[self.df['column_name'] == result[0]]
        return test
