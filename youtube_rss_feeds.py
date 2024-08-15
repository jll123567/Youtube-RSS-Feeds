import requests, re
from sys import argv
from bs4 import BeautifulSoup


opml_header = """
<?xml version="1.0" encoding="UTF-8"?>
  <opml version="2.0">
    <head>
      <title>Youtube Subscriptions</title>
    </head>
    <body>
      <outline text="Youtube Subscriptions">
      
"""
opml_footer = """
    </outline>
  </body>
</opml>

"""

def subs_to_opml(subs_file, output_path="subs.opml"):
    opml_body = ""
    with open(subs_file, "r") as f:
        links = sorted(set([a.attrs["href"] for a in BeautifulSoup(f, features="html5lib").find_all('a', 'channel-link')]), key=str.casefold)
        for link in links:
            request = requests.get(link)
            if request.status_code != 200:
                print(f"Could not get page for {link}. Skipping.")
                continue
            ch_id = re.search(r'<link rel="canonical" href="https://www.youtube.com/channel/([A-Za-z0-9-_]+)', request.text)[1]
            ch_name = re.search(r'<title>(.*) - YouTube</title>', request.text)[1]
            feed = f"https://www.youtube.com/feeds/videos.xml?channel_id={ch_id}"
            print(f"{link} -> {feed}")
            opml_body += f'        <outline text="{ch_name}" title="{ch_name}" type="rss" xmlUrl="{feed}" htmlUrl="{link}" />\n'

    with open(output_path, "w") as f:
        f.write(opml_header+opml_body+opml_footer)

if __name__ == "__main__":
    if len(argv) < 2 or "-h" in argv:
        print("Usage: python youtube_rss_feeds.py <subscriptons-html-file> [output-path]\n  python youtube_rss_feeds.py -h for this help")
    elif len(argv) == 2:
        subs_to_opml(argv[1])
    else:
        subs_to_opml(argv[1], argv[2])
