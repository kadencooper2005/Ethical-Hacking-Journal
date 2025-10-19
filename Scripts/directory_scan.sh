#!/bin/bash

command_exists () {
    command -v "$1" >/dev/null 2>&1
}
# --- Sublist3r Domain Scanner ---
# This script prompts the user for a domain and performs a subdomain scan using Sublist3r.

# Function to check if a command exists
command_exists () {
  command -v "$1" >/dev/null 2>&1
}

# --- Main script ---
echo "--- Sublist3r Domain Scanner ---"

# Check if Sublist3r is installed and exit if not
if ! command_exists sublist3r; then
  echo "Error: Sublist3r is not installed or not in your PATH."
  echo "Please install it first. See script comments for instructions."
  exit 1
fi

# Prompt the user for the target domain
read -p "Enter the target domain (e.g., example.com): " domain

# Check if the domain is provided
if [ -z "$domain" ]; then
  echo "Error: No domain was entered. Exiting."
  exit 1
fi

# Create a directory for the scan results
output_dir="${domain}_subdomains"
mkdir -p "$output_dir"
echo "Created output directory: $output_dir"

# Define the output file path
output_file="$output_dir/${domain}_results.txt"

# Run the Sublist3r scan
echo "Starting Sublist3r scan for $domain..."
sublist3r -d "$domain" -o "$output_file"

# Check if the scan was successful
if [ $? -eq 0 ]; then
  echo "Scan finished successfully."
  echo "Results saved to: $output_file"
  echo "A total of $(wc -l < "$output_file") subdomains were found."
else
  echo "Sublist3r scan failed. Check for errors above."
  rmdir "$output_dir" # Clean up the empty directory on failure
fi
echo "--- Sublist3r Domain Scanner --- "

if ! command_exists sublist3r; then

fi

