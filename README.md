# Metrics A25

**Groupe**: 01 | **Équipe**: 10

Répertoire de code pour la compagnie MTL-MobilitySoft dans le cadre du cours LOG680 - Introduction à l'approche DevOps.

## Pré-requis

Afin de faire fonctionner ce projet sur votre machine, il est important d'avoir les outils suivants d'installés :

- Python 3.13.7
- NPM

  ```bash
  git clone https://github.com/cjayneb/metrics-a25-grp1-eq10.git
  cd metrics-a25-grp1-eq10
  ```

2. **Créer et activer un environnement virtuel**

   ```bash
    python -m venv .venv
    source .venv/bin/activate   # Sur Linux/Mac
    .venv\Scripts\activate      # Sur Windows
   ```

3. **Installer les dépendances**

   ```bash
    pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement**\
   Créer un fichier `.env` à la racine du projet avec votre jeton GitHub :
   ```env
    GITHUB_TOKEN=your_personal_access_token
   ```

## Exécuter le projet

### Lancer l'API localement avec Python

```bash
    python src/app.py
```

Cela démarre le serveur Flask sur http://127.0.0.1:5000.

- Racine de l'API : http://127.0.0.1:5000/
- Endpoint des issues : http://127.0.0.1:5000/issues
- Documentation Swagger : http://127.0.0.1:5000/docs

### Lancer les test unitaires et d'intégration avec couverture de code

```bash
    python -m pytest --cov=src
```

### Générer un rapport HTML de couverture de code

```bash
    coverage html
```

Ce rapport permet de voir exactement quelle partie du code manque de tests.

## Déployer le projet

Le déploiement automatique est fait par **Vercel** à chaque fois que vous poussez des changements sur une branche. Tous les déploiements sont accessibles à partir de cette page : https://vercel.com/cjaynebs-projects/metrics-a25-grp1-eq10/deployments

> **_NOTE:_** Demander l'accès à [Jean-Christophe Benoît](https://github.com/cjayneb)

Cependant, il est aussi possible de faire un déploiement manuel du code poussé de votre branche actuelle en suivant les étapes suivantes :

1. **Installer Vercel CLI**

   ```bash
      npm i -g vercel
   ```

2. **Se connecter à Vercel**

   ```bash
      vercel login
   ```

3. **Déployer l'application sur Vercel**

   ```bash
      vercel .
   ```

   Cliquer sur le lien _Preview_ pour voir l'application dans votre naviguateur.

## Documentation

Se référer à la documentation officielle du projet située dans le [Wiki](https://github.com/cjayneb/metrics-a25-grp1-eq10/wiki).

## Contribuer au projet

Pour contribuer à ce projet, se référer au document [CONTRIBUTING.md](./CONTRIBUTING.md).

## Auteurs

- [Adam Mihajlovic](https://github.com/Funnyadd)
- [Jean-Christophe Benoît](https://github.com/cjayneb)
- [Jethro Roy](https://github.com/JethroRoy)
