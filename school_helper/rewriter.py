"""
Module de réécriture et simplification de cours

Fonctionnalités :
- Réécrire un texte avec des mots différents
- Simplifier un texte complexe
- Étendre un texte avec plus de détails
- Adapter le style (formel, informel, etc.)
"""

import re
from typing import Dict, List, Optional
import random


# Dictionnaire de synonymes pour la réécriture
SYNONYMS = {
    # Verbes
    'être': ['est', 'représente', 'constitué', 'consiste en'],
    'avoir': ['possède', 'comporte', 'inclut', 'contient'],
    'faire': ['réaliser', 'effectuer', 'accomplir', 'exécuter'],
    'dire': ['affirmer', 'expliquer', 'indiquer', 'mentionner'],
    'montrer': ['démontrer', 'prouver', 'illustrer', 'révéler'],
    'utiliser': ['employer', 'appliquer', 'mettre en œuvre', 'recourir à'],
    'permettre': ['autoriser', 'rendre possible', 'favoriser', 'faciliter'],
    'devoir': ['falloir', 'être nécessaire', 'être obligatoire', 'devoir'],
    'pouvoir': ['être capable', 'avoir la possibilité', 'pouvoir'],
    
    # Noms
    'concept': ['idée', 'notion', 'principe', 'théorie'],
    'méthode': ['technique', 'procédé', 'approche', 'manière'],
    'résultat': ['conséquence', 'effet', 'aboutissement', 'issue'],
    'problème': ['difficulté', 'défis', 'obstacle', 'question'],
    'solution': ['réponse', 'résolution', 'remède', 'moyen'],
    'exemple': ['illustration', 'cas', 'situation', 'démonstration'],
    'importance': ['signification', 'pertinence', 'valeur', 'intérêt'],
    
    # Adjectifs
    'important': ['essentiel', 'crucial', 'fondamental', 'majeur'],
    'simple': ['facile', 'basique', 'élémentaire', 'accessible'],
    'complexe': ['compliqué', 'difficile', 'sophistiqué', 'élaboré'],
    'grand': ['important', 'considérable', 'vaste', 'étendu'],
    'petit': ['modeste', 'limité', 'réduit', 'minime'],
    
    # Adverbes
    'donc': ['par conséquent', 'en conséquence', 'ainsi', 'de ce fait'],
    'alors': ['ensuite', 'puis', 'à ce moment-là', 'dans ce cas'],
    'aussi': ['également', 'de même', 'en outre', 'par ailleurs'],
    'très': ['extrêmement', 'particulièrement', 'vraiment', 'beaucoup']
}

# Mots complexes à simplifier
COMPLEX_WORDS = {
    'substantiel': 'important',
    'conséquemment': 'donc',
    'néanmoins': 'mais',
    'cependant': 'mais',
    'en effet': 'car',
    'par ailleurs': 'aussi',
    'en revanche': 'mais',
    'de surcroît': 'en plus',
    'en outre': 'aussi',
    'à savoir': 'c\'est-à-dire',
    'autrement dit': 'c\'est-à-dire',
    'en d\'autres termes': 'c\'est-à-dire',
    'par conséquent': 'donc',
    'en conséquence': 'donc',
    'dans la mesure où': 'si',
    'afin que': 'pour que',
    'de sorte que': 'pour que',
    'bien que': 'même si',
    'quand bien même': 'même si',
    'nonobstant': 'malgré',
    'en dépit de': 'malgré',
    'au moyen de': 'avec',
    'au moyen du': 'avec le',
    'au moyen de la': 'avec la'
}


def rewrite_text(text: str, style: str = 'normal', 
                complexity: str = 'same') -> str:
    """
    Réécrit un texte avec des mots différents.
    
    Args:
        text: Texte à réécrire
        style: Style de réécriture (normal, formel, informel, technique)
        complexity: Complexité (same, simpler, more_complex)
        
    Returns:
        Texte réécrit
    """
    text = clean_text(text)
    
    if style == 'formel':
        rewritten = make_formal(text)
    elif style == 'informel':
        rewritten = make_informal(text)
    elif style == 'technique':
        rewritten = make_technical(text)
    else:
        rewritten = replace_with_synonyms(text)
    
    # Applique la complexité demandée
    if complexity == 'simpler':
        rewritten = simplify_text(rewritten)
    elif complexity == 'more_complex':
        rewritten = make_more_complex(rewritten)
    
    return rewritten


def simplify_text(text: str, level: int = 2) -> str:
    """
    Simplifie un texte en remplaçant les mots complexes par des mots simples.
    
    Args:
        text: Texte à simplifier
        level: Niveau de simplification (1 = léger, 2 = moyen, 3 = fort)
        
    Returns:
        Texte simplifié
    """
    text = clean_text(text)
    
    # Remplace les mots complexes
    for complex_word, simple_word in COMPLEX_WORDS.items():
        text = re.sub(r'\b' + re.escape(complex_word) + r'\b', simple_word, text, flags=re.IGNORECASE)
    
    # Simplifie les phrases longues
    if level >= 2:
        text = simplify_sentences(text)
    
    # Supprime les redondances
    if level >= 3:
        text = remove_redundancies(text)
    
    return text


def expand_text(text: str, detail_level: int = 2) -> str:
    """
    Étend un texte en ajoutant des détails et des explications.
    
    Args:
        text: Texte à étendre
        detail_level: Niveau de détail (1 = léger, 2 = moyen, 3 = détaillé)
        
    Returns:
        Texte étendu
    """
    text = clean_text(text)
    
    # Ajoute des explications
    if detail_level >= 2:
        text = add_explanations(text)
    
    # Ajoute des exemples
    if detail_level >= 3:
        text = add_examples(text)
    
    return text


def clean_text(text: str) -> str:
    """Nettoie le texte."""
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def replace_with_synonyms(text: str) -> str:
    """Remplace certains mots par des synonymes."""
    words = text.split()
    new_words = []
    
    for word in words:
        # Nettoie le mot (supprime la ponctuation)
        clean_word = re.sub(r'[^\w\-]', '', word.lower())
        
        # Vérifie si le mot a des synonymes
        if clean_word in SYNONYMS:
            synonyms = SYNONYMS[clean_word]
            # Choisit un synonyme aléatoire
            chosen_synonym = random.choice(synonyms)
            
            # Conserve la casse du mot original
            if word[0].isupper():
                chosen_synonym = chosen_synonym.capitalize()
            
            # Conserve la ponctuation
            if not word[-1].isalnum():
                chosen_synonym += word[-1]
            
            new_words.append(chosen_synonym)
        else:
            new_words.append(word)
    
    return ' '.join(new_words)


def make_formal(text: str) -> str:
    """Rend un texte plus formel."""
    # Remplace les contractions
    text = re.sub(r"(\w+)'(\w+)", r"\1 \2", text)
    
    # Remplace les mots informels
    informal_to_formal = {
        'du coup': 'par conséquent',
        'en fait': 'en réalité',
        'bon': 'eh bien',
        'super': 'excellent',
        'cool': 'intéressant',
        'genial': 'formidable',
        'trop': 'très',
        'vachement': 'très',
        'bcp': 'beaucoup',
        'tjs': 'toujours',
        'ptet': 'peut-être',
        'voilà': 'voici',
        'ben': 'eh bien'
    }
    
    for informal, formal in informal_to_formal.items():
        text = re.sub(r'\b' + re.escape(informal) + r'\b', formal, text, flags=re.IGNORECASE)
    
    return text


def make_informal(text: str) -> str:
    """Rend un texte plus informel."""
    # Remplace les mots formels
    formal_to_informal = {
        'par conséquent': 'du coup',
        'en réalité': 'en fait',
        'eh bien': 'bon',
        'excellent': 'super',
        'intéressant': 'cool',
        'formidable': 'génial',
        'très': 'trop',
        'beaucoup': 'bcp',
        'toujours': 'tjs',
        'peut-être': 'ptet',
        'voici': 'voilà'
    }
    
    for formal, informal in formal_to_informal.items():
        text = re.sub(r'\b' + re.escape(formal) + r'\b', informal, text, flags=re.IGNORECASE)
    
    return text


def make_technical(text: str) -> str:
    """Rend un texte plus technique."""
    # Ajoute des termes techniques
    simple_to_technical = {
        'changer': 'transformer',
        'partie': 'composante',
        'trouver': 'déterminer',
        'montrer': 'démontrer',
        'utiliser': 'employer',
        'méthode': 'méthodologie',
        'résultat': 'résultat',
        'problème': 'problématique',
        'solution': 'résolution',
        'exemple': 'illustration'
    }
    
    for simple, technical in simple_to_technical.items():
        text = re.sub(r'\b' + re.escape(simple) + r'\b', technical, text, flags=re.IGNORECASE)
    
    return text


def make_more_complex(text: str) -> str:
    """Rend un texte plus complexe."""
    # Remplace les mots simples par des mots plus complexes
    simple_to_complex = {
        'et': 'ainsi que',
        'mais': 'cependant',
        'ou': 'ou bien',
        'donc': 'par conséquent',
        'car': 'en effet',
        'si': 'dans le cas où',
        'quand': 'lorsque',
        'comme': 'tel que',
        'pour': 'afin de',
        'avec': 'au moyen de'
    }
    
    for simple, complex_word in simple_to_complex.items():
        text = re.sub(r'\b' + re.escape(simple) + r'\b', complex_word, text, flags=re.IGNORECASE)
    
    return text


def simplify_sentences(text: str) -> str:
    """Simplifie les phrases longues."""
    # Divise les phrases longues en phrases plus courtes
    sentences = re.split(r'(?<=[.!?])\s+', text)
    new_sentences = []
    
    for sentence in sentences:
        # Si la phrase est trop longue, on la divise
        if len(sentence.split()) > 20:
            # Trouve un point de division (virgule, point-virgule)
            parts = re.split(r'(?<=[,;])\s+', sentence)
            new_sentences.extend(parts)
        else:
            new_sentences.append(sentence)
    
    return ' '.join(new_sentences)


def remove_redundancies(text: str) -> str:
    """Supprime les redondances."""
    # Supprime les répétitions
    text = re.sub(r'(\b\w+\b)\s+\1', r'\1', text, flags=re.IGNORECASE)
    
    # Supprime les mots inutiles
    redundant_phrases = [
        r'qui est\s+',
        r'qui a\s+',
        r'qui sont\s+',
        r'qui ont\s+',
        r'le fait que\s+',
        r'la façon dont\s+'
    ]
    
    for phrase in redundant_phrases:
        text = re.sub(phrase, '', text, flags=re.IGNORECASE)
    
    return text


def add_explanations(text: str) -> str:
    """Ajoute des explications au texte."""
    # Trouve des concepts qui pourraient être expliqués
    concepts = ['théorème', 'loi', 'principe', 'méthode', 'concept', 'notion']
    
    for concept in concepts:
        pattern = r'\b(' + concept + r'\s+\w+)'
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        
        for match in matches:
            # Ajoute une explication simple
            explanation = f" (c\'est-à-dire {match.lower()})"
            text = re.sub(r'\b' + re.escape(match) + r'\b', match + explanation, text, count=1, flags=re.IGNORECASE)
    
    return text


def add_examples(text: str) -> str:
    """Ajoute des exemples au texte."""
    # Trouve des opportunités pour ajouter des exemples
    example_triggers = ['par exemple', 'comme', 'tel que', 'notamment']
    
    for trigger in example_triggers:
        if trigger in text.lower():
            # Ajoute un exemple après le déclencheur
            text = text.replace(trigger, trigger + " (comme un triangle rectangle avec des côtés de 3 cm et 4 cm)")
            break
    
    return text


def rephrase_lesson(text: str, target_audience: str = 'lyceen') -> Dict[str, str]:
    """
    Réécrit un cours pour une audience spécifique.
    
    Args:
        text: Texte du cours
        target_audience: Audience cible (lyceen, collegien, etudiant, debutant)
        
    Returns:
        Dictionnaire avec différentes versions du cours
    """
    versions = {}
    
    # Version originale
    versions['original'] = text
    
    # Version simplifiée pour les débutants
    if target_audience in ['lyceen', 'collegien', 'debutant']:
        versions['simplified'] = simplify_text(text, level=3)
        versions['easy'] = simplify_text(text, level=2)
    
    # Version étendue pour les étudiants
    if target_audience in ['etudiant', 'avance']:
        versions['extended'] = expand_text(text, detail_level=3)
        versions['detailed'] = expand_text(text, detail_level=2)
    
    # Version réécrite
    versions['rewritten'] = rewrite_text(text)
    
    # Version formelle
    versions['formal'] = make_formal(text)
    
    return versions
