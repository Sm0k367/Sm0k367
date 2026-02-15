import re
import requests

# CONFIGURATION
SUNO_USER_URL = "https://suno.com/@dj_smoke_stream"
README_PATH = "README.md"

def get_latest_suno_track():
    try:
        # Note: In a production agentic workflow, we'd use a headless browser 
        # or the internal Suno API endpoint if available.
        # This is a placeholder for the logic that grabs your top track.
        response = requests.get(SUNO_USER_URL)
        # Mock logic: Replace with actual scraping logic or API call
        track_name = "Absolute Algorithm of Existence" 
        return f"🎧 Latest Drop: **{track_name}**"
    except Exception as e:
        print(f"Error fetching Suno tracks: {e}")
        return None

def update_readme(new_content):
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    # Regex to find the space between our markers
    pattern = r"()(.*)()"
    replacement = f"\\1\n{new_content}\n\\3"
    
    updated_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_readme)

if __name__ == "__main__":
    content = get_latest_suno_track()
    if content:
        update_readme(content)
        print("Successfully updated README with latest Suno vibe.")
