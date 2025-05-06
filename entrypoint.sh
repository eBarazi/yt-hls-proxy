#!/bin/bash

CRON_TIME="${CRON_INTERVAL:-0 */6 * * *}"
echo "$CRON_TIME python3 /app/fetch_url.py >> /var/log/cronjob.log 2>&1" > /etc/cron.d/yt-job
chmod 0644 /etc/cron.d/yt-job
crontab /etc/cron.d/yt-job

echo "[entrypoint] Running initial fetch"
python3 /app/fetch_url.py