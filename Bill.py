"""Project Bill Documentation.

This program uses command-line to perform encryption and decryption.

Example
-------

    $ python Bill.py -atbash -e -i example

Where `-atbash` is the cipher, `-e` is the argument for encoding, `-i example` 
is the location of the input file, i.e. 'example.txt'.
"""

from abc import ABC, abstractmethod
import argparse

class Cipher(ABC):
    """Abstract base class for which new classes are based."""

    def __init__(self, text: list) -> None:
        """Docstring for the __init__ method.

        Paramaters
        ----------
        text : list(list(str))
            Nested list that holds the input file data.
        """
        self.text = text

    def to_upper(self) -> list:
        """Method for converting string of data into UPPERCASE.

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        result = []
        for line in self.text:
            lines = []
            for string in line:
                lines.append(string.upper())
            result.append(lines)
        return result
    
    def to_lower(self) -> list:
        """Method for converting string of data into lowercase.

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        result = []
        for line in self.text:
            lines = []
            for string in line:
                lines.append(string.lower())
            result.append(lines)
        return result
    
    @abstractmethod
    def encode(self) -> None:
        pass

    @abstractmethod
    def decode(self) -> None:
        pass

class A1Z26(Cipher):
    """A1Z26 cipher is a substitution cipher that replaces the letters in the
    alphabet into numbers (A = 1, B = 2, ..., Z = 26).
    
    Notes
    -----
    A1Z26 cipher was used in Gravity Falls from Episodes 14 to 19.
    """

    def __init__(self, text: list) -> None:
        """Docstring for the __init__ method.

        Paramaters
        ----------
        text : list(list(str))
            Nested list that holds the input file data.

        Notes
        -----
        Calls the __init__ method from abstract class Cipher.
        """
        super().__init__(text)

    def encode(self) -> list:
        """Overrides abstract method encode(). encode() encrypts data in A1Z26
        cipher.

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        self.text = self.to_upper() # convert to uppercase
        # self.to_lower() # convert to lowercase
        result = []
        for lines in self.text:
            line = []
            for words in lines:
                word = []
                for char in words:
                    if char.isalpha():
                        if char.isupper():
                            word.append(
                                str(ord(char) % 65 + 1).zfill(2)
                            )
                        else:
                            word.append(
                                str(ord(char) % 97 + 1).zfill(2)
                            )
                line.append("-".join(word))
            result.append(line)
        return result

    def decode(self) -> list:
        """Overrides abstract method decode(). decode() decrypts data in A1Z26
        cipher.

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        result = []
        for lines in self.text:
            line = []
            for words in lines:
                chars = words.split("-")
                word = []
                for char in chars:
                    # only alphabetic numbers
                    word.append(chr(int(char) + 64))
                    # word.append(chr(int(char) + 96))
                line.append("".join(word))
            result.append(" ".join(line))
        return result

class Atbash(Cipher):
    """Atbash cipher is a substitution cipher that replaces the letters in the
    alphabet in reverse (A = Z, B = Y, ..., Z = A).
    
    Notes
    -----
    Atbash cipher was used in Gravity Falls from Episodes 7 to 13.
    """

    def __init__(self, text: list) -> None:
        """Docstring for the __init__ method.

        Paramaters
        ----------
        text : list(list(str))
            Nested list that holds the input file data.

        Notes
        -----
        Calls the __init__ method from abstract class Cipher.
        """
        super().__init__(text)
    
    def encode(self) -> list:
        """Overrides abstract method encode(). encode() encrypts data in Atbash
        cipher.

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        # no need to convert to uppercase or lowercase
        result = []
        for lines in self.text:
            line = []
            for words in lines:
                word = []
                for char in words:
                    if char.isupper():
                        word.append(
                            chr(ord("Z") - ord(char) + ord("A"))
                        )
                    elif char.islower():
                        word.append(
                            chr(ord("z") - ord(char) + ord("a"))
                        )
                    else:
                        word.append(char)
                line.append("".join(word))
            result.append(line)
        return result

    def decode(self) -> list:
        """Overrides abstract method decode(). decode() decrypts data in Atbash
        cipher.

        Returns
        -------
        list(list(str))
            Nested list of strings.

        Notes
        -----
        Encoding in Atbash is the same as decoding.
        """
        return self.encode()

class Caesar(Cipher):
    """Caesar cipher is a substitution cipher where each letter is replaced by 
    a fixed number of positions within the alphabet. With right shift of 3, the
    alphabet moves right such that A = D, B = E, ..., Z = C.
    
    Notes
    -----
    Caesar cipher was used in Gravity Falls from Episodes 1 to 6.
    """

    def __init__(self, text: list) -> None:
        """Docstring for the __init__ method.

        Paramaters
        ----------
        text : list(list(str))
            Nested list that holds the input file data.

        Notes
        -----
        Calls the __init__ method from abstract class Cipher.
        """
        super().__init__(text)
    
    def encode(self, shift: int) -> list:
        """Overrides abstract method encode(). encode() encrypts data in Caesar
        cipher.

        Parameters
        ----------
        shift : int
            Integer used to shift letters in the alphabet.

        Example
        -------
            [["Hello", "World"]] with shift 3 becomes [["Khoor", "Zruog"]].

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        result = []
        for lines in self.text:
            line = []
            for words in lines:
                word = []
                for char in words:
                    if char.isalpha():
                        if char.isupper():
                            word.append(
                                chr((ord(char) + shift - 65) % 26 + 65)
                            )
                        else:
                            word.append(
                                chr((ord(char) + shift - 97) % 26 + 97)
                            )
                    else:
                        word.append(char)
                line.append("".join(word))
            result.append(line)
        return result
    
    def decode(self, shift: int) -> list:
        """Overrides abstract method decode(). decode() decrypts data in Caesar
        cipher.

        Parameters
        ----------
        shift : int
            Integer used to shift letters in the alphabet.

        Example
        -------
            [["Khoor", "Zruog"]] with shift 3 becomes [["Hello", "World"]].

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        result = []
        for lines in self.text:
            line = []
            for words in lines:
                word = []
                for char in words:
                    if char.isalpha():
                        if char.isupper():
                            word.append(
                                chr((ord(char) + shift - 65) % 26 + 65)
                            )
                        else:
                            word.append(
                                chr((ord(char) + shift - 97) % 26 + 97)
                            )
                    else:
                        word.append(char)
                line.append("".join(word))
            result.append(line)
        return result

class Vigenère(Cipher):
    """Vigenère cipher is a substitution cipher that encrypts text using some 
    series of Caesar ciphers based on the letters of the given keyword.

    Example
    -------
    Given the plaintext "HELLO WORLD" and the keyword "TEST", the encrypted
    result would be "AIDEH AGKEH". Decrypting it with the same keyword reverts 
    the ciphertext back into plaintext.

    Notes
    -----
    Vigenère cipher was used in Gravity Falls from Episodes 21 to 40.
    """

    def __init__(self, text: list) -> None:
        """Docstring for the __init__ method.

        Paramaters
        ----------
        text : list(list(str))
            Nested list that holds the input file data.

        Notes
        -----
        Calls the __init__ method from abstract class Cipher.
        """
        super().__init__(text)
    
    def encode_key(self, key: str) -> list:
        """Encodes plaintext (and ciphertext) into lengths of keywords.

        Example
        -------
        [['HELLO', 'WORLD']] with keyword "TEST" becomes [['TESTT', 'ESTTE']].

        Parameters
        ----------
        key : str
            The keyword used for matching plaintext.

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        # convert key to either uppercase or lowercase
        key = key.upper()
        # key = key.lower()
        result = []
        total = 0
        for lines in self.text:
            line = []
            for words in lines:
                word = []
                for j in range(len(words)):
                    if words[j].isalpha():
                        word.append(key[total % len(key)])
                    else:
                        word.append(words[j])
                    total += 1
                line.append("".join(word))
            result.append(line)
        return result
    
    def encode(self, key: str) -> list:
        """Overrides abstract method encode(). encode() encrypts data in
        Vigenère cipher.

        Example
        -------
        [['HELLO', 'WORLD']] with keyword "TEST" becomes [['AIDEH', 'AGKEH']].

        Parameters
        ----------
        key : str
            The keyword used to encrypt plaintext.

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        # convert text to either uppercase or lowercase
        self.text = self.to_upper()
        # self.text = self.to_lower()
        result = []
        # match keyword to plaintext
        keyword = self.encode_key(key.upper())
        # format: ([lines_a go here], [lines_b go here])
        for lines_a, lines_b in zip(self.text, keyword):
            line = []
            # format: ([words_a go here], [words_b go here])
            for words_a, words_b in zip(lines_a, lines_b):
                word = []
                # format: ([char_a go here], [char_b go here])
                for char_a, char_b in zip(words_a, words_b):
                    if char_a.isalpha():
                        # cipher = (plaintext + keyword) mod 26
                        if char_a.isupper():
                            word.append(
                                chr((ord(char_a) + ord(char_b)) % 26 + 65)
                            )
                        else:
                            word.append(
                                chr((ord(char_a) + ord(char_b)) % 26 + 97)
                            )
                    else:
                        word.append(char_a)
                line.append("".join(word))
            result.append(line)
        return result
    
    def decode(self, key: str) -> list:
        """Overrides abstract method decode(). decode() decrypts data in
        Vigenère cipher.

        Example
        -------
        [['AIDEH', 'AGKEH']] with keyword "TEST" becomes [['HELLO', 'WORLD']].

        Parameters
        ----------
        key : str
            The keyword used to decrypt ciphertext.

        Returns
        -------
        list(list(str))
            Nested list of strings.
        """
        # convert text to either uppercase or lowercase
        self.text = self.to_upper()
        # self.text = self.to_lower()
        result = []
        # match keyword to ciphertext
        keyword = self.encode_key(key.upper())
        for lines_a, lines_b in zip(self.text, keyword):
            line = []
            for words_a, words_b in zip(lines_a, lines_b):
                word = []
                for char_a, char_b in zip(words_a, words_b):
                    if char_a.isalpha():
                        # plaintext = (cipher - keyword) mod 26
                        # "+ 26" prevents negative dividend
                        if char_a.isupper():
                            word.append(
                                chr((ord(char_a) - ord(char_b) + 26) % 26 + 65)
                            )
                        else:
                            word.append(
                                chr((ord(char_a) - ord(char_b) + 26) % 26 + 97)
                            )
                    else:
                        word.append(char_a)
                line.append("".join(word))
            result.append(line)
        return result

def init_parser() -> argparse.ArgumentParser():
    """Function to initialize the argument parser for Python.

    Returns
    -------
    argparse.ArgumentParser()
        Argument parser used for command-line execution.
    """
    # main parser
    parser = argparse.ArgumentParser(
        prog="Cipher Parser",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=f"""
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡶⢶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣇⣸⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢩⡿⢿⡍⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣥⣤⣤⣬⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠋⠁⢰⡆⠈⠙⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢀⣾⠟⣷⣄⠀⠸⠇⠀⣠⣾⠻⣷⡀⠀⠀⠀⠀⠀⠀
                ⢀⡀⠀⠀⠀⢠⣾⠋⠀⠀⠙⠛⠿⠿⠛⠋⠀⠀⠙⣷⡄⠀⠀⠀⢀⡀
                ⠈⠻⣦⣤⣤⣿⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣤⣤⣴⠟⠁
                ⠀⠀⠀⣰⣿⣉⣉⣉⣉⣹⣏⣉⣉⣉⣉⣹⣏⣉⣉⣉⣉⣿⣆⠀⠀⠀
                ⠀⠀⣴⡟⠉⢹⣿⠉⠉⠉⠉⠉⢻⡟⠉⠉⠉⠉⠉⣿⡏⠉⢻⣦⠀⠀
                ⠀⠐⠛⠛⠛⠛⠛⠛⢻⣿⠛⠛⠛⠛⠛⠛⠻⣿⠛⠛⠛⠛⠛⠛⠂⠀
                ⠀⠀⠀⠀⠀⠀⣤⣤⣸⡏⠀⠀⠀⠀⠀⠀⠀⣿⣤⣤⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠈⠉⠙⠁⠀⠀⠀⠀⠀⠀⠀⠙⠉⠁⠀⠀⠀⠀⠀⠀
Project Bill uses the 4 ciphers used in the show Gravity Falls.
Bill Cipher Art taken from 'https://emojicombos.com/bill-cipher-text-art'.""",
    )
    # display version
    parser.add_argument("-v", "--version",
                        action="version",
                        version=f'{parser.prog} v1.2')
    # group for ciphers
    cipher_available = parser.add_argument_group("Ciphers Available")
    cipher = cipher_available.add_mutually_exclusive_group()
    cipher.add_argument("-a1z26", "--a1z26",
                        action="store_true",
                        help="A1Z26 Cipher",
                        dest="a1z26")
    cipher.add_argument("-atbash", "--atbash",
                        action="store_true",
                        help="Atbash Cipher",
                        dest="atbash")
    cipher.add_argument("-caesar", "--caesar",
                        type=int,
                        help="Caesar Cipher, where SHIFT is the shift number",
                        metavar="SHIFT",
                        dest="shift")
    cipher.add_argument("-vigenere", "--vigenere",
                        type=str,
                        help="Vigenère Cipher, where KEY is the keyword",
                        metavar="KEY",
                        dest="key")
    # group for encryption/decryption
    text_conversion = parser.add_argument_group("Text Conversion")
    coding = text_conversion.add_mutually_exclusive_group()
    coding.add_argument("-e", "--encode",
                        action="store_true",
                        help="Encode plaintext",
                        dest="encode")
    coding.add_argument("-d", "--decode",
                        action="store_true",
                        help="Decode ciphertext",
                        dest="decode")
    # group for i/o
    file_handling = parser.add_argument_group("File Handling")
    file_handling.add_argument("-i", "--input",
                               help="Input file in *.txt",
                               metavar="INPUT FILE",
                               dest="infile")
    file_handling.add_argument("-o", "--output",
                               nargs="?",
                               help="Output file in *_out.txt",
                               metavar="OUTPUT FILE",
                               dest="outfile")
    return parser

def main() -> None:
    """Function to call main() for Python."""
    # initialize parser
    parser = init_parser()

    # parse arguments from command line
    args = parser.parse_args()

    # no arguments passed
    if not any(vars(args).values()):
        parser.print_help()
        parser.exit()

    # input data
    in_data = []

    # check if infile has no filename extension or uses *.txt
    try:
        if args.infile.split(".")[1].lower() == "txt":
            pass
        else:
            raise argparse.ArgumentTypeError(
                "Input filename extension must be *.txt or none")
    except IndexError:
        # add *.txt on infile
        args.infile += ".txt"

    # split in_data into lists
    with open(args.infile, mode='r', encoding='utf-8') as infile:
        # format: [['line 1 word 1', 'line 1 word 2'], ['line 2 word 1']]
        in_data = [j.split(" ") for j in [i.strip("\n") for i in infile]]

    # output data
    out_data = []

    # encoding data or decoding data
    # ternary operator for one line assignment of out_data
    if args.a1z26:
        process = A1Z26(in_data)
        out_data = process.encode() if args.encode else process.decode()
    elif args.atbash:
        process = Atbash(in_data)
        out_data = process.encode() if args.encode else process.decode()
    elif args.shift is not None:
        process = Caesar(in_data)
        out_data = process.encode(args.shift) if args.encode \
            else process.decode(args.shift)
    elif args.key is not None:
        process = Vigenère(in_data)
        out_data = process.encode(args.key) if args.encode \
            else process.decode(args.key)

    # check if outfile has no filename extension or uses *.txt
    try:
        if args.outfile is not None:
            if args.outfile.split(".")[1].lower() == "txt":
                pass
            else:
                raise argparse.ArgumentTypeError(
                    "Output filename extension must be *.txt or none")
        else:
            # rename outfile to infile + '_out.txt' as outfile is empty
            args.outfile = args.infile.split(".")[0] + "_out.txt"
    except IndexError:
        # add *.txt on infile
        args.outfile += ".txt"

    # write data
    with open(args.outfile, mode='w', encoding='utf-8') as outfile:
        for lines in out_data:
            if args.encode or args.decode == "atbash":
                line = " ".join(lines)
            elif args.decode == "a1z26":
                line = "".join(lines)
            else:
                line = " ".join(lines)

            if lines != out_data[-1]:
                outfile.writelines(line + '\n')
            else:
                outfile.writelines(line)

# runs program in command line
if __name__ == "__main__":
    main()