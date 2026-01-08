# Projet ML : Classification d'emails Spam / Ham avec Naive Bayes

## Description du projet
Ce projet est une implémentation d'un pipeline de **Machine Learning** pour classifier des emails en **spam** ou **ham** (non spam) en utilisant le modèle **Naive Bayes Multinomial**.  

Le projet illustre les bonnes pratiques suivantes :  
- Lecture et traitement de données brutes (emails)  
- Préprocessing et nettoyage des textes  
- Construction de dataset et vectorization avec un vocabulaire défini  
- Entraînement, évaluation et sauvegarde du modèle et du vectorizer  
- Prédiction end-to-end sur de nouveaux emails  

---

## Prérequis
Avant d'utiliser le projet, vous devez :  
1. Installer les packages listés dans `requirements.txt` :  
   ```bash
   pip install -r requirements.txt
2. Préparer les fichiers d'emails bruts pour ham et spam (non inclus dans ce repo, trop volumineux). Vous pouvez les télécharger depuis une source publique d’emails spam/ham (par exemple SpamAssassin Public Corpus
) et les placer dans le dossier data/raw/ham et data/raw/spam.

### Post-condition
Une fois l'environnement configuré, vous pouvez lancer le pipeline complet (entraînement et test) via le point d'entrée principal avec la commande standard.

`python main.py`
## Pipeline du projet
Le projet est structuré pour suivre une pipeline ML complète :
1. Lecture des emails
- Chaque fichier est lu depuis les dossiers **ham** et **spam**.
- Le contenu complet de l’email est récupéré avec son label associé **(0 pour ham, 1 pour spam)**.
2. Extraction du body et preprocessing
- Extraction du body et preprocessing
- Nettoyage du text:
    - Remplacement des caractères invalides
    - Remplacement des caractères invalides
    - Suppression  des mots vides (stopwords)
- Les données nettoyées peuvent être sauvegardées dans différents formats via le DatasetManager.
3. Vectorization
- Utilisation de **CountVectorizer** pour transformer les emails en vecteurs numériques.
- Définition d’un vocabulaire global à partir de tout le dataset.
- Chaque email est transformé selon ce vocabulaire pour être utilisable par le modèle.
4. Entraînement et évaluation
- Entraînement du modèle Naive Bayes Multinomial sur le train set.
- Prédiction sur le test set et calcul des métriques d’évaluation :
    - Accuracy : 0.96
    - Precision : 1.0
    - Recall :  0.78
    - F1-Score : 0.87
    - Matrice de confusion :   
| | Predicted Ham | Predicted Spam |
| :--- | :---: | :---: |
| **Actual Ham** | **511** (VN) | 0 (FP) |
| **Actual Spam** | 22 (FN) | **78** (VP) |

5. Sauvegarde du modèle
- Après validation, le modèle entraîné est sauvegardé dans models/.
- Le vectorizer associé est également sauvegardé pour assurer la cohérence lors de nouvelles prédictions.

6. Prédiction sur de nouveaux emails (end-to-end test)
- Récupération du contenu d’un email test depuis **data/test/**.
- Préprocessing complet du texte (body + nettoyage).
- Transformation via le vectorizer.
- Transformation via le vectorizer.
- Affichage de résultat :
| Chemin du Fichier | Contenu Prédit | Statut |
| :--- | :--- | :--- |
| `test/spam.txt` | **SPAM** | ✅ Succès |
| `test/ham.txt` | **HAM** | ✅ Succès |

---

## Structure du projet
```text
project_root/
├── 📁 data/
│   ├── 📄 raw/            # Emails bruts (Ham & Spam) pour l'entraînement
│   ├── 📄 processed/      # Datasets nettoyés et prêts pour le modèle
│   └── 📄 test/           # Fichiers .txt pour tests end-to-end
├── 📁 models/             # Modèles (.pkl) et vectoriseurs sauvegardés
├── 📁 src/                # Code source de l'application
│   ├── 📁 core/           # Logique métier fondamentale
│   │   ├── 📂 dataset/       # Gestion du chargement (Reader, Manager)
│   │   ├── 📂 preprocessing/ # Nettoyage de texte (Stopwords, Lemmatisation)
│   │   ├── 📂 features/      # Extraction de caractéristiques (Tf-Idf/BoW)
│   │   └── 📂 model/         # Implémentation du Naive Bayes
│   └── 📁 services/       # Couche d'abstraction pour les prédictions
├── 🐍 main.py             # Point d'entrée unique (Pipeline Manager)
├── 📋 requirements.txt    # Dépendances du projet
└── 📖 README.md           # Documentation du projet


