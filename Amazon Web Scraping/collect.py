from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': []}  # empty lists to collect data

for file in os.listdir("data"):
    try:

        with open(f"data/{file}", encoding="utf-8") as f:
            html_doc = f.read()
        
        soup = BeautifulSoup(html_doc, "html.parser")
        
        t = soup.find("h2")
        if not t:
            continue  # skip if no <h2>
        
        title = t.get_text(strip=True)
        
        ##l = t.find("a")
        ###if l and l.has_attr("href"):   # ✅ safe check
         #   link = "https://amazon.in/" + l["href"]
        #else:
           # link = None   # fallback

        p = soup.find("span" , attrs={"class" : 'a-price-whole'})
        price = p.get_text()
        d["title"].append(title)
        d["price"].append(price)
    except Exception as e:
        print(e)
        

df = pd.DataFrame(data=d)
df.to_csv("data.csv")

