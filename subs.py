import string


class CodeIt:
    """Class to hold the alphabets and manage the encodings."""

    def __init__(self):
        self.alphabet = string.ascii_letters + string.digits + " " #+ "\n"
        self.coded_alphabet: str = ""

    def create_coded_from_shift(self, _shift_value: int) -> None:
        """Shift the alphabet by the index given."""

        # Get the value to shift by

        # Create the alphabet

    def create_coded_from_phrase(self, _phrase: str) -> None:
        """Given a user-supplied phrase, create a coded alphabet."""

        # Get just individual letters

        # Create the full alphabet with no duplicates

    def create_coded_from_user_alphabet(self, new_alphabet: str) -> None:

        if len(self.alphabet) != len (new_alphabet):
            return
        for i, c in enumerate(new_alphabet):
            if c in new_alphabet[i+1:]:
                return
        self.coded_alphabet = new_alphabet



    def code_message(self, _user_message: str, _code_flag: bool) -> str:
        if _code_flag:
            alphabet_from = self.alphabet
            alphabet_to = self.coded_alphabet

        else:
            alphabet_from = self.coded_alphabet
            alphabet_to = self.alphabet

        return_message: str = ""
        for c in _user_message:
            idx = alphabet_from.find(c)
            # print(idx, alphabet_to)
            if idx == -1:
                return_message += c
                continue
            return_message += alphabet_to[idx]

        return return_message

    def code_multi_index_message(self, _user_message: str,
                                 _multi_index: str,
                                 _encode_flag: bool) -> str:
        """Encode with a multi-index based on the indeces of the phrase given"""

        alphabet_phrase = ""
        for c in _multi_index.strip():
            if c in self.alphabet:
                alphabet_phrase += c

        alphabets = []
        # Create the alphabets we will use based on the deduped phrase
        for c in alphabet_phrase:
            idx = self.alphabet.find(c)
            alphabets.append(self.alphabet[idx:] + self.alphabet[:idx])

        return_message = ""
        if _encode_flag:
            for i, c in enumerate(_user_message):
                current_alphabet = i % len(alphabets)
                letter_index = self.alphabet.find(c)
                if letter_index == -1:
                    return_message += c
                    continue
                coded_letter = alphabets[current_alphabet][letter_index]
                return_message += coded_letter
        else:
            for i, c in enumerate(_user_message):
                current_alphabet = i % len(alphabets)
                letter_index = alphabets[current_alphabet].find(c)
                if letter_index == -1:
                    return_message += c
                    continue
                coded_letter = self.alphabet[letter_index]
                return_message += coded_letter

        return return_message




