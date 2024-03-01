# %%
import requests
from bs4 import BeautifulSoup
import time

# %%
url = "https://crypto-fundraising.info/deal-flow/?category=108"
response = requests.get(url)

# %%


# %%
def get_links_from_url(url: str) -> list[str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    links = [
        link
        for a in soup.find_all("a")
        if (link := a.get("href")) and link.startswith("/projects/")
    ]
    return links


url = "https://crypto-fundraising.info/deal-flow/?category=108"
links = get_links_from_url(url)
links

# %%
project_links = []
for i in range(1, 6):
    url = f"https://crypto-fundraising.info/deal-flow/page/{i}/?category=108"
    links = get_links_from_url(url)
    projet_links.extend(links)
    time.sleep(1)


# %%
project_links = projet_links
project_links

# %%


def get_info_from_project_url(project_url: str) -> dict:
    response = requests.get(project_url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)
    fund_links = [
        url for link in links if (url := link.get("href")).startswith("/funds")
    ]
    category_links = [
        url
        for link in links
        if (url := link.get("href")).startswith(
            "https://crypto-fundraising.info/deal-flow/?category"
        )
    ]
    description = soup.select_one(
        "#primary > div.wrapper.global-wrapper > div.wrapper-w-sidebar.mobiflexcol > div.main-col > div > div.project-description"
    )
    website = soup.select_one(
        "#primary > div.wrapper.global-wrapper > div.wrapper-w-sidebar.mobiflexcol > div.sidebar > div.spoiler-wrap.flexmob1 > div.spoiler-content > div:nth-child(2) > div"
    )
    proejct_name = soup.select_one(
        "#primary > div.wrapper.global-wrapper > div.wrapper-w-sidebar.mobiflexcol > div.main-col > div > div.single-project-header-badge > div.singleproject-name-ticker > h1"
    )
    return {
        "proejct_name": proejct_name and proejct_name.text.strip(),
        "fund_links": fund_links,
        "category_links": category_links,
        "description": description and description.text.strip(),
        "website": website and website.text.strip(),
        "crypto-fundraising": proejct_url,
    }


# proejct_url = "https://crypto-fundraising.info/projects/bitfinity/"
# get_info_from_project_url(proejct_url)

# %%
info_list = []
BASE_URL = "https://crypto-fundraising.info"
for i, project_slug in enumerate(project_links):
    project_url = f"{BASE_URL}{project_slug}"
    print(i, project_url)

    project_info = get_info_from_project_url(project_url)
    print(project_info)

    info_list.append(project_info)
    time.sleep(2)

# %%

import pandas as pd

df = pd.DataFrame(info_list)
df.head()

# %%
get_info_from_project_url(
    "https://crypto-fundraising.info/projects/chainway-labs-citrea"
)

# %%
