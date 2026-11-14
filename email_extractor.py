# CodeAlpha Python Task 3: Task Automation
# Extract all email addresses from a .txt file and save them to another file.

import os
import re

INPUT_FILE = "sample_input.txt"
OUTPUT_FILE = "extracted_emails.txt"

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(text):
    """Return a sorted list of unique email addresses found in text."""
    return sorted(set(re.findall(EMAIL_PATTERN, text)))


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: '{INPUT_FILE}' not found in this folder.")
        return

    with open(INPUT_FILE, "r") as f:
        text = f.read()

    emails = extract_emails(text)

    with open(OUTPUT_FILE, "w") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"Found {len(emails)} unique email address(es).")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
