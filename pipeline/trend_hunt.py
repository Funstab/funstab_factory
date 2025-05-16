import requests, datetime, sqlite_utils, pathlib, random
db = sqlite_utils.Database("storage/backlog.db")

def tiktok_tags():
    url = ("https://business-api.tiktok.com/open_api/v1.2/"
           "trend/hashtag/list/?country_code=US&date="
           f"{datetime.date.today()}&interval=HOUR")
    data = requests.get(url).json()
    for h in data["data"]["hashtag_list"][:10]:
        yield h["hashtag_name"].lstrip("#")

topics = set(tiktok_tags())
table = db["queue"]
table.create({"topic": str, "status": str, "added": str}, pk="topic", alter=True)

for word in random.sample(list(topics), 5):
    try:
        table.insert({"topic": word, "status": "NEW",
                      "added": datetime.datetime.now().isoformat()})
    except sqlite_utils.db.IntegrityError:
        pass
print("★ added", len(topics), "topics to the backlog")
