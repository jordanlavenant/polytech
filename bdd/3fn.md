# 3FN

## Définition

On dit d'une table qu'elle est en **3FN** (Troisième Forme Normale) si elle est en **2FN** et qu'aucun attribut **non clé** ne dépend transitivement de la clé primaire, c'est à dire dépendent d'un **autre attribut non clé**.

## Exemple

| Code Cours | Nom Du Coursa | Code Professeur | Prénom Professeur | Nom Professeur |
| ---------- | ------------- | --------------- | ----------------- | -------------- |
| C001       | Mathématiques | P001            | Alice             | Dupont         |
| C002       | Physique      | P002            | Bob               | Martin         |

Ici, la table est en **2FN** car chaque attribut non clé dépend de la clé primaire (Code Cours).

Cependant, les attributs "Prénom Professeur" et "Nom Professeur" dépendent transitivement de la clé primaire via l'attribut "Code Professeur".

## Résolution

Pour mettre cette table en **3FN**, il faut créer une nouvelle table pour les professeurs :

| Code Professeur | Prénom Professeur | Nom Professeur |
| --------------- | ----------------- | -------------- |
| P001            | Alice             | Dupont         |
| P002            | Bob               | Martin         |

Et modifier la table des cours pour ne garder que le code du professeur :
| Code Cours | Nom Du Cours | Code Professeur |
|------------|--------------|-----------------|
| C001 | Mathématiques| P001 |
| C002 | Physique | P002 |

Ainsi, chaque attribut non clé dépend uniquement de la clé primaire dans chaque table, respectant ainsi la **3FN**.
