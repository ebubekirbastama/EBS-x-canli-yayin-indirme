
# m3u8 Video Downloader using Selenium and ffmpeg

This Python script allows you to capture and download video streams from a Twitter broadcast URL (or other platforms that use m3u8 for video streaming) using Selenium and ffmpeg. The script intercepts network requests to extract the m3u8 URL and uses ffmpeg to download the video.

## Features

- Capture m3u8 URLs from network traffic using Selenium and JavaScript interception.
- Automatically download video streams from m3u8 URLs using ffmpeg.
- Supports user-specific Chrome profiles for authentication if needed.

## Requirements

- Python 3.x
- Selenium
- ffmpeg
- Google Chrome (with a user profile for network requests)
- A Chrome WebDriver compatible with your browser version.

## Installation

1. Install the necessary Python dependencies:
    ```bash
    pip install selenium
    ```

2. Download and install [ffmpeg](https://ffmpeg.org/download.html).

3. Set up Selenium with the appropriate WebDriver:
   - Download the ChromeDriver version that matches your Google Chrome version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Make sure the `chromedriver` binary is in your system PATH or specify its path in the code.

4. Place the script in a folder and run it.

## Usage

1. Make sure you have Google Chrome installed and that you can access the user profile. The script uses the Chrome profile to capture network requests. Replace the `profile_path` with the correct path to your Chrome user profile.
   - On Windows, the default profile path is usually:
     ```
     C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data
     ```
   - Replace `<YourUsername>` with your actual Windows username.

2. Run the script:
    ```bash
    python script.py
    ```

3. Enter the Twitter broadcast URL when prompted, for example:
    ```
    https://x.com/AlArabiya/live
    ```

4. The script will capture the m3u8 URL and start downloading the video using ffmpeg.

## Notes

- The script intercepts m3u8 URLs from the browser's console logs. If no m3u8 URL is found, ensure the Twitter broadcast page has fully loaded and that the m3u8 stream is visible in network traffic.
- Make sure you have permission to download content from the broadcast you're trying to capture.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
