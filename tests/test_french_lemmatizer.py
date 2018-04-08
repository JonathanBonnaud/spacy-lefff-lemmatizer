import unittest
import spacy
from spacy_french_lemmatizer import FrenchLemmatizer


class TestFrenchLemmatizer(unittest.TestCase):

    def setUp(self):
        self.nlp = spacy.load('fr')
        french_lem = FrenchLemmatizer()

        self.nlp.add_pipe(french_lem, name='lefff', after='parser')

    def test1(self):
        doc = self.nlp(u"les voitures arrivent à destination.")
        for d in doc:
            print(d.text, d.pos_, d.lemma_, d._.lefff_lemma)

