# YouTube Live HLS Proxy (Multi-Stream, Dockerized)

This project allows you to proxy one or more YouTube Live `.m3u8` HLS streams via static, local URLs like:

```
http://your-server:5055/live1.m3u8
http://your-server:5055/live2.m3u8
```

This is useful for Home Assistant, VLC, Kodi, or any IPTV/HLS-compatible player.

## ✅ Features

- Supports multiple YouTube Live streams
- Exposes fixed `.m3u8` URLs that refresh in the background
- Configurable via environment variables
- Refresh interval configurable via `CRON_INTERVAL`

## 🚀 Getting Started

### 1. Clone or Download

```bash
git clone https://github.com/your-username/youtube-live-hls-proxy.git
cd youtube-live-hls-proxy
```

### 2. Edit `docker-compose.yml`

Replace the YouTube URLs with your own.

### 3. Launch the proxy

```bash
docker compose up -d --build
```

### 4. Use the static `.m3u8` links

In VLC, Kodi, etc.

```
http://localhost:5055/live1.m3u8
http://localhost:5055/live2.m3u8
```

## 🛠 Advanced

- Change update interval via `CRON_INTERVAL`
- Add more streams by extending the env variables

MIT License