import requests
from bs4 import BeautifulSoup

def get_job_listings(keywords):
    listings = []

    for keyword in keywords:
        query = f"{keyword} site:in.indeed.com OR site:wellfound.com OR site:naukri.com"
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"

        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')

        for g in soup.select('div.g'):
            title_tag = g.find('h3')
            link_tag = g.find('a')
            if title_tag and link_tag:
                title = title_tag.text.strip()
                link = link_tag['href']
                listings.append(f"🔹 {title}\n🔗 {link}")

    return listings[:10]  # limit results
