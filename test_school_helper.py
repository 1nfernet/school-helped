#!/usr/bin/env python3
"""
Tests unitaires pour School Helper
"""

import unittest
from school_helper.summarizer import summarize_text, summarize_lesson, extract_keywords
from school_helper.explainer import explain_concept, explain_with_examples
from school_helper.exercise_generator import generate_exercise, generate_quiz, generate_math_exercise
from school_helper.rewriter import clean_text, rewrite_text, simplify_text, expand_text


class TestSummarizer(unittest.TestCase):
    """Tests pour le module summarizer."""
    
    def test_summarize_text(self):
        """Test la fonction summarize_text."""
        text = "Le théorème de Pythagore est un résultat fondamental. Il stipule que dans un triangle rectangle, le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés. Ce théorème est très utile."
        summary = summarize_text(text, ratio=0.5)
        
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) < len(text))
        self.assertIn("théorème", summary.lower())
    
    def test_extract_keywords(self):
        """Test la fonction extract_keywords."""
        text = "Le théorème de Pythagore est fondamental en géométrie pour les triangles rectangles."
        keywords = extract_keywords(text, n=3)
        
        self.assertIsInstance(keywords, list)
        self.assertEqual(len(keywords), 3)
    
    def test_summarize_lesson(self):
        """Test la fonction summarize_lesson."""
        text = "Le théorème de Pythagore est un résultat fondamental en géométrie. Il stipule que dans un triangle rectangle, le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés."
        result = summarize_lesson(text, subject="maths")
        
        self.assertIsInstance(result, dict)
        self.assertIn('short_summary', result)
        self.assertIn('keywords', result)
        self.assertIn('subject_tips', result)


class TestExplainer(unittest.TestCase):
    """Tests pour le module explainer."""
    
    def test_explain_concept(self):
        """Test la fonction explain_concept."""
        result = explain_concept("théorème de pythagore", subject="maths")
        
        self.assertIsInstance(result, dict)
        self.assertIn('concept', result)
        self.assertIn('explanation', result)
        self.assertEqual(result['subject'], 'maths')
    
    def test_explain_unknown_concept(self):
        """Test l'explication d'un concept inconnu."""
        result = explain_concept("concept inconnu", subject="maths")
        
        self.assertIn("Désolé, je ne connais pas", result['explanation'])
    
    def test_explain_with_examples(self):
        """Test la fonction explain_with_examples."""
        result = explain_with_examples("théorème de pythagore", subject="maths", num_examples=2)
        
        self.assertIsInstance(result, dict)
        self.assertIn('examples', result)
        self.assertEqual(len(result['examples']), 2)


class TestExerciseGenerator(unittest.TestCase):
    """Tests pour le module exercise_generator."""
    
    def test_generate_exercise(self):
        """Test la génération d'un exercice."""
        exercise = generate_exercise("maths", difficulty="facile")
        
        self.assertIsInstance(exercise, object)
        self.assertEqual(exercise.subject, "maths")
        self.assertEqual(exercise.difficulty, "facile")
        self.assertTrue(hasattr(exercise, 'question'))
        self.assertTrue(hasattr(exercise, 'answer'))
    
    def test_generate_quiz(self):
        """Test la génération d'un quiz."""
        quiz = generate_quiz("maths", num_questions=3, difficulty="moyen")
        
        self.assertIsInstance(quiz, object)
        self.assertEqual(quiz.subject, "maths")
        self.assertEqual(len(quiz.questions), 3)
    
    def test_generate_math_exercise(self):
        """Test la génération d'un exercice de maths."""
        exercise = generate_math_exercise(exercise_type="algebra", difficulty="facile")
        
        self.assertEqual(exercise.subject, "maths")
        # Le titre peut être "Équation du premier degré" ou similaire
        self.assertIn("équation", exercise.title.lower())


class TestRewriter(unittest.TestCase):
    """Tests pour le module rewriter."""

    def test_clean_text_normalizes_unicode_whitespace_and_preserves_content(self):
        """clean_text compacte les espaces Unicode sans modifier les caractères."""
        text = "  Élève\tétudie\nle\u00a0théorème  "

        self.assertEqual(clean_text(text), "Élève étudie le théorème")

    def test_clean_text_returns_empty_string_for_empty_or_whitespace_input(self):
        """clean_text produit une chaîne vide quand il n'y a aucun contenu."""
        self.assertEqual(clean_text(""), "")
        self.assertEqual(clean_text("\t \n\u00a0"), "")

    def test_clean_text_rejects_non_string_input(self):
        """clean_text exige une chaîne, conformément à son annotation publique."""
        with self.assertRaises(TypeError):
            clean_text(None)
    
    def test_rewrite_text(self):
        """Test la fonction rewrite_text."""
        text = "Le théorème de Pythagore est fondamental en géométrie."
        rewritten = rewrite_text(text)
        
        self.assertIsInstance(rewritten, str)
        self.assertTrue(len(rewritten) > 0)
    
    def test_simplify_text(self):
        """Test la fonction simplify_text."""
        text = "Le théorème de Pythagore, qui est un principe fondamental en géométrie, stipule que..."
        simplified = simplify_text(text, level=2)
        
        self.assertIsInstance(simplified, str)
        # Le texte simplifié devrait être plus court ou différent
        self.assertTrue(len(simplified) <= len(text))
    
    def test_expand_text(self):
        """Test la fonction expand_text."""
        text = "Le théorème de Pythagore est fondamental."
        expanded = expand_text(text, detail_level=2)
        
        self.assertIsInstance(expanded, str)
        # Le texte étendu pourrait être plus long
        self.assertTrue(len(expanded) >= len(text))


if __name__ == '__main__':
    unittest.main()
