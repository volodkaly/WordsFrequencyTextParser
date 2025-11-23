import re
import os
import unicodedata
from collections import Counter

# --- Stopwords placeholder (safe and editable) ---
ROMANIAN_STOPWORDS = set()

# --- Safety limits ---
MAX_FILE_SIZE = 5 * 1024 * 1024     # 5 MB
MAX_WORD_LENGTH = 40
MIN_WORD_LENGTH = 4
MIN_WORD_FREQUENCY = 10

def sanitize_text(text: str) -> str:
    """Normalize text and remove unsafe characters."""
    text = unicodedata.normalize("NFKC", text)
    text = "".join(ch for ch in text if ch.isprintable())
    text = re.sub(r"[\u200B-\u200F\u202A-\u202E]", "", text)
    return text

def safe_read_file(path: str) -> str:
    """Read file safely with protection against large/binary files."""
    if not os.path.exists(path):
        raise FileNotFoundError("File not found.")

    if os.path.getsize(path) > MAX_FILE_SIZE:
        raise ValueError("File is too large.")

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def analyze_romanian_text_advanced(filename: str):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, os.path.basename(filename))
    output_path = os.path.join(script_dir, 'results_clean.txt')

    try:
        print(f"Processing file: {filename} ...")

        raw_text = safe_read_file(input_path)
        text = sanitize_text(raw_text)

        words = re.findall(r"[a-zA-ZăîâșțĂÎÂȘȚ]+", text.lower())

        filtered_words = [
            w for w in words
            if MIN_WORD_LENGTH <= len(w) <= MAX_WORD_LENGTH and w not in ROMANIAN_STOPWORDS
        ]

        word_counts = Counter(filtered_words)

        with open(output_path, "w", encoding="utf-8") as out:
            out.write(f"{'WORD':<20} | {'COUNT'}\n")
            out.write("-" * 32 + "\n")

            saved = 0
            for word, count in word_counts.most_common():
                if count < MIN_WORD_FREQUENCY:
                    break
                out.write(f"{word:<20} | {count}\n")
                saved += 1

        print(f"Done. Found {saved} words (>= {MIN_WORD_FREQUENCY}).")
        print("Saved to: results_clean.txt")

    except Exception as e:
        print(f"Error: {e}")

# --- Run ---
analyze_romanian_text_advanced("textToParse.txt")
