import nltk
from nltk.corpus import cmudict, words
import random

arpabet_to_ipa = { # ARPAbet to IPA conversion dictionary
    "AA": "ɑ", "AE": "æ", "AH": "ʌ", "AO": "ɔ", "AW": "aʊ", "AY": "aɪ",
    "B": "b", "CH": "tʃ", "D": "d", "DH": "ð", "EH": "ɛ", "ER": "ɜr",
    "EY": "eɪ", "F": "f", "G": "ɡ", "HH": "h", "IH": "ɪ", "IY": "i",
    "JH": "dʒ", "K": "k", "L": "l", "M": "m", "N": "n", "NG": "ŋ",
    "OW": "oʊ", "OY": "ɔɪ", "P": "p", "R": "r", "S": "s", "SH": "ʃ",
    "T": "t", "TH": "θ", "UH": "ʊ", "UW": "u", "V": "v", "W": "w",
    "Y": "j", "Z": "z", "ZH": "ʒ",
    "0": "", "1": "", "2": ""  # Remove stress markers
}

vowels = {'AA', 'AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW'}

def init_nltk(): # Download necessary NLTK data
  try:
      arpabet = cmudict.dict()
  except LookupError:
      nltk.download('cmudict')
      arpabet = cmudict.dict()
  try:
      wrdz = words.words()
  except LookupError:
      nltk.download('words')
      wrdz = words.words()
  wrdz = set(wrdz)
  return arpabet, wrdz

def filter_arpabet(arpabet, english_words):
    # Filter the CMU Pronouncing Dictionary to include only common English words
    result = {}
    for word, pron in arpabet.items():
        if word in english_words:
            result[word] = pron
    return result

def init_dicts():
    arpabet, words = init_nltk()
    filtered_arpa = filter_arpabet(arpabet, words)
    return filtered_arpa, words

def convert_arpabet_to_ipa(arpabet_syllable):
    return ''.join(arpabet_to_ipa.get(phoneme.strip('012'), phoneme) for phoneme in arpabet_syllable)

def is_vowel(phoneme):
    if not phoneme:
        return False
    this_phon = phoneme.strip('012')
    return this_phon in vowels

def is_consonant(phoneme):
    return phoneme and not is_vowel(phoneme)

def is_vowel_or_consonant(current_syllable):
    vowel = False
    consonant = False
    for p in current_syllable:
        thing = p.strip('012')
        if thing in vowels:
            vowel = True
        else:
            consonant = True
    return vowel, consonant

def has_vowel(current_syllable):
    vowel, consonant = is_vowel_or_consonant(current_syllable)
    return vowel

def last_syllable_ends_with_vowel(syllables):
    if len(syllables) < 1:
        return False
    last_syllable = syllables[-1]
    last_bit = last_syllable[-1]
    return is_vowel(last_bit)

def syllabify(pronunciation):
    syllables = []
    my_syllable = []

    for i, phoneme in enumerate(pronunciation):
        this_phon = phoneme
        next_phon = None
        if i + 1 < len(pronunciation):
            next_phon = pronunciation[i + 1].strip('012')
        if is_vowel(this_phon):
            if my_syllable:
                vowel, consonant = is_vowel_or_consonant(my_syllable)
                if consonant:
                    syllables.append(my_syllable + [phoneme])
                    my_syllable = []
                else:
                    syllables.append(my_syllable)
                    my_syllable = [phoneme]
            else:
                my_syllable.append(phoneme)
        else: # phoneme is a consonant
            if not next_phon: # end of the list, append this consonant to the last syllable
                if len(syllables) > 0:
                    syllables[-1].append(phoneme)
                else:
                    syllables.append(my_syllable + [phoneme])
                my_syllable = []
                break
            if is_consonant(next_phon):
                # two consonants in a row, if last syllable ends in a vowel, append this one and move on
                if last_syllable_ends_with_vowel(syllables):
                    syllables[-1].append(phoneme)
                    my_syllable = []
                    continue
            if my_syllable:
                if has_vowel(my_syllable) \
                  and next_phon and (next_phon in vowels) \
                  and (i + 1 < len(pronunciation)):
                    syllables.append(my_syllable)
                    my_syllable = [phoneme]
                else:
                  my_syllable.append(phoneme)
            else:
                my_syllable.append(phoneme)

    if my_syllable:
        vowel, consonant = is_vowel_or_consonant(my_syllable)
        if consonant:
            syllables[-1].extend(my_syllable)
        else:
            syllables.append(my_syllable)

    final_syllables = []
    for syllable in syllables:
        arp = convert_arpabet_to_ipa(syllable)
        final_syllables.append(arp)
    return final_syllables, syllables

def update_dict_list(d, key, value):
  if key not in d:
    d[key] = []
  l = d[key]
  l.append(value)

def main():
    arpabet, words = init_nltk()
    #arpabet, english_words = init_dicts()
    word_to_syllables = {}
    f = open("output-arpabet.txt", 'w')
    words = list(words)
    random.shuffle(words)
    for word in words:
      word = word.lower()
      if word not in arpabet:
          s = f"Word: '{word}' not found in arpabet"
          f.write(s + "\n")
          continue
      pronunciations = arpabet[word]
      for pronunciation in pronunciations:
          syllables, arpabet_syllables = syllabify(pronunciation)
          #hyphenated = hyphenate_word(word, syllables)
          update_dict_list(word_to_syllables, word, syllables)
          s = f"Word: {word}, Syllables: {syllables}, Arpabet: {arpabet_syllables}"
          f.write(s + "\n")
    f.close()

if __name__ == '__main__':
    main()