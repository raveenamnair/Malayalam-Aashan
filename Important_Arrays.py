from Alphabet_Categories import *
URLS = ["http://learn101.org/malayalam_adjectives.php", "http://learn101.org/malayalam_nouns.php",
        "http://learn101.org/malayalam_plural.php", "http://learn101.org/malayalam_gender.php",
        "http://learn101.org/malayalam_numbers.php", "http://learn101.org/malayalam_phrases.php",
        "http://learn101.org/malayalam_grammar.php", "http://learn101.org/malayalam_vocabulary.php",
        "http://learn101.org/malayalam_verbs.php"]
ignore_words = ["Grammar Rules - Malayalam + Pronunciation", " English - Malayalam - Pronunciation",
                " Grammar + Rules - Malayalam + Pronunciation", " Grammar Rules - Malayalam + Pronunciation",
                " Holiday Wishes - Malayalam - Pronunciation", " Cardinal and Ordinal - Malayalam - Pronunciation",
                " Prepositions - Malayalam - Pronunciation", " Prepositions + Rules - Malayalam + Pronunciation",
                " Negation + Rules - Malayalam + Pronunciation", " Negative Sentences - Malayalam + Pronunciation",
                " Questions + Rules - Malayalam + Pronunciation", " Adverbs - Malayalam - Pronunciation",
                " Adverbs + Rules - Malayalam + Pronunciation", " Personal Pronouns - Malayalam - Pronunciation",
                " Object Pronouns - Malayalam - Pronunciation", " Possessive Pronouns - Malayalam - Pronunciation",
                " Personal Pronouns - Malayalam + Pronunciation", " Object Pronouns - Malayalam + Pronunciation",
                " Possessive Pronouns - Malayalam + Pronunciation", " Demonstrative Pronouns - Malayalam - Pronunciation",
                " Language - Malayalam - Pronunciation - Country - Malayalam - Pronunciation", " Travel - Malayalam - Pronunciation",
                " Class - Malayalam - Pronunciation", " Present Tense - Malayalam - Pronunciation",
                " Past Tense - Malayalam - Pronunciation", " Future Tense - Malayalam - Pronunciation"]

VOWELS = get_vowels()
CONSONANTS = get_consonants()
MODIFIERS = get_modify_vowels()

MODULES = ["Learn Vowels", "Review Vowels", "Learn Consonants", "Review Consonants", "Learn Modifiers",
           "Review Modifiers", "Practice Quiz", "Basic Words", "Medium Level Words", "Difficult Words",
           "Small Sentences", "Long Sentences", "Advanced Reading"]
