from datetime import datetime, timedelta
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

def get_repos(url, limit):
    repos_returned = 0
    repos = []
    while repos_returned < limit:
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/vnd.github+json")
        try:
            with urllib.request.urlopen(req) as response:
                response_headers = dict(response.headers)
                links_header = response_headers["Link"]
                url = get_next_url(links_header)
                data = response.read()
                payload = json.loads(data)
                new_repos = payload["items"]
                length = len(new_repos)
                print(length)
                repos_returned += length
                if repos_returned > limit:
                    remaining_num_repos = limit - len(repos)
                    repos.extend(new_repos[0:remaining_num_repos])
                else:
                    repos.extend(new_repos)
        except Exception as e:
            print(f"Error: {e}")
    return repos

def get_next_url(links_header):
    links = {}
    parts = links_header.strip().split(",")
    for part in parts:
        section = part.strip().split(";")
        url = section[0].strip()[1:-1]
        k, v = section[1].strip().split("=")
        v = v.strip('"')
        if v == "next":
            return url