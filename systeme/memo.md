# Memo système

Structure de stockage de données : **Pile** & **Tas**

**Tas :** variables allouées dynamiquements, partagé par les threads et processus.

**Pile :** Variables temporaires du programme.

**Système d'exploitation :** ensemble de programme qui gèrent les capacités d'un ordinateur. Il fait partie de la couche noyau, et veille à la bonne utilisation des ressources (mémoires, processeurs, périphériques, etc.).

**Programme :** Code décrivant une tâche.

**Processeur :** Automate électronique de traitement.

**Processus :** Programme exécuté par un processeur.

**Thread :** Unité d'ordonnancement, qui dispose de sa pile et de son contexte d'appel.

**Sémaphore :** Contient une liste de processus en attente d'une ressource, d'une fonction `Prendre` et `Vendre`, devant être appelée par tout processus avant d'entrer / terminer sa section critiquer pour "tenter" de prendre / rendre la ressource pour d'autres processus.

**Tube :** Un tube est un canal de communication entre 2 processus, qui comportent 2 frichiers, afin d'écrire et lire des données.

**FP :** Fixed priorities

**FP Préemptif :** Exécution **peut** être interrompue.

**FP Non-préemptif :** Exécution **ne peut pas** être interrompue.

**FIFO (First In First Out) :** Ordonnancement dynamique, plus la date d'activation d'un processus est ancienne, plus celui-ci est prioritaire.

**FP/FIFO :** Comme FIFO mais avec les Fixed Priorities pour chaque processus.

**RR (Round Robin) :** Tranche de temps d'éxécution aux processus, à tour de rôle, de façon égale, sans accorder de priorité.

**EDF (Earliest Deadline First) :** La priorité d'une tâche est alors d'autant plus grande que son échéance est proche.
