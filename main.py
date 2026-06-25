from yt_dlp import YoutubeDL
import os

# Vai verificar se o ffmpeg está instalado
ffmeg_instalado = not bool(os.system("ffmpeg -version 2>&1"))

if not ffmeg_instalado:
    print("Você precisa instalar o ffmpeg para prosseguir")
    print("Iremos executar esse comando para instalar:")
    print("- winget install Gyan.FFmpeg")
    userchoice = input("Gostaria de instalar? (y/N)").lower()
    if userchoice == "y":
        # Vai detectar se o sistema é Windows ou Linux
        if os.name == "nt":
            os.system("pip install -r requirements.txt")
            os.system("winget install Gyan.FFmpeg")
        else:
            os.system("pip3 install -r requirements.txt")
            os.system("sudo apt install ffmpeg")

    # Vai verificar se instalou corretamente
    ffmeg_instalado = not bool(os.system("ffmpeg -version"))
    if ffmeg_instalado:
        print("FFMPEG instalado com sucesso!")
    else:
        print("Erro ao baixar o FFMPEG...")

print("Baixe audios do youtube apenas com a URL")
url = input("Cole aqui sua url: ").strip()

opcoes = {
    "format": "bestaudio/best",
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

print("Vídeo instalado com sucesso!")