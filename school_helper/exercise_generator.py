"""
Module de génération d'exercices

Fonctionnalités :
- Générer des exercices variés
- Créer des QCM
- Générer des exercices de maths avec corrections
- Adapter la difficulté
"""

import random
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass


@dataclass
class Exercise:
    """Représente un exercice avec son énoncé et sa correction."""
    title: str
    statement: str
    question: str
    answer: str
    explanation: str
    difficulty: str  # facile, moyen, difficile
    subject: str
    exercise_type: str  # qcm, open, problem, etc.


@dataclass
class Quiz:
    """Représente un quiz avec plusieurs questions."""
    title: str
    questions: List[Dict]
    subject: str
    difficulty: str


# Base de données d'exercices par matière
EXERCISE_DATABASE = {
    'maths': {
        'facile': [
            {
                'type': 'open',
                'title': 'Calcul simple',
                'statement': 'Calculez :',
                'question': '5 + 7 = ?',
                'answer': '12',
                'explanation': '5 + 7 = 12. C\'est une addition simple.'
            },
            {
                'type': 'open',
                'title': 'Multiplication',
                'statement': 'Calculez :',
                'question': '6 × 8 = ?',
                'answer': '48',
                'explanation': '6 × 8 = 48. Vous pouvez vérifier avec l\'addition répétée : 6+6+6+6+6+6+6+6 = 48.'
            },
            {
                'type': 'qcm',
                'title': 'Théorème de Pythagore',
                'statement': 'Dans un triangle rectangle avec des côtés de 3 cm et 4 cm, quelle est la longueur de l\'hypoténuse ?',
                'question': '',
                'options': ['5 cm', '7 cm', '6 cm', '8 cm'],
                'answer': '5 cm',
                'explanation': 'D\'après le théorème de Pythagore : 3² + 4² = 9 + 16 = 25 = 5². Donc l\'hypoténuse mesure 5 cm.'
            }
        ],
        'moyen': [
            {
                'type': 'open',
                'title': 'Équation du premier degré',
                'statement': 'Résolvez l\'équation :',
                'question': '2x + 5 = 13',
                'answer': 'x = 4',
                'explanation': '2x + 5 = 13 → 2x = 13 - 5 → 2x = 8 → x = 8 / 2 → x = 4.'
            },
            {
                'type': 'open',
                'title': 'Calcul de pourcentage',
                'statement': 'Calculez :',
                'question': 'Quel est 20% de 150 ?',
                'answer': '30',
                'explanation': '20% de 150 = (20/100) × 150 = 0.2 × 150 = 30.'
            },
            {
                'type': 'qcm',
                'title': 'Fonction affine',
                'statement': 'Quelle est la pente de la fonction f(x) = 3x - 2 ?',
                'question': '',
                'options': ['3', '-2', '1', '0'],
                'answer': '3',
                'explanation': 'Dans une fonction affine f(x) = ax + b, le coefficient a représente la pente. Ici, a = 3.'
            }
        ],
        'difficile': [
            {
                'type': 'open',
                'title': 'Équation du second degré',
                'statement': 'Résolvez l\'équation :',
                'question': 'x² - 5x + 6 = 0',
                'answer': 'x = 2 ou x = 3',
                'explanation': 'x² - 5x + 6 = 0 → (x - 2)(x - 3) = 0 → x = 2 ou x = 3.'
            },
            {
                'type': 'open',
                'title': 'Problème de géométrie',
                'statement': 'Un triangle rectangle a une hypoténuse de 10 cm et un côté de 6 cm. Quelle est la longueur du troisième côté ?',
                'question': '',
                'answer': '8 cm',
                'explanation': 'Soit c le côté inconnu. D\'après Pythagore : 6² + c² = 10² → 36 + c² = 100 → c² = 64 → c = 8 cm.'
            }
        ]
    },
    'physique': {
        'facile': [
            {
                'type': 'qcm',
                'title': 'Unité de force',
                'statement': 'Quelle est l\'unité de la force dans le système international ?',
                'question': '',
                'options': ['Newton (N)', 'Joule (J)', 'Watt (W)', 'Kilogramme (kg)'],
                'answer': 'Newton (N)',
                'explanation': 'La force se mesure en Newton (N) dans le système international.'
            },
            {
                'type': 'open',
                'title': 'Calcul de vitesse',
                'statement': 'Une voiture parcourt 100 km en 2 heures. Quelle est sa vitesse moyenne ?',
                'question': '',
                'answer': '50 km/h',
                'explanation': 'Vitesse = Distance / Temps = 100 km / 2 h = 50 km/h.'
            }
        ],
        'moyen': [
            {
                'type': 'open',
                'title': 'Énergie cinétique',
                'statement': 'Calculez l\'énergie cinétique d\'un objet de 5 kg se déplaçant à 10 m/s.',
                'question': '',
                'answer': '250 J',
                'explanation': 'Ec = ½ × m × v² = 0.5 × 5 × 10² = 0.5 × 5 × 100 = 250 J.'
            }
        ]
    },
    'chimie': {
        'facile': [
            {
                'type': 'qcm',
                'title': 'Symbole chimique',
                'statement': 'Quel est le symbole chimique de l\'oxygène ?',
                'question': '',
                'options': ['O', 'Ox', 'Og', 'O₂'],
                'answer': 'O',
                'explanation': 'Le symbole chimique de l\'oxygène est O.'
            }
        ]
    },
    'francais': {
        'facile': [
            {
                'type': 'open',
                'title': 'Conjugaison',
                'statement': 'Conjuguez le verbe "être" à la première personne du singulier du présent de l\'indicatif.',
                'question': '',
                'answer': 'je suis',
                'explanation': 'Le verbe "être" se conjugue "je suis" à la première personne du singulier du présent.'
            }
        ]
    }
}


def generate_exercise(subject: str, difficulty: str = 'moyen', 
                     exercise_type: Optional[str] = None) -> Exercise:
    """
    Génère un exercice aléatoire.
    
    Args:
        subject: Matière (maths, physique, chimie, etc.)
        difficulty: Niveau de difficulté (facile, moyen, difficile)
        exercise_type: Type d'exercice (qcm, open, problem) - optionnel
        
    Returns:
        Un objet Exercise
    """
    subject = subject.lower()
    difficulty = difficulty.lower()
    
    # Vérifie que la matière existe
    if subject not in EXERCISE_DATABASE:
        raise ValueError(f"Matière '{subject}' non trouvée. Matières disponibles : {list(EXERCISE_DATABASE.keys())}")
    
    # Vérifie que le niveau existe
    if difficulty not in EXERCISE_DATABASE[subject]:
        difficulty = 'moyen'  # Niveau par défaut
    
    # Filtre par type si spécifié
    exercises = EXERCISE_DATABASE[subject][difficulty]
    if exercise_type:
        exercises = [e for e in exercises if e.get('type') == exercise_type]
    
    if not exercises:
        # Si aucun exercice ne correspond, on prend tous les exercices
        exercises = EXERCISE_DATABASE[subject][difficulty]
    
    # Sélectionne un exercice aléatoire
    exercise_data = random.choice(exercises)
    
    # Crée l'objet Exercise
    exercise = Exercise(
        title=exercise_data.get('title', 'Exercice'),
        statement=exercise_data.get('statement', ''),
        question=exercise_data.get('question', ''),
        answer=exercise_data.get('answer', ''),
        explanation=exercise_data.get('explanation', ''),
        difficulty=difficulty,
        subject=subject,
        exercise_type=exercise_data.get('type', 'open')
    )
    
    return exercise


def generate_quiz(subject: str, num_questions: int = 5, 
                  difficulty: str = 'moyen') -> Quiz:
    """
    Génère un quiz avec plusieurs questions.
    
    Args:
        subject: Matière
        num_questions: Nombre de questions
        difficulty: Niveau de difficulté
        
    Returns:
        Un objet Quiz
    """
    questions = []
    
    for _ in range(num_questions):
        exercise = generate_exercise(subject, difficulty)
        
        question = {
            'type': exercise.exercise_type,
            'statement': exercise.statement,
            'question': exercise.question,
            'answer': exercise.answer,
            'explanation': exercise.explanation
        }
        
        # Ajoute les options pour les QCM
        if exercise.exercise_type == 'qcm':
            # On doit trouver les options dans la base de données
            # Pour l'instant, on génère des options aléatoires
            question['options'] = generate_qcm_options(exercise)
        
        questions.append(question)
    
    quiz = Quiz(
        title=f"Quiz de {subject} - Niveau {difficulty}",
        questions=questions,
        subject=subject,
        difficulty=difficulty
    )
    
    return quiz


def generate_qcm_options(exercise: Exercise) -> List[str]:
    """Génère des options pour un QCM."""
    # Si l'exercice a déjà des options, on les utilise
    if hasattr(exercise, 'options'):
        return exercise.options
    
    # Sinon, on génère des options aléatoires
    # (Ceci est une version simplifiée)
    correct_answer = exercise.answer
    
    # Génère 3 mauvaises réponses
    wrong_answers = []
    
    # Pour les réponses numériques
    if correct_answer.isdigit():
        correct_num = int(correct_answer)
        wrong_answers = [
            str(correct_num + random.randint(1, 5)),
            str(correct_num - random.randint(1, 5)),
            str(correct_num * 2)
        ]
    else:
        # Pour les réponses textuelles, on génère des variantes
        wrong_answers = [
            f"Réponse {random.randint(1, 100)}",
            f"Autre {random.randint(1, 100)}",
            f"Option {random.randint(1, 100)}"
        ]
    
    # Mélange les options
    options = [correct_answer] + wrong_answers
    random.shuffle(options)
    
    return options


def generate_math_exercise(exercise_type: str = 'algebra', 
                          difficulty: str = 'moyen') -> Exercise:
    """
    Génère un exercice de maths spécifique.
    
    Args:
        exercise_type: Type d'exercice (algebra, geometry, calculus, etc.)
        difficulty: Niveau de difficulté
        
    Returns:
        Un objet Exercise
    """
    exercise_type = exercise_type.lower()
    
    # Génère selon le type
    if exercise_type == 'algebra':
        return generate_algebra_exercise(difficulty)
    elif exercise_type == 'geometry':
        return generate_geometry_exercise(difficulty)
    elif exercise_type == 'calculus':
        return generate_calculus_exercise(difficulty)
    else:
        # Par défaut, on génère un exercice d'algèbre
        return generate_algebra_exercise(difficulty)


def generate_algebra_exercise(difficulty: str) -> Exercise:
    """Génère un exercice d'algèbre."""
    if difficulty == 'facile':
        # Équation simple
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        c = a * random.randint(2, 8)
        
        question = f"{a}x + {b} = {c}"
        answer = f"x = {(c - b) / a}"
        explanation = f"{a}x + {b} = {c} → {a}x = {c} - {b} → {a}x = {c - b} → x = {(c - b) / a}"
        
        return Exercise(
            title='Équation du premier degré',
            statement='Résolvez l\'équation :',
            question=question,
            answer=answer,
            explanation=explanation,
            difficulty=difficulty,
            subject='maths',
            exercise_type='open'
        )
    
    elif difficulty == 'moyen':
        # Équation avec fractions
        a = random.randint(2, 5)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        d = a * random.randint(2, 5) + b
        
        question = f"{a}x + {b} = {d}"
        answer = f"x = {(d - b) / a}"
        explanation = f"{a}x + {b} = {d} → {a}x = {d} - {b} → x = {(d - b) / a}"
        
        return Exercise(
            title='Équation avec coefficients',
            statement='Résolvez l\'équation :',
            question=question,
            answer=answer,
            explanation=explanation,
            difficulty=difficulty,
            subject='maths',
            exercise_type='open'
        )
    
    else:  # difficile
        # Équation du second degré
        a = random.randint(1, 2)
        b = random.randint(-5, 5)
        c = random.randint(1, 4)
        
        # Calcul des solutions
        discriminant = b**2 - 4*a*c
        if discriminant < 0:
            # On recommence pour avoir des solutions réelles
            return generate_algebra_exercise(difficulty)
        
        import math
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        
        question = f"{a}x² + {b}x + {c} = 0"
        answer = f"x = {x1} ou x = {x2}"
        explanation = (f"Utilisation de la formule du discriminant : Δ = b² - 4ac = {discriminant}. "
                      f"Solutions : x = (-b ± √Δ) / 2a")
        
        return Exercise(
            title='Équation du second degré',
            statement='Résolvez l\'équation :',
            question=question,
            answer=answer,
            explanation=explanation,
            difficulty=difficulty,
            subject='maths',
            exercise_type='open'
        )


def generate_geometry_exercise(difficulty: str) -> Exercise:
    """Génère un exercice de géométrie."""
    if difficulty == 'facile':
        # Calcul de périmètre
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        perimeter = 2 * (a + b)
        
        question = f"Quel est le périmètre d'un rectangle de longueur {a} cm et de largeur {b} cm ?"
        answer = f"{perimeter} cm"
        explanation = f"Périmètre = 2 × (longueur + largeur) = 2 × ({a} + {b}) = 2 × {a + b} = {perimeter} cm"
        
        return Exercise(
            title='Périmètre d\'un rectangle',
            statement='Calculez :',
            question=question,
            answer=answer,
            explanation=explanation,
            difficulty=difficulty,
            subject='maths',
            exercise_type='open'
        )
    
    elif difficulty == 'moyen':
        # Théorème de Pythagore
        a = random.randint(3, 8)
        b = random.randint(3, 8)
        c = (a**2 + b**2)**0.5
        
        if not c.is_integer():
            # On veut un triangle pythagoricien
            return generate_geometry_exercise(difficulty)
        
        c = int(c)
        
        question = (f"Dans un triangle rectangle, les côtés de l'angle droit mesurent {a} cm et {b} cm. "
                   f"Quelle est la longueur de l'hypoténuse ?")
        answer = f"{c} cm"
        explanation = f"D'après le théorème de Pythagore : {a}² + {b}² = {a**2} + {b**2} = {a**2 + b**2} = {c}²"
        
        return Exercise(
            title='Théorème de Pythagore',
            statement='Calculez :',
            question=question,
            answer=answer,
            explanation=explanation,
            difficulty=difficulty,
            subject='maths',
            exercise_type='open'
        )
    
    else:  # difficile
        # Aire d'un cercle
        r = random.randint(2, 10)
        area = 3.14 * r**2
        
        question = f"Quelle est l'aire d'un cercle de rayon {r} cm ? (Utilisez π ≈ 3.14)"
        answer = f"{area:.2f} cm²"
        explanation = f"Aire = π × r² = 3.14 × {r}² = 3.14 × {r**2} = {area:.2f} cm²"
        
        return Exercise(
            title='Aire d\'un cercle',
            statement='Calculez :',
            question=question,
            answer=answer,
            explanation=explanation,
            difficulty=difficulty,
            subject='maths',
            exercise_type='open'
        )


def generate_calculus_exercise(difficulty: str) -> Exercise:
    """Génère un exercice d'analyse."""
    if difficulty == 'facile':
        # Calcul de dérivée simple
        a = random.randint(1, 5)
        b = random.randint(0, 5)
        
        question = f"Quelle est la dérivée de f(x) = {a}x + {b} ?"
        answer = f"f'(x) = {a}"
        explanation = f"La dérivée d'une fonction affine f(x) = ax + b est f'(x) = a"
        
        return Exercise(
            title='Dérivée d\'une fonction affine',
            statement='Calculez :',
            question=question,
            answer=answer,
            explanation=explanation,
            difficulty=difficulty,
            subject='maths',
            exercise_type='open'
        )
    
    else:  # moyen ou difficile
        # Calcul de dérivée avec puissance
        a = random.randint(1, 3)
        n = random.randint(2, 4)
        
        question = f"Quelle est la dérivée de f(x) = {a}x^{n} ?"
        answer = f"f'(x) = {a * n}x^{n - 1}"
        explanation = f"La dérivée de ax^n est a×n×x^(n-1). Donc {a}x^{n} → {a * n}x^{n - 1}"
        
        return Exercise(
            title='Dérivée d\'une fonction puissance',
            statement='Calculez :',
            question=question,
            answer=answer,
            explanation=explanation,
            difficulty=difficulty,
            subject='maths',
            exercise_type='open'
        )
