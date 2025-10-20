This project is part of my 100 Days, 100 Python Projects challenge.

🎯 Goal

Create a simple URL Shortener App that converts long URLs into short, easy-to-share links instantly using the pyshorteners library.

🧠 How It Works

The user enters a long URL.

The app validates the URL (adds https:// if missing).

It uses the pyshorteners library to generate a TinyURL-based short link.

The shortened link is displayed and automatically copied to the clipboard.

🧩 Features

✂️ Converts long URLs into compact short links.

📋 Automatically copies the shortened URL to clipboard.

🚫 Handles missing protocols or invalid links gracefully.

⚡ Super quick and simple to use in the terminal.

🛠️ Tech Used

Python 3

pyshorteners library

pyperclip library

🚀 How to Run

Install the required libraries:

pip install pyshorteners pyperclip


Run the Python file:

python url_shortener.py


Enter a long URL and get a shortened one instantly!

🧾 Example Output
🔗 Welcome to the URL Shortener!
Enter the URL to shorten: https://www.example.com/this-is-a-very-long-url

✅ Shortened URL: https://tinyurl.com/y5example
📋 The shortened link has been copied to your clipboard!
