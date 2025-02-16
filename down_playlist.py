import yt_dlp
import os
import browser_cookie3

def detectar_navegador_youtube():
    try:
        cj = browser_cookie3.chrome()
        if any("youtube.com" in cookie.domain for cookie in cj):
            return 'chrome'
    except Exception:
        pass

    try:
        cj = browser_cookie3.firefox()
        if any("youtube.com" in cookie.domain for cookie in cj):
            return 'firefox'
    except Exception:
        pass

    return None

navegador = detectar_navegador_youtube()
if navegador:
    print(f"Browser detectado para cookies: {navegador}")
else:
    print("Nenhum cookie do YouTube foi detectado automaticamente.")
    navegador = input("Digite o navegador (chrome/firefox): ").strip().lower()

playlist_url = input("Digite o link da playlist: ")
output_folder = input("Digite o caminho da pasta onde os arquivos serão salvos: ")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

audio_only = input("Deseja baixar apenas o áudio? (s/n): ").strip().lower() == 's'

if audio_only:
    ydl_opts = {
        'ignoreerrors': True,
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'cookies_from_browser': navegador,
        'user_agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/115.0.0.0 Safari/537.36'
        ),
        'noplaylist': False,
    }
else:
    ydl_opts = {
        'ignoreerrors': True,
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'cookies_from_browser': navegador,
        'user_agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/115.0.0.0 Safari/537.36'
        ),
        'noplaylist': False,
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print("\n🎉 Download concluído!")
