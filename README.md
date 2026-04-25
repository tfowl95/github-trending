# GitHub Trending CLI

A lightweight Python CLI tool that fetches trending GitHub repositories based on creation date, star count, and a configurable time window. Results are pulled from the GitHub Search API and displayed in a simple ranked terminal output.

---

## Overview

This tool queries GitHub’s repository search endpoint and returns the most popular repositories created within a selected time range. Results are sorted by star count and limited by user input.

---

## Concepts Demonstrated

* REST API consumption using `requests`
* Query parameter construction for APIs
* Pagination handling via HTTP `Link` headers
* CLI argument parsing with `argparse`
* Basic data aggregation and limiting results
* Modular separation of CLI logic and API utilities

---

## Features

* Fetches trending repositories from GitHub Search API
* Configurable time window: day, week, month, year
* Customizable result limit
* Sorted by star count (descending)
* Handles paginated API responses
* Simple terminal output format

---

## Project Structure

```
github-trending      # CLI entry point, output formatting
cli.py               # Argument parsing logic
utils.py             # API interaction and pagination handling
```

---

## Requirements

* Python 3.7+
* Internet connection (GitHub API access)
* `requests` library

---

Install dependency:

```
pip install requests
```

## Installation

1. Clone the repository:

```
git clone https://github.com/tfowl95/github-trending.git
cd github-trending
```

2. Add to PATH

3. Make executable (macOS/Linux):

```
chmod +x github-trending
```

---

## Usage

Run the script:

```
github-trending --duration <day|week|month|year> --limit <number>
```

Example:

```
github-trending --duration week --limit 10
github-trending --duration month --limit 25
```

---

## Example Output

```
10136 stars: OpenMythos
https://github.com/kyegomez/OpenMythos
A theoretical reconstruction of the Claude Mythos architecture, built from first principles using the available research literature.
-----------
6132 stars: huashu-design
https://github.com/alchaincyf/huashu-design
Huashu Design · HTML-native design skill for Claude Code · Claude Code 里 HTML 原生的设计 skill · 高保真原型 / 幻灯片 / 动画 + 20 设计哲学 + 5 维评审 + MP4 导出 · Agent-agnostic
-----------
3282 stars: awesome-gpt-image-2-prompts
https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts
Curated GPT-Image-2 prompts fot the Openai API：image examples across portraits, posters, UI mockups, character sheets, and community experiments.
-----------
3058 stars: Kami
https://github.com/tw93/Kami
👩‍🚒 Good content deserves good paper.
-----------
2196 stars: open-codesign
https://github.com/OpenCoworkAI/open-codesign
Open-source Claude Design alternative. One-click import your Claude Code / Codex API key. Prompt → prototype / slides / PDF. Multi-model (Claude, GPT, Gemini, Kimi, GLM, Ollama). BYOK, local-first, MIT.
-----------
```

---

## How It Works

1. CLI arguments are parsed in `cli.py` using `argparse`.
2. The selected time window is converted into a start date.
3. `utils.py` constructs a GitHub Search API query:
    `https://api.github.com/search/repositories?q=created:>YYYY-MM-DD&sort=stars&order=desc`
4. A request is made using `requests.get()` with headers and query parameters.
5. Results are extracted from the JSON response (`items` field).
6. Pagination is handled using the `Link` header to follow `next` pages.
7. Repositories are accumulated until the requested limit is reached.
8. Final results are printed to the terminal.

---

## Error Handling

* Network/API request failures
* Missing or malformed Link headers
* Unexpected JSON structure
* Graceful fallback via exception capture in request loop

---

## Notes

* Results depend on GitHub Search API availability and rate limits
* Trending behavior is approximated via creation date + star ranking
* Only public repositories are returned
* Pagination is required for larger result sets

---

## License

No license specified.
