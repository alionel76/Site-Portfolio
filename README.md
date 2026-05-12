# Portfolio Django 



## 📌 Description 
Petit projet de portfolio réalisé avec le Framework Django


## 📌 Installation 

### 1. Télécharger et installer Python
Visiter le site officiel : [https://www.python.org/downloads/](https://www.python.org/downloads/)

### 2. Créer un environnement virtuel et l'activer
- **Creation** 
```bash
    # A créer de préférence à la racine du projet (confere "project_structure.txt"
    python -m venv nom_de_la_venv
```
- **Activation** 
```bash
    nom_de_la_venv\Scripts\activate             # Windows

    source nom_de_la_venv/bin/activate          # Linux/Mac
```

### 3. Installer les librairies necessaires
```bash
    pip install -r requirements.txt
```

### 4. Appliquer les migrations 
```bash
    python manage.py makemigrations              # 
    
    python manage.py migrate
```

### 5. Créer un Super Utilisateur 
```bash
    python manage.py createsuperuser
```

## 📌 Utilisation
```bash
    # Lancer le serveur
    python manage.py runserver
```
