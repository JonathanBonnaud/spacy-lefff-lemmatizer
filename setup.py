from setuptools import setup

setup(
    name='spacy-lefff-lemmatizer',
    version='0.1',
    description='SpaCy extension for French Lemmatizer based on LEFFF a large-scale morphological and syntactic lexicon for French',
    keywords='spacy french lefff lemmatizer',
    url='https://github.com/JonathanBonnaud/spacy-lefff-lemmatizer',
    author='Jonathan Bonnaud',
    author_email='jonathan.bonnaud.pro@gmail.com',
    license='Apache 2',
    packages=['spacy_french_lemmatizer'],
    zip_safe=False
)
