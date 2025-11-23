🔎 WordsFrequencyTextParser (Safe Version)

This script reads a user-provided text file and extracts the most frequent Romanian words while filtering unsafe characters, large files, and binary/hidden content.
It securely processes the file and outputs the result to results_clean.txt.

📌 Features

Safe file reading (blocks huge or malformed files)

Unicode normalization (removes hidden/invisible characters)

Prevents regex DoS

Filters common stopwords (editable)

Saves only frequently repeated words (default: ≥10)

🚀 How to Use

Place your text file in the same folder as the script.
Example: textToParse.txt

Run the script:

python your_script_name.py


Check the output file:

results_clean.txt

⚙️ Optional Settings

Inside the script, you can modify:

Setting	Description
ROMANIAN_STOPWORDS	Add words you want to exclude
MIN_WORD_FREQUENCY	Minimum repetitions to include in results
MIN_WORD_LENGTH / MAX_WORD_LENGTH	Word length filtering
MAX_FILE_SIZE	Maximum allowed file size
📝 Notes

Only alphabetic Romanian characters are counted (ăîâșț included)

Case-insensitive counting

All unsafe or invisible Unicode characters are removed automatically
