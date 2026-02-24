# 1. Méthode de Newton

Permet de calculer une solution approchée de $f(x) = 0$

On suppose $f$ non-linéaire et dérivable.

Méthode itérative où on construit une suite d'élements $x_0, x_1, ..., x_n$ qui converge vers $x$ tel que $f(x) = 0$

**Intérêt** si $x_0$ est assez proche de la solution, la méthode converge rapidement.

**Utile** pour problèmes d'optimisation ou système d'équations non-linéaires.

## 1. Construction du schéma itératif

$f : \R^n \rightarrow \R^n$

$x \rightarrow f(x) = \begin{pmatrix}
f_1(x) \\
. \\
. \\
f_n(x)
\end{pmatrix}$

$Vi, f_i: \R^n \rightarrow \R$

On utilise un développement limité de $f$ à l'ordre 1, au voisinnage de $x$

$f(x + \Delta x) = f(x) + J(x) \Delta x + o(|\Delta x|)$

Avec $J(x)$ dérivé, différencielle de $f$ en $x$

Jacobienne de $f$ en $x$ :

![matrice jacobienne](./assets/matrice_jacobienne.png)

$\in \R^{n.n}$

---

Avec la méthode de Newton, on cherche $\bar{x} / f(\bar{x}) = 0$

Pour $x$ proche de $\bar{x}$ ($x = \bar{x} + \Delta x$), le développement limité devient :

$0 = f(\bar{x}) + J(x) \Delta x$

---

### Schéma itératif

On défini la suite ($x_k$) de $\R^n$ qui converge vers $\bar{x}$, avec une erreur $\Delta x = x_{k+1} - x_k$

$0 = f(x_k) + J(x_k) (x_{k+1} - x_k)$

### Relation de récurrence

$J(x_k)(x_{k+1} - x_k) = -f(x_k)$

$x_{k+1} - x_k = -J(x_k)^{-1} f(x_k)$

$x_{k+1} = x_k - J(x_k)^{-1} f(x_k)$

Avec $J(x)^{-1}$ inverse de la Jacobienne.

Attention, les $x_k$ désignent ici des vecteurs de $\R^n$ et pas des composants de vecteur.

### Cas particulier

$f: \R \rightarrow \R$

Alors $J(x) = f'(x)$

Et l'équation $y = f(x_k) + f'(x_k)(x_{k+1} - x_k)$ correspond à la tangente de $f$ en $\begin{pmatrix}
x_k \\
f(x_k)
\end{pmatrix}$

$x_{k+1}$ correspond au point où cette tangente coupe l'axe des $x$
.

![formule de recurrence](./assets/formule_de_recurrence.png)

Explications :

On trace la tangeante au point $x_k$. Cette tangente a une intersection avec l'axe des abscices, ce qui donne le point $x_{k+1}$. Puis on récupère la valeur de la fonction en $f(x_{k+1})$, et on trace une tangeante, et etc...

Donc la formule de récurrence vaut :

$x_{k+1} = x_k - \frac{-f(x_k)}{f'(x_k)}$

### Remarque

Dans le cas général, le schéma s'écrit $J(x_k)(x_{k+1} - x_k) = -f(x_k)$ qui est un systèmed linéaire $n*n$

En général on ne calcule pas explicitement $J(x)^{-1}$ mais on résout le système linéaire. (pour des raions de précision numériques)

On pose $S_k = x_{k+1} - x_k$

On calcule $S_k$ mais $x_{k+1}$ se déduit par $x_{k+1} = x_k + S_k$

---

Dans le cas $f: \R \rightarrow \R$, si la dérivée de $f$ n'est pas disponible, on peut remplacer le schéma itératif $f'(x_k)$ par le taux d'accroissement.

Taux d'accroissement : $\frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}$

Le schéma est alors :

$x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}$

### Algorithme

- Cas $f: \R \rightarrow \R$

Choissiez $x_0$ et $k = 0$

repeat {

$x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$

$k = k + 1$

} $until |f(x_k)| < \varepsilon$

---

- Cas $f: \R^n \rightarrow \R^n$

Choissiez $x_0$ et $k = 0$

repeat {

calculer $J(x_k)$

résoudre le système linéaire $J(x_k) S_k = -f(x_k)$

$x_{k+1} = x_k + S_k$

$k = k + 1$

} $until ||f(x_k)|| < \varepsilon$

---

## 2. Critères d'arrêt

- Par exemple $||x_{k+1} - x_k|| < \varepsilon$

- Lorsque solution proche de $0$, le mieux est de prendre l'erreur relative

Erreur relative : $\frac{||x_{k+1} - x_k||}{||x_{k+1}||} < \varepsilon$

- On peut aussi ajouter une limite sur le nombre d'itérations
