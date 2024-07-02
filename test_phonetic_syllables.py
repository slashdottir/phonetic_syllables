import unittest
from phonetic_syllables import syllabify, init_dicts, init_nltk

class TestSyllabify(unittest.TestCase):

  def test_some_words(self):
    word = 'ace'
    arpabet_pronunciation = ['EY1', 'S'] # arpabet[word]
    expect = ['eɪs']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'accumulatively'
    arpabet_pronunciation = ['AH0', 'K', 'Y', 'UW1', 'M', 'Y', 'AH0', 'L', 'EY2', 'T', 'IH0', 'V', 'L', 'IY0'] # arpabet[word]
    expect = ['ʌk', 'jum', 'jʌ', 'leɪ', 'tɪv', 'li']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'blastoderm'
    arpabet_pronunciation = ['B', 'L', 'AE1', 'S', 'T', 'AH0', 'D', 'ER0', 'M'] # arpabet[word]
    expect = ['blæs', 'tʌ', 'dɜrm']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'barbarism'
    arpabet_pronunciation = ['B', 'AA1', 'R', 'B', 'ER0', 'IH2', 'Z', 'AH0', 'M'] # arpabet[word]
    expect = ['bɑr', 'bɜr', 'ɪ', 'zʌm']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'iridescent'
    arpabet_pronunciation = ['IH2', 'R', 'AH0', 'D', 'EH1', 'S', 'AH0', 'N', 'T'] #arpabet[word]
    expect = ['ɪ', 'rʌ', 'dɛ', 'sʌnt'] #
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'asbestosis'
    arpabet_pronunciation = ['AE2', 'S', 'B', 'EH2', 'S', 'T', 'OW1', 'S', 'AH0', 'S'] # arpabet[word]
    expect = ['æs', 'bɛs', 'toʊ', 'sʌs'] # would prefer un-in-tres-ting, but ok I guess
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'uninteresting'
    arpabet_pronunciation = ['AH0', 'N', 'IH1', 'N', 'T', 'R', 'AH0', 'S', 'T', 'IH0', 'NG'] # arpabet[word]
    expect = ['ʌ', 'nɪn', 'trʌs', 'tɪŋ'] # would prefer un-in-tres-ting, but ok I guess
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'truncheon'
    arpabet_pronunciation = ['T', 'R', 'AH1', 'N', 'CH', 'IH0', 'N'] # arpabet[word]
    expect = ['trʌn', 'tʃɪn'] #
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'screened'
    arpabet_pronunciation = ['S', 'K', 'R', 'IY1', 'N', 'D'] # arpabet[word]
    expect = ['skrind'] # would prefer a-de-kwat-li, but it's fine
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'marketable'
    arpabet_pronunciation = ['M', 'AA1', 'R', 'K', 'AH0', 'T', 'AH0', 'B', 'AH0', 'L'] # arpabet[word]
    expect = ['mɑr', 'kʌ', 'tʌ', 'bʌl']# would prefer a-de-kwat-li, but it's fine
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'adequately'
    arpabet_pronunciation = ['AE1', 'D', 'AH0', 'K', 'W', 'AH0', 'T', 'L', 'IY0'] # arpabet[word]
    expect = ['æ', 'dʌk', 'wʌt', 'li'] # would prefer a-de-kwat-li, but it's fine
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'whichever'
    arpabet_pronunciation = ['W', 'IH0', 'CH', 'EH1', 'V', 'ER0'] # arpabet[word]
    expect = ['wɪ', 'tʃɛ', 'vɜr']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'ingenious'
    arpabet_pronunciation = ['IH0', 'N', 'JH', 'IY1', 'N', 'Y', 'AH0', 'S'] # arpabet[word]
    expect = ['ɪn', 'dʒin', 'jʌs']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'mostly'
    arpabet_pronunciation = ['M', 'OW1', 'S', 'T', 'L', 'IY0'] # arpabet[word]
    expect = ['moʊs', 'tli']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'propane'
    arpabet_pronunciation = ['P', 'R', 'OW1', 'P', 'EY2', 'N'] # arpabet[word]
    expect = ['proʊ', 'peɪn']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'jamb'
    arpabet_pronunciation = ['JH', 'AE1', 'M'] # arpabet[word]
    expect = ['dʒæm']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'pettiness'
    arpabet_pronunciation = ['P', 'EH1', 'T', 'IY0', 'N', 'AH0', 'S'] # arpabet[word]
    expect = ['pɛ', 'ti', 'nʌs']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'permutation'
    arpabet_pronunciation = ['P', 'ER2', 'M', 'Y', 'UW0', 'T', 'EY1', 'SH', 'AH0', 'N'] # arpabet[word]
    expect = ['pɜrm', 'ju', 'teɪ', 'ʃʌn']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'recordable'
    arpabet_pronunciation = ['R', 'IH0', 'K', 'AO1', 'R', 'D', 'AH0', 'B', 'AH0', 'L'] # arpabet[word]
    expect = ['rɪ', 'kɔr', 'dʌ', 'bʌl']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'fork'
    arpabet_pronunciation = ['F', 'AO1', 'R', 'K']
    expect = ['fɔrk']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

    word = 'attention'
    arpabet_pronunciation = ['AH0', 'T', 'EH1', 'N', 'SH', 'AH0', 'N']
    expect = ['ʌ', 'tɛn', 'ʃʌn']
    syllables, _ = syllabify(arpabet_pronunciation)
    self.assertEqual(syllables, expect)

  def test_some_output(self):
    arpabet, english_words = init_dicts()
    lines = open('english-words.txt', 'r').readlines()
    f = open("output.txt", 'w')
    for word in lines:
      word = word.strip()
      arpabet_pronunciation = arpabet[word][0]
      syllables = syllabify(arpabet_pronunciation)
      s = f"Word: {word}, syllables: {syllables}"
      f.write(s + "\n")
    f.close()

if __name__ == '__main__':
  unittest.main()