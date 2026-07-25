"""
Module de résumé de cours et de textes

Fonctionnalités :
- Résumer un texte long en quelques phrases
- Résumer un cours complet avec structure
- Extraire les points clés
"""

import re
from typing import List, Dict, Optional, Tuple


def clean_text(text: str) -> str:
    """Nettoie le texte en supprimant les espaces multiples et les caractères spéciaux inutiles."""
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_sentences(text: str) -> List[str]:
    """Extrait les phrases d'un texte."""
    # Utilise des expressions régulières pour identifier les fins de phrases
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]


def extract_keywords(text: str, n: int = 10) -> List[str]:
    """Extrait les mots-clés d'un texte (simplifié)."""
    # Supprime la ponctuation et passe en minuscule
    words = re.findall(r'\b\w{4,}\b', text.lower())
    
    # Compte la fréquence des mots
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Filtre les mots courants (articles, prépositions, etc.)
    stop_words = {
        'le', 'la', 'les', 'de', 'des', 'du', 'un', 'une', 'et', 'est', 'en', 'à', 'au',
        'pour', 'par', 'sur', 'avec', 'dans', 'ce', 'cette', 'ces', 'qui', 'que', 'dont',
        'plus', 'sont', 'ont', 'été', 'être', 'avoir', 'il', 'elle', 'on', 'nous', 'vous',
        'ils', 'elles', 'son', 'sa', 'ses', 'leur', 'leurs', 'ceci', 'cela'
    }
    
    filtered_words = {word: freq for word, freq in word_freq.items() 
                     if word not in stop_words and len(word) > 3}
    
    # Trie par fréquence et retourne les n premiers
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in sorted_words[:n]]


def summarize_text(text: str, ratio: float = 0.3, max_sentences: Optional[int] = None) -> str:
    """
    Résume un texte en conservant les phrases les plus importantes.
    
    Args:
        text: Texte à résumer
        ratio: Ratio de conservation (0.1 à 1.0)
        max_sentences: Nombre maximum de phrases dans le résumé
        
    Returns:
        Résumé du texte
    """
    text = clean_text(text)
    sentences = extract_sentences(text)
    
    if not sentences:
        return text
    
    # Si max_sentences est spécifié, on le respecte
    if max_sentences is not None:
        max_sentences = min(max_sentences, len(sentences))
        return ' '.join(sentences[:max_sentences])
    
    # Sinon, on utilise le ratio
    num_sentences = max(1, int(len(sentences) * ratio))
    
    # Pour l'instant, on prend simplement les premières phrases
    # (Une version plus avancée pourrait analyser la pertinence)
    summary = ' '.join(sentences[:num_sentences])
    
    return summary


def summarize_lesson(text: str, subject: Optional[str] = None) -> Dict[str, str]:
    """
    Résume un cours complet avec une structure adaptée.
    
    Args:
        text: Texte du cours
        subject: Matière (optionnel, pour adapter le résumé)
        
    Returns:
        Dictionnaire avec différentes versions du résumé
    """
    text = clean_text(text)
    
    # Résumé court (10% du texte)
    short_summary = summarize_text(text, ratio=0.1)
    
    # Résumé moyen (30% du texte)
    medium_summary = summarize_text(text, ratio=0.3)
    
    # Points clés (5 phrases max)
    key_points = summarize_text(text, max_sentences=5)
    
    # Mots-clés
    keywords = extract_keywords(text, n=8)
    
    result = {
        'short_summary': short_summary,
        'medium_summary': medium_summary,
        'key_points': key_points,
        'keywords': keywords,
        'original_length': len(text.split()),
        'summary_length': len(short_summary.split())
    }
    
    # Ajoute des conseils spécifiques selon la matière
    if subject:
        result['subject_tips'] = get_subject_tips(subject)
    
    return result


def get_subject_tips(subject: str) -> str:
    """Retourne des conseils spécifiques selon la matière."""
    subject = subject.lower()
    
    tips = {
        'maths': "Pour les maths, concentrez-vous sur les formules et les démonstrations. "
                "Essayez de comprendre la logique derrière chaque théorème.",
        'physique': "En physique, comprenez les concepts fondamentaux avant d'apprendre les formules. "
                   "Faites des schémas pour visualiser les phénomènes.",
        'chimie': "En chimie, mémorisez les réactions types et comprenez les mécanismes. "
                  "Utilisez des tableaux pour organiser les informations.",
        'histoire': "En histoire, retenez les dates clés et les causes/conséquences des événements. "
                    "Faites des frises chronologiques.",
        'francais': "En français, analysez la structure des textes et les procédés littéraires. "
                    "Lisez à voix haute pour mieux comprendre.",
        'anglais': "En anglais, pratiquez régulièrement l'oral et l'écrit. "
                   "Apprenez du vocabulaire par thèmes.",
        'biologie': "En biologie, comprenez les mécanismes du vivant et les liens entre les concepts. "
                    "Utilisez des schémas annotés.",
        'philosophie': "En philosophie, concentrez-vous sur les arguments et les contre-arguments. "
                       "Essayez de reformuler les idées avec vos propres mots."
    }
    
    return tips.get(subject, "Pour bien réviser, relisez régulièrement vos cours et faites des exercices d'application.")
