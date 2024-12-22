import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Functions for downloading and file handling
def download(m3u8_url: str, output: str = "output.mp4", ffmpeg_path: str = "") -> None:
    """Download video from m3u8 URL using ffmpeg"""
    command = ""

    if not ffmpeg_path:
        command = "ffmpeg"
    else:
        command = ffmpeg_path

    command += f" -i {m3u8_url} -vcodec copy -acodec copy {output}"
    os.system(command)

def remove_file(file: str) -> None:
    """Remove temporary files if needed"""
    os.remove(file)

def extract_m3u8_url(text: str) -> str:
    """Extract m3u8 URL from the console log text"""
    text = text.replace("\\", "")
    for i in text.split('"'):
        if ".m3u8" in i and ("playlist_" in i or "master_dynamic_" in i):
            return i

# JavaScript to intercept network requests and capture m3u8 URL
listener_js = """
(function () {
    var origin = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function () {
        this.addEventListener("load", function () {
            var t = this.responseText;

            if (t.includes(".m3u8") && (t.includes("playlist_") || t.includes("master_dynamic_"))) {
                console.error(t);
            }
        });
        origin.apply(this, arguments);
    };
})();
"""

# Selenium script for capturing m3u8 URL
def capture_m3u8_url(url: str, profile_path: str) -> str:
    """Use Selenium to capture m3u8 URL from the provided Twitter broadcast URL using a specific profile"""
    options = Options()
    options.add_argument(f"user-data-dir={profile_path}")  # Path to your Chrome profile
    options.add_argument("profile-directory=Default")  # Use Default profile, change if needed
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    # Execute the JavaScript code to intercept network requests
    driver.execute_script(listener_js)

    data = ""
    
    # Wait until m3u8 URL is found in the console logs
    while not data:
        for i in driver.get_log("browser"):
            if (
                "message" in i
                and "source" in i
                and i["source"] == "console-api"
                and ".m3u8" in i["message"]
            ):
                data = i["message"]
        
        # Adding a short delay to avoid overloading the system
        time.sleep(1)

    driver.quit()  # Close the browser after capturing data

    # Extract and return the m3u8 URL
    return extract_m3u8_url(data)

# Main function to coordinate the whole process
def main():
    """Main function to download video from Twitter broadcast URL"""
    # Get the URL from the user input
    url = input("Enter the Twitter broadcast URL (e.g., https://x.com/AlArabiya/live): ")

    # Dynamically get the current user's name
    user_name = os.getlogin()  # Get the current logged-in user
    profile_path = os.path.join("C:\\Users", user_name, "AppData", "Local", "Google", "Chrome", "User Data")

    # Capture the m3u8 URL using Selenium
    m3u8_url = capture_m3u8_url(url, profile_path)

    if m3u8_url:
        print("m3u8 URL captured successfully:", m3u8_url)
        # Start downloading the video
        download(m3u8_url)
        print("Download completed!")
    else:
        print("Failed to capture m3u8 URL.")

# Entry point for the script
if __name__ == "__main__":
    main()
