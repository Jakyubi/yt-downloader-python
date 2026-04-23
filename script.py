import yt_dlp
import os

def download(url, mode, quality="best", dir="downloaded"):

    current_dir = os.getcwd()
    ydl_opts = {
        "outtmpl": f"{dir}/%(title)s.%(ext)s",
        "ffmpeg_location": current_dir,
    }

    if mode == "v":
        if quality.lower() == "best":
            format_str = "bestvideo+bestaudio/best"
        else:
            format_str = f"bestvideo[height<={quality}]+bestaudio/best[height<={quality}]"
        ydl_opts.update({
            "format": format_str,
            "merge_output_format": "mp4",
        })

    elif mode == "a":
        ydl_opts.update({
            "format": "bestaudio[ext=m4a]/bestaudio/best",
            "postprocessors": [{
                "key" : "FFmpegExtractAudio",
                "preferredcodec": "m4a",
            }],
        })
    else:
        print("Invalid choice (v/a)")
        return
    print("\nDownloading started.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nOK. File saved in: {dir}")
    except yt_dlp.utils.DownloadError as e:
        print(f"\nERROR while downloading. INFO:\n{e}")
    except Exception as e:
        print(f"\nERROR: {e}")

if __name__ == "__main__":
    print("--- YouTube Downloader ---")
    while True:
        link = input("Paste YouTube link: ").strip()
        if link.lower() == 'exit':
            break
        
        while True:
            choice = input("What to download? video (v) / audio (a): ").lower().strip()
            if choice in ["v", "a"]:
                break
            print("Invalid choice (v/a)")

        if choice == "v":
            quality = input("Choose video quality (1080, 720, 480 etc. or 'best'): ").strip()
            if not quality:
                quality = "best"
        else:
            quality = "best"

        download(link, choice, quality)