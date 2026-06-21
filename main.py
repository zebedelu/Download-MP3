from yt_dlp import YoutubeDL


url = input("Cole aqui sua url: ").strip()

opcoes = {
    "format": "bestaudio/best",
    "ffmpeg_location": r"C:\Users\User\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin",
    "noplaylist": True,
    "outtmpl": "%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

try:
    with YoutubeDL(opcoes) as ydl:
        info = ydl.extract_info(url, download=False)

        if info.get("_type") == "playlist":
            print("Essa URL parece ser de playlist/canal. Cole a URL de um video especifico.")
            raise SystemExit(1)

        print(info.get("title"))
        print(info.get("thumbnail"))
        ydl.download([url])
except Exception as erro:
    print("Nao foi possivel baixar/converter o audio.")
    print("Para gerar MP3, instale o FFmpeg e tente novamente.")
    print(f"Erro: {erro}")
