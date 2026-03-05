import csv
import requests

from datetime import datetime


# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────

API_URL   = "https://jsonplaceholder.typicode.com/posts"
MAX_POSTS = 10


# ─────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────

def timestamp():
    """Return a filesystem-safe timestamp: YYYYMMDD_HHMMSS."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def log(message, entries):
    """Print a message and save it to the log entries list."""
    print(message)
    entries.append(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]  {message}")


# ─────────────────────────────────────────────
# CORE FUNCTIONS
# ─────────────────────────────────────────────

def fetch_posts(url, limit, log_entries):
    """
    Fetch posts from the API.
    Returns a list of post dicts, or empty list on failure.
    """
    log(f"Fetching up to {limit} posts from {url} ...", log_entries)

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            posts = response.json()[:limit]
            log(f"✅ Success — {len(posts)} posts received (HTTP {response.status_code}).", log_entries)
            return posts
        else:
            log(f"❌ Request failed with status code {response.status_code}.", log_entries)
            return []

    except requests.exceptions.ConnectionError:
        log("❌ Connection error — could not reach the API.", log_entries)
        return []
    except requests.exceptions.Timeout:
        log("❌ Request timed out after 10 seconds.", log_entries)
        return []
    except requests.exceptions.RequestException as exc:
        log(f"❌ Unexpected error: {exc}", log_entries)
        return []


def summarise(posts, log_entries):
    """Print and log a short summary of each fetched post."""
    if not posts:
        return

    log("─" * 40, log_entries)
    log(f"  SUMMARY: {len(posts)} posts fetched", log_entries)
    log("─" * 40, log_entries)

    for post in posts:
        short_title = post.get("title", "")[:55]
        log(f"  [{post.get('id'):>3}]  {short_title}", log_entries)


def write_csv(posts, filename, log_entries):
    """Write fetched posts to a .csv file."""
    if not posts:
        log("⚠️  No posts to write — skipping CSV output.", log_entries)
        return

    fieldnames = ["id", "userId", "title", "body"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(posts)

    log(f"📊 CSV written  →  {filename}  ({len(posts)} rows)", log_entries)


def write_txt_log(entries, filename):
    """Write all log entries to a .txt file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("  ACTIVITY LOG — generate_log.py\n")
        f.write("=" * 60 + "\n\n")
        for entry in entries:
            f.write(entry + "\n")
        f.write("\n" + "=" * 60 + "\n")
        f.write("  END OF LOG\n")
        f.write("=" * 60 + "\n")

    print(f"📄 Log written  →  {filename}")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":

    log_entries = []
    ts = timestamp()

    log("=" * 40, log_entries)
    log("  generate_log.py started", log_entries)
    log(f"  Run timestamp: {ts}", log_entries)
    log("=" * 40, log_entries)

    # Step 1 — fetch data from the API
    posts = fetch_posts(API_URL, MAX_POSTS, log_entries)

    # Step 2 — summarise what was fetched
    summarise(posts, log_entries)

    # Step 3 — write CSV output
    csv_filename = f"posts_{ts}.csv"
    write_csv(posts, csv_filename, log_entries)

    # Step 4 — write the activity log last (captures all messages)
    log("✅ All tasks complete.", log_entries)
    txt_filename = f"log_{ts}.txt"
    write_txt_log(log_entries, txt_filename)


