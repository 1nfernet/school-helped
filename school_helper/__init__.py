"""
School Helper - Mini IA pour aider les lycéens dans leurs cours

Ce package contient les modules pour :
- Résumer des cours
- Expliquer des concepts
- Générer des exercices
- Réécrire/simplifier des cours
"""

from .summarizer import summarize_text, summarize_lesson
from .explainer import explain_concept, explain_with_examples
from .exercise_generator import generate_exercise, generate_quiz, generate_math_exercise
from .rewriter import rewrite_text, simplify_text, expand_text

__version__ = "1.0.0"
__all__ = [
    'summarize_text', 'summarize_lesson',
    'explain_concept', 'explain_with_examples',
    'generate_exercise', 'generate_quiz', 'generate_math_exercise',
    'rewrite_text', 'simplify_text', 'expand_text'
]
