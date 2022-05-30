# Project Bill
Ciphers coded in different programming languages.

A1Z26 - Created in 09-18-2019.

Atbash - Created in 09-12-2019.

Caesar - Created in 09-17-2019.

Vigenère - Created in 09-18-2019.

## How to run/execute (Windows)
### Via Command Prompt
Locate the directory of `Bill.py` in command window and type `python Bill.py <insert argument here>`.

## How to run/execute (Linux)
### Via Terminal
Locate the directory of `Bill.py` in console and type `python Bill.py <insert argument here>`.

# Documentation
## Usage in Command Line
`python Bill.py [-h] [-v] [-a1z26 | -atbash | -caesar SHIFT | -vigenere KEY] [-e | -d] [-i INPUT FILE] [-o [OUTPUT FILE]]`

## Help
Calling `-h` or `--help` as an argument prompts the help.

## Version
Calling `-v` or `--version` as an argument prompts the version.

## Ciphers available
### A1Z26 Cipher
Calling `-a1z26` or `--a1z26` as the first argument uses the **A1Z26 Cipher**.

### Atbash Cipher
Calling `-atbash` or `--a1z26` as the first argument uses the **Atbash Cipher**.

### Caesar Cipher
Calling `-caesar SHIFT` or `--caesar SHIFT` as the first argument (along with the required argument for shift number) uses the **Caesar Cipher**.

### Vigenère Cipher
Calling `-vigenere KEY` or `--vigenere KEY` as the first argument (along with the required argument for keyword) uses the **Vigenère Cipher**.

## Text Conversion
### Encoding
Calling `-e` or `--encode` as the second argument encodes the input file data into the specified cipher.

### Decoding
Calling `-d` or `--decode` as the second argument decodes the input file data into the specified cipher.

## File input/output
## Note
The `INPUT FILE` and `OUTPUT FILE` must have a filename extension of `.txt` or none at all as the program can add the file extension.

### Input
Calling `-i INPUT FILE` or `--input INPUT FILE` as the third argument (along with the required argument for input file) reads the data (or text) inside.

### Output
Calling `-o [OUTPUT FILE]` or `--output [OUTPUT FILE]` as the third argument (along with the optional argument for output file) writes the processed data.
