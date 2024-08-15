# Youtube-RSS-Feeds
A small python program to take your YouTube subscriptons, get the channel's RSS feeds, and format them into an OPML file.

## Prerequisites
This is made to be run from the command line(im lazy).
It also depends on `beautifulsoup4` and `requests` so `pip install` them.
Like I said, Im lazy and this isn't packaged nicely or anything.

## Installation
Download `youtube_rss_feeds.py`.

## Usage
Assuming that it runs on your machine...
1. Download the webpage with your subscriptions [link here](https://www.youtube.com/feed/channels).
  * You can do this in most browsers by pressing `ctrl-s`.
2. Run the script with `python youtube_rss_feeds.py <path to subscriptions html> [optional output opml path]`.
  * If no output path is specified, the output is to `subs.opml` in the current directory.
3. Wait for the script to make your feedlist...
4. Import into your feedreader!

## Notes
This was written on 8/15/2024 and makes some assumptions about how youtube structures /feed/channels and their channel html. 
If they change it, this code will break.

If something breaks please make an issue :)
