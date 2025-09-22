# Contribuer au projet

Merci de votre intérêt pour ce projet!\
Ce guide explique comment proposer des idées, signaler des bugs et soumettre des modifications.

## Avant de commencer
- Lisez le [README](./README.md), bien entendu, pour savoir commenter installer et démarrer le projet localement.
- Recherchez dans les **Issues** et **Pull Requests** existantes pour éviter les doublons.

## Signaler un bug
1. Ouvrez une **Issue** avec le gabarit `Rapport de Bug`.
2. Remplissez l'**Issue** avec le plus d'information possible.
3. Ajoutez des labels pertinents (`bug`, `help wanted`, `good first issue`, etc.).

## Proposer une amélioration
1. Ouvrez une **Issue** `Demande de fonctionnalité` pour discuter de l’idée.
2. Remplissez l'**Issue** avec le plus d'information possible.

## Stratégie de branches
- **main**: branche stable (déploiements/tags).
- **Branches de travail**: feat/courte-description, bug/courte-description, chore/....

## Workflow de contribution
1. Créez une branche depuis main.
2. Faites des commits atomiques et clairs.
3. Mettez à jour/ajoutez des tests et la documentation.
4. Vérifiez la qualité :
    - Assurez vous que le style de votre nouveau code est uniforme avec le reste du projet.
    - Lancer les tests unitaires et d'intégration.
5. Rebase proprement sur la branche cible si nécessaire:
    ```shell
    git fetch origin
    git rebase origin/main
    ```
6. Ouvrez une *Pull Request* vers la branche `main`.

## Check-list Pull Request
- [ ] L’Issue liée est référencée.
- [ ] Tests ajoutés/mis à jour et passent.
- [ ] Lint/formatage OK.
- [ ] Documentation mis à jour si nécessaire.
- [ ] Pas de secrets/credentials dans le diff.
- [ ] Captures d’écran ou GIF si l’UI est modifiée.

## Revue de code
- Soyez respectueux et précis.
- Préférez des commentaires actionnables.
- Les relecteurs peuvent demander des changements en laissant des commentaires dans la **Pull Request**.

## Tests & Qualité
- Ajoutez des tests unitaires pour chaque nouvelle fonctionnalité.
- Maintenez ou améliorez la couverture de test.
- Suivez les conventions de style.

## Sécurité
- Ne divulguez pas de vulnérabilités publiquement.
- Utilisez [Security Advisories](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability) de GitHub.

## Remerciements
> Merci à toutes les contributrices et tous les contributeurs!
