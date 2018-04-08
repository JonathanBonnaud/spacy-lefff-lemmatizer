from spacy.tokens import Token
from french_lefff_lemmatizer.french_lefff_lemmatizer import FrenchLefffLemmatizer


class FrenchLemmatizer(object):
    name = 'lefff'

    SPACY_WORDNET_DIC = {'ADJ': 'a',
                         'ADV': 'r',
                         'NOUN': 'n',
                         'VERB': 'v'}

    def __init__(self):
        # register your new attribute token._.lefff_lemma
        Token.set_extension('lefff_lemma', default=None)

        self.lemmatizer = FrenchLefffLemmatizer()

    def __call__(self, doc):
        for token in doc:
            wn_pos = self.SPACY_WORDNET_DIC[token.pos_] if token.pos_ in self.SPACY_WORDNET_DIC else token.pos_
            lemma = self.lemmatizer.lemmatize(token.text, wn_pos)

            # TODO: return only ONE lemma
            if not isinstance(lemma, list):
                token._.lefff_lemma = lemma
            elif len(lemma) == 1:
                token._.lefff_lemma = lemma[0][0]
            else:
                # not lemmatized word or None or empty?
                token._.lefff_lemma = ''
        return doc
