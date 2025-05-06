import os
import subprocess

OUTPUT_DIR = "/output"

def fetch_all_streams():
    for key, url in os.environ.items():
        if key.startswith("YOUTUBE_URL_"):
            stream_name = key.replace("YOUTUBE_URL_", "").lower()
            filename = f"{OUTPUT_DIR}/{stream_name}.txt"
            print(f"[fetch_url] Fetching stream for {key} → {filename}")
            try:
                result = subprocess.run(
                    ["yt-dlp", "-g", url],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                if result.returncode == 0:
                    with open(filename, "w") as f:
                        f.write(result.stdout.strip())
                    print(f"[fetch_url] Updated {filename}")
                else:
                    print(f"[fetch_url] yt-dlp failed for {key}: {result.stderr}")
            except Exception as e:
                print(f"[fetch_url] Exception fetching {key}: {e}")

if __name__ == "__main__":
    fetch_all_streams()