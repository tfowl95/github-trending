from datetime import datetime
import urllib.request
import json

def create_url(duration, limit):
    durations = {
        "day": 1,
        "week": 7,
        "month": 30,
        "year": 365
    }
    today = datetime.today().date()
    start_date = (today - timedelta(days=durations[duration])).isoformat()

    per_page = min(100, limit)
    return f"https://api.github.com/search/repositories?q=created%3A%3E{start_date}&per_page={per_page}&sort=stars&order=desc"

def get_repos(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    try:
        with urllib.request.urlopen(req) as response:
            response_headers = dict(response.headers)
            links = response_headers["Link"]
            get_next_link = parse_links(links)
            data = response.read()
            return json.loads(data)
    except Exception as e:
        print(f"Error: {e}")

def parse_links(links):
    pass