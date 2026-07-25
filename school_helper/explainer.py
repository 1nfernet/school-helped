"""
Module d'explication de concepts

Fonctionnalités :
- Expliquer un concept de manière simple
- Fournir des exemples concrets
- Adapter l'explication au niveau de l'élève
"""

from typing import Dict, List, Optional
import random


# Base de connaissances pour différentes matières
KNOWLEDGE_BASE = {
    'maths': {
        'théorème de pythagore': {
            'definition': "Le théorème de Pythagore s'applique aux triangles rectangles. "
                         "Il stipule que le carré de l'hypoténuse (côté opposé à l'angle droit) "
                         "est égal à la somme des carrés des deux autres côtés.",
            'formula': "a² + b² = c²",
            'examples': [
                "Si un triangle rectangle a des côtés de 3 cm et 4 cm, "
                "l'hypoténuse sera de 5 cm car 3² + 4² = 9 + 16 = 25 = 5².",
                "Pour un triangle avec a=6 et b=8, on calcule c = √(6² + 8²) = √(36 + 64) = √100 = 10."
            ],
            'applications': [
                "Calculer des distances en géométrie",
                "Vérifier si un triangle est rectangle",
                "Résoudre des problèmes de construction"
            ]
        },
        'fonction affine': {
            'definition': "Une fonction affine est une fonction de la forme f(x) = ax + b, "
                         "où a et b sont des nombres réels.",
            'formula': "f(x) = ax + b",
            'examples': [
                "f(x) = 2x + 3 est une fonction affine avec a=2 et b=3.",
                "La fonction f(x) = -x + 5 a une pente de -1 et une ordonnée à l'origine de 5."
            ],
            'applications': [
                "Modéliser des situations de proportionnalité",
                "Représenter des droites dans un repère",
                "Résoudre des problèmes de vitesse constante"
            ]
        },
        'équation du second degré': {
            'definition': "Une équation du second degré est une équation de la forme ax² + bx + c = 0, "
                         "où a, b et c sont des réels avec a ≠ 0.",
            'formula': "ax² + bx + c = 0",
            'examples': [
                "x² - 5x + 6 = 0 a pour solutions x=2 et x=3.",
                "2x² + 4x - 6 = 0 peut être résolue avec la formule du discriminant."
            ],
            'applications': [
                "Trouver les racines d'une parabole",
                "Résoudre des problèmes de géométrie",
                "Optimiser des fonctions"
            ]
        }
    },
    'physique': {
        'loi de newton': {
            'definition': "Les lois de Newton décrivent le mouvement des objets. "
                         "La première loi (principe d'inertie) stipule qu'un objet au repos "
                         "reste au repos et un objet en mouvement reste en mouvement à vitesse constante "
                         "sauf si une force extérieure agit sur lui.",
            'formula': "F = m × a (2ème loi)",
            'examples': [
                "Une balle roulant sur le sol s'arrête à cause des frottements (force extérieure).",
                "Dans l'espace, sans frottement, un objet lancé continuera indéfiniment."
            ],
            'applications': [
                "Comprendre le mouvement des planètes",
                "Calculer des forces en ingénierie",
                "Expliquer les trajectoires"
            ]
        },
        'énergie cinétique': {
            'definition': "L'énergie cinétique est l'énergie que possède un objet du fait de son mouvement.",
            'formula': "Ec = ½ × m × v²",
            'examples': [
                "Une voiture de 1000 kg roulant à 20 m/s a une énergie cinétique de 200,000 J.",
                "Un ballon de football lancé a une énergie cinétique proportionnelle à sa vitesse."
            ],
            'applications': [
                "Calculer l'énergie nécessaire pour arrêter un véhicule",
                "Comprendre les chocs et les collisions",
                "Étudier le mouvement des particules"
            ]
        }
    },
    'chimie': {
        'réaction chimique': {
            'definition': "Une réaction chimique est une transformation de la matière où "
                         "des réactifs sont convertis en produits.",
            'formula': "Réactifs → Produits",
            'examples': [
                "2H₂ + O₂ → 2H₂O (formation de l'eau)",
                "Fe + S → FeS (formation du sulfure de fer)"
            ],
            'applications': [
                "Comprendre la combustion",
                "Étudier la corrosion des métaux",
                "Développer de nouveaux médicaments"
            ]
        },
        'ph': {
            'definition': "Le pH mesure l'acidité ou la basicité d'une solution. "
                         "Il varie de 0 (très acide) à 14 (très basique), avec 7 étant neutre.",
            'formula': "pH = -log[H⁺]",
            'examples': [
                "Le jus de citron a un pH d'environ 2 (acide).",
                "L'eau pure a un pH de 7 (neutre).",
                "Le savon a un pH d'environ 9-10 (basique)."
            ],
            'applications': [
                "Mesurer l'acidité des sols",
                "Contrôler la qualité de l'eau",
                "Comprendre les réactions acido-basiques"
            ]
        }
    },
    'histoire': {
        'révolution française': {
            'definition': "La Révolution française (1789-1799) est une période de bouleversements "
                         "politiques, sociaux et économiques en France qui a mis fin à la monarchie absolue.",
            'formula': None,
            'examples': [
                "La prise de la Bastille le 14 juillet 1789 est un symbole fort du début de la révolution.",
                "La Déclaration des droits de l'homme et du citoyen a été adoptée en 1789."
            ],
            'applications': [
                "Comprendre les origines des démocraties modernes",
                "Étudier les changements sociaux majeurs",
                "Analyser l'impact des idées des Lumières"
            ]
        },
        'première guerre mondiale': {
            'definition': "La Première Guerre mondiale (1914-1918) est un conflit mondial "
                         "qui a opposé les Alliés (France, Royaume-Uni, Russie, etc.) "
                         "aux Empires centraux (Allemagne, Autriche-Hongrie, etc.).",
            'formula': None,
            'examples': [
                "L'assassinat de l'archiduc François-Ferdinand en 1914 a déclenché la guerre.",
                "Le traité de Versailles en 1919 a officiellement mis fin à la guerre."
            ],
            'applications': [
                "Comprendre les causes des conflits modernes",
                "Étudier l'évolution des frontières en Europe",
                "Analyser l'impact des guerres sur les sociétés"
            ]
        }
    }
}


def explain_concept(concept: str, subject: Optional[str] = None, 
                   level: str = 'intermédiaire') -> Dict[str, str]:
    """
    Explique un concept de manière détaillée.
    
    Args:
        concept: Concept à expliquer
        subject: Matière (maths, physique, chimie, histoire, etc.)
        level: Niveau (débutant, intermédiaire, avancé)
        
    Returns:
        Dictionnaire avec l'explication, des exemples et des applications
    """
    concept = concept.lower().strip()
    
    # Recherche dans la base de connaissances
    explanation = None
    
    if subject:
        subject = subject.lower()
        if subject in KNOWLEDGE_BASE:
            if concept in KNOWLEDGE_BASE[subject]:
                explanation = KNOWLEDGE_BASE[subject][concept]
    else:
        # Recherche dans toutes les matières
        for subj, concepts in KNOWLEDGE_BASE.items():
            if concept in concepts:
                explanation = concepts[concept]
                subject = subj
                break
    
    # Si le concept n'est pas trouvé dans la base
    if explanation is None:
        return {
            'concept': concept,
            'explanation': f"Désolé, je ne connais pas encore le concept '{concept}'. "
                          f"Essayez de préciser la matière ou de reformuler.",
            'examples': [],
            'applications': [],
            'subject': subject or 'inconnu',
            'level': level
        }
    
    # Adapte l'explication au niveau
    base_explanation = explanation['definition']
    
    if level == 'débutant':
        # Simplifie l'explication
        simplified = simplify_explanation(base_explanation)
        final_explanation = simplified
    elif level == 'avancé':
        # Ajoute des détails techniques
        final_explanation = base_explanation + " " + get_advanced_details(concept, subject)
    else:
        final_explanation = base_explanation
    
    result = {
        'concept': concept,
        'explanation': final_explanation,
        'formula': explanation.get('formula', None),
        'examples': explanation.get('examples', []),
        'applications': explanation.get('applications', []),
        'subject': subject,
        'level': level
    }
    
    # Ajoute des conseils d'apprentissage
    result['learning_tips'] = get_learning_tips(concept, subject)
    
    return result


def simplify_explanation(explanation: str) -> str:
    """Simplifie une explication pour un niveau débutant."""
    # Remplace les termes complexes par des termes simples
    replacements = {
        'stipule': 'dit',
        "s'applique": 'concernent',
        'hypoténuse': 'le côté le plus long',
        'proportionnalité': 'une relation directe',
        'bouleversements': 'grands changements',
        'monarchie absolue': 'un roi avec tous les pouvoirs',
        'conflit': 'guerre',
        'transformation': 'changement',
        'convertis': 'transformés',
        'mesure': 'indique'
    }
    
    simplified = explanation
    for complex_term, simple_term in replacements.items():
        simplified = simplified.replace(complex_term, simple_term)
    
    return simplified


def get_advanced_details(concept: str, subject: str) -> str:
    """Ajoute des détails techniques pour un niveau avancé."""
    details = {
        ('théorème de pythagore', 'maths'): "Ce théorème est valable dans les espaces euclidiens. "
                                          "Il existe une généralisation en dimension supérieure appelée "
                                          "le théorème de Pythagore généralisé.",
        ('fonction affine', 'maths'): "La représentation graphique d'une fonction affine est une droite. "
                                     "Le coefficient a représente la pente de la droite, et b l'ordonnée à l'origine.",
        ('loi de newton', 'physique'): "Ces lois sont fondamentales en mécanique classique. "
                                       "La troisième loi stipule que pour chaque action, il existe une réaction "
                                       "égale et opposée.",
        ('énergie cinétique', 'physique'): "L'énergie cinétique est une forme d'énergie mécanique. "
                                           "Elle est conservée dans les collisions élastiques.",
        ('réaction chimique', 'chimie'): "Les réactions chimiques peuvent être exothermiques (dégagent de la chaleur) "
                                         "ou endothermiques (absorbent de la chaleur).",
        ('révolution française', 'histoire'): "La Révolution française a été influencée par les idées des Lumières "
                                              "et a eu un impact majeur sur toute l'Europe."
    }
    
    return details.get((concept, subject), "")


def get_learning_tips(concept: str, subject: str) -> List[str]:
    """Retourne des conseils pour apprendre ce concept."""
    tips = {
        ('théorème de pythagore', 'maths'): [
            "Dessinez des triangles rectangles et mesurez les côtés pour vérifier le théorème",
            "Apprenez la formule par cœur : a² + b² = c²",
            "Entraînez-vous avec des exercices de calcul de longueurs"
        ],
        ('fonction affine', 'maths'): [
            "Tracez des droites dans un repère pour visualiser les fonctions affines",
            "Calculez la pente entre deux points pour trouver le coefficient a",
            "Résolvez des problèmes concrets (vitesse, coût, etc.)"
        ],
        ('loi de newton', 'physique'): [
            "Faites des expériences avec des objets en mouvement",
            "Observez comment les forces affectent le mouvement",
            "Étudiez des exemples concrets (voitures, ballons, etc.)"
        ],
        ('réaction chimique', 'chimie'): [
            "Équilibrez des équations chimiques simples",
            "Observez des réactions chimiques dans la vie quotidienne (combustion, rouille, etc.)",
            "Utilisez des schémas pour représenter les réactions"
        ]
    }
    
    return tips.get((concept, subject), [
        "Relisez votre cours attentivement",
        "Faites des schémas ou des résumés",
        "Posez des questions à votre professeur si quelque chose n'est pas clair"
    ])


def explain_with_examples(concept: str, subject: Optional[str] = None, 
                         num_examples: int = 2) -> Dict[str, str]:
    """
    Explique un concept avec des exemples concrets.
    
    Args:
        concept: Concept à expliquer
        subject: Matière
        num_examples: Nombre d'exemples à fournir
        
    Returns:
        Dictionnaire avec l'explication et les exemples
    """
    explanation = explain_concept(concept, subject)
    
    # Sélectionne un nombre limité d'exemples
    examples = explanation.get('examples', [])
    selected_examples = random.sample(examples, min(num_examples, len(examples))) if examples else []
    
    # Ajoute des exemples générés si nécessaire
    while len(selected_examples) < num_examples:
        generated = generate_example(concept, subject)
        if generated and generated not in selected_examples:
            selected_examples.append(generated)
    
    result = {
        'concept': concept,
        'explanation': explanation.get('explanation', ''),
        'examples': selected_examples,
        'subject': explanation.get('subject', subject or 'inconnu')
    }
    
    return result


def generate_example(concept: str, subject: Optional[str] = None) -> Optional[str]:
    """Génère un exemple pour un concept donné."""
    concept = concept.lower()
    
    example_templates = {
        ('théorème de pythagore', 'maths'): [
            "Un triangle rectangle avec des côtés de {a} cm et {b} cm a une hypoténuse de {c} cm.",
            "Pour calculer la longueur manquante d'un triangle rectangle, utilisez a² + b² = c²."
        ],
        ('fonction affine', 'maths'): [
            "La fonction f(x) = {a}x + {b} est une fonction affine avec une pente de {a}.",
            "Si une voiture roule à vitesse constante, la distance parcourue est une fonction affine du temps."
        ],
        ('énergie cinétique', 'physique'): [
            "Un objet de masse {m} kg se déplaçant à {v} m/s a une énergie cinétique de {ec} J.",
            "Plus un objet va vite, plus son énergie cinétique est grande."
        ]
    }
    
    if subject:
        key = (concept, subject.lower())
    else:
        key = (concept, None)
    
    templates = example_templates.get(key, [])
    if templates:
        return random.choice(templates)
    
    return None
