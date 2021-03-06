from future import Future

hit_list = [ "http://...", "...", "..." ] # list of feeds to pull down

# pull down all feeds
future_calls = [Future(feedparser.parse,rss_url) for rss_url in hit_list]
# block until they are all in
feeds = [future_obj() for future_obj in future_calls]

entries = []
for feed in feeds:
    entries.extend( feed[ "items" ] )

sorted_entries = sorted(entries, key=lambda entry: entry["date_parsed"])
sorted_entries.reverse() # for most recent entries first