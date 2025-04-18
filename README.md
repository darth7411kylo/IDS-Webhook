# Snort IDS + Discord Webhook Alerts #

This project uses Snort to detect suspicious network activity and a Python script to send real-time alerts to a Discord channel via a webhook.

## KEY FEATURES ##
- Real-time alerting from Snort
- Discord webhook integration using Python
- Custom rules for ICMP and overflow detection
- Tested with real-world PCAP files

## ⚠️ PCAP File Notice
The PCAP file used for testing is too large to upload to GitHub (over 100MB).  
You can use your own `.pcap` files or request the test file from me directly.

## Usage ##

### 1. Run Snort on a PCAP:
```bash
sudo snort -r yourfile.pcap -c /etc/snort/snort.conf -A fast
