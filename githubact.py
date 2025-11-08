import requests 
import sys

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    
    if response.status_code == 200:
        events = response.json()
        return events
    else:
        print(f"Error: Unable to fetch data for user '{username}'. Status code: {response.status_code}")
        return None


def display_activity(events):
    if events:
        for event in events:
            event_type = event['type']
            repo_name = event['repo']['name']
            created_at = event['created_at']
            print(f"{created_at}: {event_type} in {repo_name}")
    else:
        print("No events found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)

    username = sys.argv[1]
    events = fetch_github_activity(username)
    display_activity(events)