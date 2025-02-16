# DownPlaylistFull

O DownPlaylistFull foi criado para atender à necessidade de baixar todos os vídeos de uma playlist do YouTube de forma rápida, eficiente e com a mais alta qualidade possível. Atualmente, existem poucos sites ou projetos confiáveis ​​dedicados a isso, e é por isso que o DownPlaylistFull foi desenvolvido.

## Tecnologias usadas

| Nome | Versão |
|---------|---------|
| Python | 3.12.8 (ou qualquer versão acima) |
| ffmpeg | (versão mais recente) |
| yt-dlp | (versão mais recente) |
| browser-cookie3 | (versão mais recente) |
## Instalação

Antes de executar o script, você precisa instalar **Python**, **yt-dlp** e **FFmpeg**.

### Instalando yt-dlp

Para **Windows**:

```sh
pip install yt-dlp

```

Para **Linux**:

```sh
pip install yt-dlp

```
Para **Windows**:

```sh
pip install browser-cookie3

```

Para **Linux**:

```sh
pip install browser-cookie3

```
### Instalando FFmpeg

Para **Windows** (usando Winget):

```sh
winget install -e --id Gyan.FFmpeg

```

Para **Linux**:

```sh
sudo apt update && sudo apt install ffmpeg

```

## Uso

Primeiro, você precisa estar logado no YouTube no seu navegador. (Firefox ou Chrome baseados) para que o script possa acessar os cookies.

Depois de instalar todas as dependências, baixe ou copie o script [AQUI](https://github.com/DaviJoseMach/DownPlaylistFull/blob/main/down_playlist.py).

Execute o script usando o seguinte comando:

```sh
python your_script_name.py

```

Siga as instruções na tela para inserir o link da playlist do YouTube e a pasta onde os vídeos serão salvos.

### Recursos

- Baixa todos os vídeos (ou apenas os áudios) de uma playlist do YouTube.
- Garante a mais alta qualidade disponível (até 1080p com áudio).
- Usa **FFmpeg** para mesclar arquivos de vídeo e áudio perfeitamente.
- Funciona tanto no Windows quanto no Linux.

Aproveite os downloads de playlists do YouTube sem complicações com **DownPlaylistFull**! 🚀
