ARG WORKER_PYTHON_VERSION=3.11
ARG WORKER_DEBIAN_VERSION=bookworm
ARG TWITCH_DOWNLOADER_CLI_VERSION=1.55.2
ARG FFMPEG_VERSION=7.1

FROM python:${WORKER_PYTHON_VERSION}-${WORKER_DEBIAN_VERSION}

WORKDIR /code

RUN wget -O /code/twitch-downloader-cli.zip https://github.com/lay295/TwitchDownloader/releases/download/${TWITCH_DOWNLOADER_CLI_VERSION}/TwitchDownloaderCLI-${TWITCH_DOWNLOADER_CLI_VERSION}-Linux-x64.zip

RUN unzip twitch-downloader-cli.zip -d /code/twitch-downloader-cli
# Twitch downloader at /code/twitch-downloader-cli/TwitchDownloaderCLI

RUN pip install --no-cache-dir --upgrade yt-dlp streamlink

#COPY --from=mwader/static-ffmpeg:7.1 /ffmpeg /code/ffmpeg/
#COPY --from=mwader/static-ffmpeg:7.1 /ffprobe /code/ffmpeg/
COPY --from=jrottenberg/ffmpeg:ffmpeg-${FFMPEG_VERSION}-ubuntu2404 /usr/share/fonts /usr/share/fonts
COPY --from=jrottenberg/ffmpeg:ffmpeg-${FFMPEG_VERSION}-ubuntu2404 /usr/share/fontconfig /usr/share/fontconfig
COPY --from=jrottenberg/ffmpeg:ffmpeg-${FFMPEG_VERSION}-ubuntu2404 /usr/bin/fc-* /usr/bin/
COPY --from=jrottenberg/ffmpeg:ffmpeg-${FFMPEG_VERSION}-ubuntu2404 /usr/bin/ffmpeg /usr/bin/
COPY --from=jrottenberg/ffmpeg:ffmpeg-${FFMPEG_VERSION}-ubuntu2404 /usr/bin/ffprobe /usr/bin/

COPY ./app /code/app

CMD ["python3", "app/main.py"]