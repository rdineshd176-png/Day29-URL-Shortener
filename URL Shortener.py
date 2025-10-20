import pyshorteners
import pyperclip

def shorten_url():
    print("🔗 Welcome to the URL Shortener!")
    long_url = input("Enter the URL to shorten: ").strip()
    
    if not long_url.startswith(("http://", "https://")):
        long_url = "https://" + long_url  # Auto-fix missing protocol
    
    try:
        # Create a shortener object
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(long_url)
        
        # Copy to clipboard
        pyperclip.copy(short_url)
        
        print("\n✅ Shortened URL:", short_url)
        print("📋 The shortened link has been copied to your clipboard!")
    
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    shorten_url()
