Clone the repository (or just download the two files WordsFrequencyTextParser.py and textToParse.txt to the same folder).
Put the text that needs to be analyzed into textToParse.txt.
Launch WordsFrequencyTextParser.py
Safe to use.

### 📊 Example Output

The script produces a frequency table like this:

| WORD      | COUNT |
|-----------|-------|
| care      | 6972  |
| pentru    | 4320  |
| este      | 3844  |
| sunt      | 1876  |
| când      | 1665  |
| mine      | 1631  |
| dacă      | 1607  |
| asta      | 1506  |
| bine      | 1447  |
| poate     | 1336  |
| fost      | 1245  |
| mult      | 1234  |
| prin      | 1233  |
| trebuie   | 1206  |
| foarte    | 1179  |
| spus      | 1138  |
| avea      | 1123  |
| după      | 1095  |
| timp      | 1091  |
| nici      | 1062  |
| rnai      | 1062  |
| mama      | 1029  |
| eram      | 986   |
| într      | 958   |

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
