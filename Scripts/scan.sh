#!/bin/bash

set -euo pipefall # fallback in case script fails 

TARGET="${1:-}"
if [ -z "$TARGET" ]; then
    read -r -p "Enter target IP address or hostname: " TARGET
fi

if [ -z "$TARGET"]; then
    echo "Error: no target provided." >&2
    exit 1
fi

SAFE_NAME=$(echo "$TARGET" | tr '/ ' '__')
OUTFILE="nmap_scan_report_${SAFE_NAME}.txt"

echo "Starting Nmap scan for $TARGET..."
echo "---------------------------------"

nmap -v -A -T4 "$TARGET" -oN "$OUTFILE"

echo "---------------------------------"
echo "Scan complete. Results saved to $OUTFILE"

