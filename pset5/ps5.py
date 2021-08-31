import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    # BE SURE TO change the value of the f constant to the complete path name for the file "story.txt"
    f = open("c:/Users/Fernanda-SSD/Desktop/Bill Gates/mit/w5/pset5/story.txt", "r")
    story = str(f.read())
    f.close()
    return story
# BE SURE TO change the value of the WORDLIST_FILENAME constant to the complete path name for the file "words.txt"
WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    # TO DO
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        cypher_dict = {}
        for i in lower_case:
            cypher_dict[i] = chr((ord(i)) + shift)
            if ord(cypher_dict[i]) > 122:
                cypher_dict[i] = chr((ord(cypher_dict[i]) % 122) + 96)
        for i in upper_case:
            cypher_dict[i] = chr((ord(i)) + shift)
            if ord(cypher_dict[i]) > 90:
                cypher_dict[i] = chr((ord(cypher_dict[i]) % 90) + 64)
        return cypher_dict

      
    # TO DO
    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        e_msg = ""
        cypher = self.build_shift_dict(shift)
        for letter in self.get_message_text():
            if letter not in cypher:
                e_msg = e_msg + letter
            else:
                for key in cypher:
                    if key == letter:
                        e_msg = e_msg + cypher[key]
        return e_msg

      
# TO DO
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, self.shift)
        self.message_text_encrypted = Message.apply_shift(self, self.shift)
        

# TO DO
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        n_words_best_shift = 0
        for shift in range (26):
            n_words_test_shift = 0
            decrypted_text_words = self.apply_shift(shift).split(' ')
            for word in decrypted_text_words:
                if is_word(self.get_valid_words(), word):
                    n_words_test_shift = n_words_test_shift + 1
            if n_words_test_shift > n_words_best_shift:
                n_words_best_shift = n_words_test_shift
                best_shift = shift
        tuple_decrypt = (best_shift, self.apply_shift(best_shift))
        return tuple_decrypt

      
# TO DO      
def decrypt_story():
    decrypt = CiphertextMessage(get_story_string())
    return decrypt.decrypt_message()

#Example test case (PlaintextMessage)
'''
plaintext = PlaintextMessage('woman loose twist pride enjoy what finger weed extra worship mild width accuse stamp rough tight off soap dear excess abroad arm window white difference influential meet strengthen hatred follow purple deserve deceive prison review', 12)
print('Output:', plaintext.get_message_text_encrypted())
'''
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('iaymz xaaeq fiuef bdupq qzvak itmf ruzsqd iqqp qjfdm iadetub yuxp iupft moogeq efmyb dagst fustf arr eamb pqmd qjoqee mndamp mdy iuzpai itufq purrqdqzoq uzrxgqzfumx yqqf efdqzsftqz tmfdqp raxxai bgdbxq pqeqdhq pqoquhq bdueaz dqhuqi')
print('Final Output:', ciphertext.decrypt_message())

print(decrypt_story())
