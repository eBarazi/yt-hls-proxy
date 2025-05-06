FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    cron \
    supervisor \
    && pip install yt-dlp flask requests waitress \
    && apt-get clean

WORKDIR /app
COPY . /app
RUN chmod +x /app/entrypoint.sh
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 5055
CMD ["/usr/bin/supervisord"]