# Logique

## Séquent valide

### Sémantique

- Validité : Faire la table de vérité et prouver qu'une ligne est vraie
- Tautologie : Une formule qui est toujours vraie

### Logique minimale

Résoudre le séquent avec les règles de la logique minimale `hypothèse`, `modus ponens`, `inclusion`.

## Algorithme de Davis-Putnam

- `∧` : **AND** (conjonction)
- `∨` : **OR** (disjonction)
- `¬` : **NOT** (négation)
- `_` : **vide**

Il faut que les hypothèses soient sous forme normale **disjonctive (OR ou `∨`)**.

**Formule importante :** `A ⇒ B <=> ¬A ∨ B`.

1. Supprimer les clauses **unitaires**, c'est-à-dire les clauses qui ne contiennent qu'un littéral. Par exemple, si on a la clause `A`, on peut supprimer toutes les clauses contenant `A`, et enlever les littéraux `¬A` des autres clauses (sans les sipprimer).
2. Supprimer les **littéraux purs**, c'est-à-dire les littéraux qui n'apparaissent qu'avec une seule polarité (soit toujours positifs, soit toujours négatifs). Par exemple, si `B` n'apparaît que sous la forme `B` et jamais sous la forme `¬B`, on peut **supprimer** toutes les clauses contenant `B`.
3. Effectuer une résolution sur un littéral quelconque `C`. Cela consiste à créer de nouvelles clauses en combinant les clauses contenant `C` avec celles contenant `¬C`, en supprimant `C` et `¬C` de ces clauses respectives. Par exemple, si on a les clauses `(C ∨ D)` et `(¬C ∨ E)`, on crée la nouvelle clause `(D ∨ E)`.
4. Supprimer les éventuelles clauses **unitaires** ou **littéraux purs** générés par la résolution.
5. Répéter les étapes 1 à 4 fois jusqu'à ce qu'on obtienne une contradiction (une clause vide) ou qu'il n'y ait plus de clauses à traiter.
