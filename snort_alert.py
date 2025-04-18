import requests
import time

logfile = '/var/log/snort/alert'
webhook_url = 'https://discord.com/api/webhooks/1362254034643456010/4PNp9WHj1XynjTSu-_PBBhCNQfCzXrltzY8YbUa_gImgUVNQZuzrFKXwc7vip9D8TPcR'

def send_discord_alert(message):
    data = {'content': message}
    try:
        requests.post(webhook_url, data=data)
    except Exception as e:
        print(f"Failed to send alert: {e}")

def tail_alerts(logfile):
    try:
        with open(logfile, 'r') as file:
            file.seek(0, 2)  # Go to the end of the file
            while True:
                line = file.readline()
                if not line:
                    time.sleep(1)
                    continue
                if '[**]' in line:
                    send_discord_alert(f"=¨ SNORT ALERT OPEN UP: {line.strip()}")
    except FileNotFoundError:
        print(f"Alert file not found: {logfile}")
    except Exception as e:
        print(f"Error reading alert file: {e}")

if __name__ == '__main__':
    tail_alerts(logfile)
