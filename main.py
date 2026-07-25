#!/usr/bin/env python3
"""
School Helper - Mini IA 100% Python pour aider les lycéens

Ce programme offre plusieurs fonctionnalités :
- Résumer des cours
- Expliquer des concepts
- Générer des exercices
- Réécrire/simplifier des cours

Utilisation :
    python main.py [command] [options]

Exemples :
    python main.py summarize --text "Le théorème de Pythagore..."
    python main.py explain --concept "théorème de pythagore" --subject maths
    python main.py exercise --subject maths --difficulty moyen
    python main.py rewrite --text "Le cours est complexe..." --style simple
"""

import argparse
import sys
import textwrap
from typing import Optional, Dict, Any

from school_helper.summarizer import summarize_text, summarize_lesson, extract_keywords
from school_helper.explainer import explain_concept, explain_with_examples
from school_helper.exercise_generator import generate_exercise, generate_quiz, generate_math_exercise
from school_helper.rewriter import rewrite_text, simplify_text, expand_text, rephrase_lesson


def print_header():
    """Affiche l'en-tête du programme."""
    print("=" * 60)
    print("  SCHOOL HELPER - Mini IA pour les lycéens")
    print("=" * 60)
    print()


def print_footer():
    """Affiche le pied de page."""
    print()
    print("-" * 60)
    print("Fin de l'exécution. Bonne continuation dans vos études !")
    print("-" * 60)


def format_output(title: str, data: Any, color: Optional[str] = None) -> str:
    """Formate la sortie avec un titre et des données."""
    output = []
    output.append("\n" + "=" * 60)
    output.append(f"  {title.upper()}")
    output.append("=" * 60)
    
    if isinstance(data, dict):
        for key, value in data.items():
            if value:  # On n'affiche pas les valeurs vides
                output.append(f"\n{key.replace('_', ' ').title()}: ")
                if isinstance(value, list):
                    for item in value:
                        output.append(f"  - {item}")
                else:
                    output.append(f"  {value}")
    elif isinstance(data, str):
        output.append(f"\n{data}")
    else:
        output.append(f"\n{str(data)}")
    
    return '\n'.join(output)


def cmd_summarize(args):
    """Commande pour résumer un texte."""
    print_header()
    
    if args.text:
        # Résume le texte fourni
        if args.mode == 'lesson':
            result = summarize_lesson(args.text, args.subject)
            print(format_output("Résumé du cours", result))
        else:
            ratio = float(args.ratio) if args.ratio else 0.3
            summary = summarize_text(args.text, ratio=ratio, max_sentences=args.max_sentences)
            
            result = {
                'texte original': args.text[:200] + '...' if len(args.text) > 200 else args.text,
                'résumé': summary,
                'ratio': f"{ratio * 100:.0f}%",
                'mots originaux': len(args.text.split()),
                'mots dans le résumé': len(summary.split())
            }
            print(format_output("Résumé du texte", result))
            
            # Extrait aussi les mots-clés
            if len(args.text.split()) > 50:
                keywords = extract_keywords(args.text, n=5)
                print(f"\nMots-clés: {', '.join(keywords)}")
    else:
        print("Erreur : Veuillez fournir un texte avec l'option --text ou -t")
        print("Exemple : python main.py summarize --text 'Votre texte ici...'")
    
    print_footer()


def cmd_explain(args):
    """Commande pour expliquer un concept."""
    print_header()
    
    if args.concept:
        result = explain_concept(
            args.concept,
            subject=args.subject,
            level=args.level
        )
        
        print(format_output(f"Explication de : {args.concept}", result))
        
        # Ajoute des exemples si demandé
        if args.examples:
            examples_result = explain_with_examples(
                args.concept,
                subject=args.subject,
                num_examples=int(args.examples)
            )
            print(format_output("Exemples", examples_result))
    else:
        print("Erreur : Veuillez fournir un concept avec l'option --concept ou -c")
        print("Exemple : python main.py explain --concept 'théorème de pythagore' --subject maths")
    
    print_footer()


def cmd_exercise(args):
    """Commande pour générer un exercice."""
    print_header()
    
    if args.subject:
        if args.quiz:
            # Génère un quiz
            num_questions = int(args.quiz) if args.quiz.isdigit() else 5
            quiz = generate_quiz(
                args.subject,
                num_questions=num_questions,
                difficulty=args.difficulty
            )
            
            print(format_output(f"Quiz de {args.subject} - {num_questions} questions", {
                'titre': quiz.title,
                'matière': quiz.subject,
                'difficulté': quiz.difficulty,
                'nombre de questions': len(quiz.questions)
            }))
            
            print("\n" + "=" * 60)
            print("  QUESTIONS")
            print("=" * 60)
            
            for i, question in enumerate(quiz.questions, 1):
                print(f"\nQuestion {i}: {question.get('statement', '')} {question.get('question', '')}")
                if question.get('type') == 'qcm' and 'options' in question:
                    for j, option in enumerate(question['options'], 1):
                        print(f"  {j}. {option}")
                print(f"\n  → Réponse: {question.get('answer', '?')}")
                print(f"  → Explication: {question.get('explanation', '')}")
        
        elif args.math_type:
            # Génère un exercice de maths spécifique
            exercise = generate_math_exercise(
                exercise_type=args.math_type,
                difficulty=args.difficulty
            )
            print(format_output(f"Exercice de maths - {args.math_type}", {
                'titre': exercise.title,
                'énoncé': exercise.statement,
                'question': exercise.question,
                'réponse': exercise.answer,
                'explication': exercise.explanation,
                'difficulté': exercise.difficulty
            }))
        else:
            # Génère un exercice aléatoire
            exercise = generate_exercise(
                args.subject,
                difficulty=args.difficulty,
                exercise_type=args.type
            )
            print(format_output(f"Exercice de {args.subject}", {
                'titre': exercise.title,
                'énoncé': exercise.statement,
                'question': exercise.question,
                'réponse': exercise.answer,
                'explication': exercise.explanation,
                'difficulté': exercise.difficulty,
                'type': exercise.exercise_type
            }))
    else:
        print("Erreur : Veuillez fournir une matière avec l'option --subject ou -s")
        print("Exemple : python main.py exercise --subject maths --difficulty moyen")
    
    print_footer()


def cmd_rewrite(args):
    """Commande pour réécrire un texte."""
    print_header()
    
    if args.text:
        if args.mode == 'simplify':
            result = simplify_text(args.text, level=int(args.level) if args.level else 2)
            print(format_output("Texte simplifié", {
                'original': args.text[:200] + '...' if len(args.text) > 200 else args.text,
                'simplifié': result
            }))
        
        elif args.mode == 'expand':
            result = expand_text(args.text, detail_level=int(args.level) if args.level else 2)
            print(format_output("Texte étendu", {
                'original': args.text[:200] + '...' if len(args.text) > 200 else args.text,
                'étendu': result
            }))
        
        elif args.mode == 'rephrase':
            versions = rephrase_lesson(args.text, target_audience=args.audience)
            print(format_output("Cours réécrit", versions))
        
        else:
            result = rewrite_text(
                args.text,
                style=args.style,
                complexity=args.complexity
            )
            print(format_output("Texte réécrit", {
                'original': args.text[:200] + '...' if len(args.text) > 200 else args.text,
                'réécrit': result,
                'style': args.style,
                'complexité': args.complexity
            }))
    else:
        print("Erreur : Veuillez fournir un texte avec l'option --text ou -t")
        print("Exemple : python main.py rewrite --text 'Votre texte ici...' --mode simplify")
    
    print_footer()


def cmd_interactive():
    """Mode interactif."""
    print_header()
    print("\nBienvenue dans le mode interactif de School Helper !")
    print("Tapez 'help' pour voir les commandes disponibles.")
    print("Tapez 'quit' ou 'exit' pour quitter.\n")
    
    while True:
        try:
            command = input("school-helper> ").strip()
            
            if not command:
                continue
            
            if command.lower() in ['quit', 'exit', 'q']:
                print("Au revoir !")
                break
            
            elif command.lower() in ['help', 'h', '?']:
                print_interactive_help()
            
            elif command.lower().startswith('summarize '):
                text = command[len('summarize '):]
                if text:
                    summary = summarize_text(text, ratio=0.3)
                    print(f"\nRésumé: {summary}\n")
                else:
                    print("Veuillez fournir un texte à résumer.")
            
            elif command.lower().startswith('explain '):
                parts = command[len('explain '):].split(' in ')
                concept = parts[0].strip()
                subject = parts[1].strip() if len(parts) > 1 else None
                
                if concept:
                    result = explain_concept(concept, subject=subject)
                    print(f"\n{result['concept'].upper()}: {result['explanation']}")
                    if result.get('formula'):
                        print(f"Formule: {result['formula']}")
                    if result.get('examples'):
                        print("Exemples:")
                        for example in result['examples']:
                            print(f"  - {example}")
                    print()
                else:
                    print("Veuillez fournir un concept à expliquer.")
            
            elif command.lower().startswith('exercise '):
                parts = command[len('exercise '):].split()
                if parts:
                    subject = parts[0]
                    difficulty = parts[1] if len(parts) > 1 else 'moyen'
                    
                    exercise = generate_exercise(subject, difficulty)
                    print(f"\n{exercise.title}")
                    print(f"Difficulté: {exercise.difficulty}")
                    print(f"\n{exercise.statement} {exercise.question}")
                    print(f"\nRéponse: {exercise.answer}")
                    print(f"Explication: {exercise.explanation}\n")
                else:
                    print("Veuillez fournir une matière. Exemple: 'exercise maths moyen'")
            
            elif command.lower().startswith('rewrite '):
                text = command[len('rewrite '):]
                if text:
                    result = rewrite_text(text, style='normal')
                    print(f"\nTexte réécrit: {result}\n")
                else:
                    print("Veuillez fournir un texte à réécrire.")
            
            elif command.lower().startswith('simplify '):
                text = command[len('simplify '):]
                if text:
                    result = simplify_text(text, level=2)
                    print(f"\nTexte simplifié: {result}\n")
                else:
                    print("Veuillez fournir un texte à simplifier.")
            
            else:
                print(f"Commande inconnue: '{command}'. Tapez 'help' pour voir les commandes disponibles.")
        
        except KeyboardInterrupt:
            print("\nAu revoir !")
            break
        except Exception as e:
            print(f"Erreur: {e}")
    
    print_footer()


def print_interactive_help():
    """Affiche l'aide pour le mode interactif."""
    help_text = """
Commandes disponibles dans le mode interactif :

  summarize <texte>          Résume le texte fourni
  explain <concept>         Explique un concept (optionnel: 'in <matière>')
  exercise <matière>        Génère un exercice (optionnel: <difficulté>)
  rewrite <texte>           Réécrit le texte
  simplify <texte>          Simplifie le texte

  help, h, ?               Affiche cette aide
  quit, exit, q             Quitte le programme

Exemples :
  summarize Le théorème de Pythagore stipule que...
  explain théorème de pythagore in maths
  exercise maths moyen
  simplify Ce concept est particulièrement complexe...

Matières disponibles : maths, physique, chimie, histoire, francais, anglais, biologie
Niveaux de difficulté : facile, moyen, difficile
    """
    print(help_text)


def main():
    """Point d'entrée principal."""
    parser = argparse.ArgumentParser(
        description='School Helper - Mini IA pour aider les lycéens dans leurs cours',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
Exemples d'utilisation :
  python main.py summarize --text "Le théorème de Pythagore..."
  python main.py explain --concept "théorème de pythagore" --subject maths
  python main.py exercise --subject maths --difficulty moyen
  python main.py rewrite --text "Le cours est complexe..." --mode simplify
  python main.py --interactive

Matières disponibles : maths, physique, chimie, histoire, francais, anglais, biologie
Niveaux de difficulté : facile, moyen, difficile
        """)
    )
    
    # Argument global pour le mode interactif
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Lance le mode interactif'
    )
    
    # Sous-commandes
    subparsers = parser.add_subparsers(dest='command', help='Commandes disponibles')
    
    # Commande summarize
    summarize_parser = subparsers.add_parser('summarize', help='Résumer un texte ou un cours')
    summarize_parser.add_argument('--text', '-t', type=str, help='Texte à résumer')
    summarize_parser.add_argument('--mode', '-m', type=str, default='text', 
                                   choices=['text', 'lesson'], help='Mode de résumé')
    summarize_parser.add_argument('--subject', '-s', type=str, help='Matière du cours')
    summarize_parser.add_argument('--ratio', '-r', type=float, default=0.3, 
                                   help='Ratio de conservation (0.1 à 1.0)')
    summarize_parser.add_argument('--max-sentences', '-n', type=int, 
                                   help='Nombre maximum de phrases dans le résumé')
    
    # Commande explain
    explain_parser = subparsers.add_parser('explain', help='Expliquer un concept')
    explain_parser.add_argument('--concept', '-c', type=str, help='Concept à expliquer')
    explain_parser.add_argument('--subject', '-s', type=str, help='Matière')
    explain_parser.add_argument('--level', '-l', type=str, default='intermédiaire',
                                 choices=['débutant', 'intermédiaire', 'avancé'],
                                 help='Niveau d\'explication')
    explain_parser.add_argument('--examples', '-e', type=int, default=0,
                                 help='Nombre d\'exemples à fournir')
    
    # Commande exercise
    exercise_parser = subparsers.add_parser('exercise', help='Générer un exercice')
    exercise_parser.add_argument('--subject', '-s', type=str, required=True,
                                  help='Matière')
    exercise_parser.add_argument('--difficulty', '-d', type=str, default='moyen',
                                  choices=['facile', 'moyen', 'difficile'],
                                  help='Niveau de difficulté')
    exercise_parser.add_argument('--type', '-t', type=str, 
                                  choices=['qcm', 'open', 'problem'],
                                  help='Type d\'exercice')
    exercise_parser.add_argument('--quiz', '-q', type=int, nargs='?', const=5,
                                  help='Génère un quiz avec le nombre de questions spécifié')
    exercise_parser.add_argument('--math-type', '-m', type=str,
                                  choices=['algebra', 'geometry', 'calculus'],
                                  help='Type d\'exercice de maths')
    
    # Commande rewrite
    rewrite_parser = subparsers.add_parser('rewrite', help='Réécrire un texte')
    rewrite_parser.add_argument('--text', '-t', type=str, help='Texte à réécrire')
    rewrite_parser.add_argument('--mode', '-m', type=str, default='rewrite',
                                 choices=['rewrite', 'simplify', 'expand', 'rephrase'],
                                 help='Mode de réécriture')
    rewrite_parser.add_argument('--style', '-s', type=str, default='normal',
                                 choices=['normal', 'formel', 'informel', 'technique'],
                                 help='Style de réécriture')
    rewrite_parser.add_argument('--complexity', '-c', type=str, default='same',
                                 choices=['same', 'simpler', 'more_complex'],
                                 help='Complexité')
    rewrite_parser.add_argument('--level', '-l', type=int, default=2,
                                 help='Niveau de simplification/expansion (1-3)')
    rewrite_parser.add_argument('--audience', '-a', type=str, default='lyceen',
                                 help='Audience cible pour la réécriture')
    
    args = parser.parse_args()
    
    if args.interactive:
        cmd_interactive()
    elif args.command == 'summarize':
        cmd_summarize(args)
    elif args.command == 'explain':
        cmd_explain(args)
    elif args.command == 'exercise':
        cmd_exercise(args)
    elif args.command == 'rewrite':
        cmd_rewrite(args)
    else:
        # Si aucune commande n'est fournie, on lance le mode interactif
        if not args.command:
            cmd_interactive()
        else:
            parser.print_help()


if __name__ == '__main__':
    main()
