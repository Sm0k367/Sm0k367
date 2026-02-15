import re
import requests

# This points to your Suno profile
SUNO_USER_URL = "https://suno.com/@dj_smoke_stream"
README_PATH = "README.md"

def get_latest_suno_track():
    try:
        # For now, this acts as a high-tier placeholder. 
        # When Suno's API/scrapers update, you change this one line.
        track_name = "Absolute Algorithm" 
        return f"🎧 Latest Drop: **{track_name}**"
    except Exception as e:
        print(f"Error: {e}")
        return None

def update_readme(new_content):
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    # This looks for the markers we will add to your README in the next step
    pattern = r"()(.*)()"
    replacement = f"\\1\n{new_content}\n\\3"
    
    updated_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_readme)

if __name__ == "__main__":
    content = get_latest_suno_track()
    if content:
        update_readme(content)
        print("Vibe synced.")
