import nltk
from nltk.corpus import wordnet as wn
import random


def unplagiarize(text):
    """Take text and unplagiarize it."""

    words = nltk.word_tokenize(text)

    tagged_words = nltk.pos_tag(words)

    for word in tagged_words:

        # Only change adverbs and adjectives for better readability
        if str(word[1][:2]) in ["RB", "JJ"]:
            dice_roll = random.randint(0, 100)
            if dice_roll < 80:
                synonyms = get_synonyms(word[0])

                if synonyms:
                    text = text.replace(" " + word[0] + " ", " " + synonyms[0] + " ")

        elif str(word[1][:2]) == "NN":

            dice_roll = random.randint(0, 100)
            if dice_roll < 50:
                synonyms = get_synonyms(word[0])

                if synonyms:
                    text = text.replace(" " + word[0] + " ", " " + synonyms[0]" ")

    return text


def get_synonyms(word, min_acceptable_reputation=1):
    synonyms = []

    word_synsets = wn.synsets(word)

    for syn in word_synsets:

        synset_has_reputable_lemmas = False

        for lemma in syn.lemmas():

            if lemma.count() < min_acceptable_reputation:
                continue

            synset_has_reputable_lemmas = True

            if lemma.name() != word:
                synonyms.append(lemma.name().replace("_", " "))

        if synset_has_reputable_lemmas:

            syn_name = syn.name()

            syn_name = syn_name.split(".")[0]
            if syn_name != word:
                synonyms.append(syn_name.replace("_", " "))

    synonyms = list(set(synonyms))

    return synonyms
