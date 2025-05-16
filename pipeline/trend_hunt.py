# trend_hunt.py  –  v2  (Google Trends + Reddit /r/news)
import datetime, random, sqlite_utils, requests, textwrap

db = sqlite_utils.Database("storage/backlog.db")
queue = db["queue"]
queue.create({"topic": str,
              "status": str,
              "added": str},
              pk="topic", ignore=True)

# ---------- 1. Google daily hot searches ----------
import feedparser, time

def google_hot():
    """Return today’s top Google-Trends queries (RSS feed = no auth needed)."""
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"
    feed = feedparser.parse(url)
    # Protect against empty feed / network error
    if not feed.entries:
        print("Google RSS empty; skipping")
        return []
    # Keep the first 20 titles
    return [e.title for e in feed.entries[:20]]

google_topics = google_hot()

# ---------- 2. Reddit front-page news ----------
reddit = requests.get(
    "https://www.reddit.com/r/news/hot.json?limit=20",
    headers={"User-Agent": "funstab-bot"}
).json()
reddit_topics = [p["data"]["title"].split(" - ")[0]
                 for p in reddit["data"]["children"]]

all_topics = set(google_topics) | set(reddit_topics)
picked = random.sample(list(all_topics), 10)   # choose 10 to avoid spam

added = 0
for t in picked:
    try:
        queue.insert({"topic": t.strip(),
                      "status": "NEW",
                      "added": datetime.datetime.now().isoformat()})
        added += 1
    except sqlite_utils.db.IntegrityError:
        pass    # already in backlog

print(f"★ Added {added} fresh topics to backlog, total rows:",
      queue.count)
