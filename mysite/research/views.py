import feedparser
import urllib.parse
from django.shortcuts import render

def company_research_view(request):
    # Get company name from query string, default is "Apple Inc"
    company_name = request.GET.get("q", "Apple Inc")

    # Encode company name for safe URL
    encoded_name = urllib.parse.quote(company_name)

    # Google News RSS feed for that company
    rss_url = f"https://news.google.com/rss/search?q={encoded_name}"
    feed = feedparser.parse(rss_url)

    # Collect top 5 news articles
    news_items = []
    for entry in feed.entries[:5]:
        news_items.append({
            "title": entry.title,
            "link": entry.link
        })

    context = {
        "name": company_name,
        "description": f"Research summary for {company_name}.",
        "news": news_items,
    }
    return render(request, "company_profile.html", context)
