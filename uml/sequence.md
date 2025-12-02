# Diagramme de séquence (intération)

### Messages entre les objets

Lors de l'appel d'une fonction, on écrit le labal de la fonction sur l'objet suivant.

- **Message synchrone :** attend une réponse (ligne pleine avec flèche pointue). (ex : `getNom()` qui va renvoyer un `String`)
- **Message asynchrone :** n'attend pas de réponse (ligne pleine avec demi-flèche pointue). (ex : `start()` qui ne renvoie rien)

## Symboles

- **Loop** : boucle (ex : pour chaque élément d'une liste)
- **Alt** : condition (if / else)
- **Opt** : optionnel (if)
- **Ref** : référence à un autre diagramme de séquence

## Messages

- **Création d'instance** : label `<<create>>` vers l'objet créée (activation).
- **Destruction d'instance** : label `<<destroy>>` la ligne de vie de l'objet détruit.
