# Secret Code Language - Coder & Decoder

A Python-based encryption and decryption utility that transforms plain text into a secure "Secret Code Language" using string manipulation and random noise generation.

## 📝 Problem Statement
The goal is to create a tool that allows two parties to communicate securely by converting English words into a coded format based on specific length-based rules.

### Encryption (Coding) Rules:
1. **If the word has 3 or more characters:**
   - Remove the first letter and move it to the end.
   - Add three random characters (noise) to the beginning and three random characters to the end.
2. **If the word has 1 or 2 characters:**
   - Simply reverse the string.
3. **If the word is empty:**
   - Notify the user that nothing was entered.

### Decryption (Decoding) Rules:
1. **If the word has 3 or more characters:**
   - Remove the 3 random noise characters from the start and the 3 noise characters from the end.
   - Take the last character of the remaining string and move it back to the front.
2. **If the word has 1 or 2 characters:**
   - Reverse it back to its original form.

---

## 📋 Requirements
* **Python Version:** Python 3.13 or higher (Required for `random.choices` keyword argument support).
* **Standard Libraries:** `random`, `string` (No external installations required).

---

## 🚀 How to Run
1. Ensure you have the correct Python version installed.
2. Clone this repository and navigate to the folder.
3. Run the script:
   ```bash
   python coder_decoder.py
   ```
 4. Follow the menu:
   - Type **'c'** to Code.
   - Type **'d'** to Decode.
   - Press **Enter** on the main menu to exit.

---


## 🛠️ Concepts Used
* **String Slicing:** Manipulating indices to move characters and strip noise.
* **Random Module:** Using `random.choices` with `k=3` for secure noise generation.
* **Loops:** Nested `while` loops for continuous user interaction and menu navigation.
* **Error Handling:** `try-except` block to catch and report unexpected issues.
* **User Input:** Handling dynamic input and case-insensitive commands.

---

## 👤 Author
* **Yuv Sharma** - [yuvsharma723](https://github.com/yuvsharma723)
