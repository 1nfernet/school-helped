# School Helper - Mini IA 100% Python pour les lycéens

🎓 **School Helper** est une mini IA développée en Python pur pour aider les lycéens dans leurs cours. Elle offre plusieurs fonctionnalités pour faciliter l'apprentissage et la révision.

## ✨ Fonctionnalités

### 📝 Résumer des cours
- Résumer un texte long en quelques phrases
- Extraire les points clés d'un cours
- Identifier les mots-clés importants
- Adapter le résumé selon la matière

### 💡 Expliquer des concepts
- Expliquer des concepts de manière simple et claire
- Fournir des exemples concrets
- Adapter l'explication au niveau de l'élève (débutant, intermédiaire, avancé)
- Base de connaissances intégrée pour plusieurs matières

### 📚 Générer des exercices
- Créer des exercices aléatoires par matière
- Générer des QCM (Questions à Choix Multiples)
- Produire des quiz complets
- Générer des exercices de maths spécifiques (algèbre, géométrie, analyse)
- Adapter la difficulté (facile, moyen, difficile)

### 🔄 Réécrire et simplifier des cours
- Réécrire un texte avec des mots différents
- Simplifier un texte complexe
- Étendre un texte avec plus de détails
- Adapter le style (formel, informel, technique)
- Réécrire un cours pour une audience spécifique

## 📦 Installation

### Prérequis
- Python 3.7 ou supérieur

### Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/piloroRARE/school-helped.git
   cd school-helped
   ```

2. **Aucune dépendance externe n'est requise** ! Le projet fonctionne avec les bibliothèques standard de Python.

3. **Lancer le programme** :
   ```bash
   python main.py
   ```

## 🚀 Utilisation

### Mode interactif
Lancez simplement le programme sans arguments pour entrer dans le mode interactif :
```bash
python main.py
```

Ou avec l'option `--interactive` :
```bash
python main.py --interactive
```

Dans le mode interactif, vous pouvez utiliser les commandes suivantes :
- `summarize <texte>` - Résume le texte fourni
- `explain <concept> [in <matière>]` - Explique un concept
- `exercise <matière> [difficulté]` - Génère un exercice
- `rewrite <texte>` - Réécrit le texte
- `simplify <texte>` - Simplifie le texte
- `help` - Affiche l'aide
- `quit` - Quitte le programme

### Utilisation en ligne de commande

#### Résumer un texte
```bash
python main.py summarize --text "Le théorème de Pythagore stipule que..."
python main.py summarize --text "..." --ratio 0.2 --max-sentences 3
```

#### Expliquer un concept
```bash
python main.py explain --concept "théorème de pythagore" --subject maths
python main.py explain --concept "loi de newton" --subject physique --level débutant
python main.py explain --concept "révolution française" --subject histoire --examples 3
```

#### Générer un exercice
```bash
python main.py exercise --subject maths --difficulty moyen
python main.py exercise --subject physique --type qcm
python main.py exercise --subject maths --quiz 10  # Génère un quiz de 10 questions
python main.py exercise --subject maths --math-type algebra --difficulty difficile
```

#### Réécrire un texte
```bash
python main.py rewrite --text "Le cours est complexe..." --mode simplify
python main.py rewrite --text "..." --mode expand --level 3
python main.py rewrite --text "..." --style formel
```

## 📚 Matières supportées

- **Mathématiques** : Théorème de Pythagore, fonctions affines, équations du second degré, etc.
- **Physique** : Lois de Newton, énergie cinétique, etc.
- **Chimie** : Réactions chimiques, pH, etc.
- **Histoire** : Révolution française, Première Guerre mondiale, etc.
- **Français** : Conjugaison, grammaire, etc.
- **Anglais** : Vocabulaire, grammaire, etc.
- **Biologie** : Concepts de base
- **Philosophie** : Concepts philosophiques

## 🎯 Niveaux de difficulté

- **Facile** : Exercices simples, concepts de base
- **Moyen** : Exercices standards, concepts intermédiaires
- **Difficile** : Exercices complexes, concepts avancés

## 📂 Structure du projet

```
school-helped/
├── main.py                 # Point d'entrée principal
├── school_helper/
│   ├── __init__.py         # Package principal
│   ├── summarizer.py       # Module de résumé
│   ├── explainer.py        # Module d'explication
│   ├── exercise_generator.py # Module de génération d'exercices
│   └── rewriter.py         # Module de réécriture
├── data/                   # Données et exemples
├── requirements.txt        # Dépendances (aucune !)
└── README.md               # Documentation
```

## 🔧 Personnalisation

Vous pouvez facilement étendre les fonctionnalités du projet :

1. **Ajouter une nouvelle matière** : Modifiez le fichier `explainer.py` pour ajouter de nouveaux concepts dans la `KNOWLEDGE_BASE`.

2. **Ajouter des exercices** : Modifiez le fichier `exercise_generator.py` pour ajouter de nouveaux exercices dans la `EXERCISE_DATABASE`.

3. **Ajouter des synonymes** : Modifiez le fichier `rewriter.py` pour ajouter de nouveaux synonymes dans le dictionnaire `SYNONYMS`.

## 💡 Exemples concrets

### Exemple 1 : Résumer un cours
```bash
python main.py summarize --text "Le théorème de Pythagore s'applique aux triangles rectangles. Il stipule que le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés. Ce théorème est très utile en géométrie pour calculer des longueurs."
```

### Exemple 2 : Expliquer un concept
```bash
python main.py explain --concept "théorème de pythagore" --subject maths --level débutant
```

### Exemple 3 : Générer un quiz
```bash
python main.py exercise --subject maths --quiz 5 --difficulty moyen
```

### Exemple 4 : Simplifier un texte
```bash
python main.py rewrite --text "Le théorème de Pythagore, qui est un principe fondamental en géométrie, stipule que, dans un triangle rectangle, le carré de l'hypoténuse est égal à la somme des carrés des deux autres côtés." --mode simplify
```

## 🎓 Conseils pour les lycéens

1. **Pour réviser efficacement** : Utilisez la fonction de résumé pour créer des fiches de révision.

2. **Pour comprendre un concept** : Utilisez la fonction d'explication avec le niveau adapté à votre compréhension.

3. **Pour vous entraîner** : Générez des exercices et des quiz pour tester vos connaissances.

4. **Pour simplifier un cours** : Utilisez la fonction de simplification pour rendre un texte complexe plus accessible.

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le dépôt
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`)
3. Commitez vos changements (`git commit -m 'Ajout de ma fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/ma-fonctionnalité`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- À tous les lycéens qui utilisent ce programme pour réussir leurs études
- Aux enseignants qui inspirent leurs élèves
- À la communauté open source pour ses contributions inestimables

---

**School Helper** - Votre assistant personnel pour réussir au lycée ! 🎓✨
