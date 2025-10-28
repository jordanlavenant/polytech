# Équations différentielles

## Ordre 1

### Forme homogène

S'écrit sous la forme : $y_h(x)$

* Cas : $y' = ay$

    Solution générale : $y = Ce^{ax}$

* Cas : $y' = ay + b$

    Solution générale : $y = Ce^{ax} - \frac{b}{a}$

### Forme particulière

S'écrit sous la forme : $y_p(x)$

Identifie la forme de $f(x)$ dans l'équation $y' = ay + f(x)$ et applique la règle correspondante :

* Si $f(x) = P_n(x)$ (polynôme de degré $n$) :

    Alors $y_p(x)$ est un polynôme de degré $n$.

Exemples :

- Si $f(x) = 5x^2 + 3x + 1$, alors $y_p(x) = ax^2 + bx + c$
- Si $f(x) = 4x + 7$, alors $y_p(x) = ax + b$
- Si $f(x) = 6$, alors $y_p(x) = a$

### Forme générale

La solution générale de l'équation différentielle s'écrit :

$y(x) = y_h(x) + y_p(x)$

### Exemple

Exemple de résolution complète :

Résoudre l'équation $y' = -y + 2x + 3$.

1. Forme homogène : $y_h = Ce^{-x}$ car :  
    $y' = -y$ $\Rightarrow$ $y = Ce^{-x}$

2. Forme particulière : $y_p = ax + b$ car $f(x) = 2x + 3$ est un polynôme de degré 1.

    On calcule $y_p'$ : $y_p' = a$

    On remplace dans l'équation initiale :

    $a = - (ax + b) + 2x + 3$

    $a = -ax - b + 2x + 3$

    $a = (2-a)x + 3-b$

    $0 = (2-a)x + 3-b-a$

    On identifie les coefficients terme à terme :

    $\begin{cases}
    0 = 2 - a \\
    0 = 3 - b - a
    \end{cases}$

    On résout le système :
    $\begin{cases}
    a = 2 \\
    b = 1
    \end{cases}$

    Donc $y_p = 2x + 1$

Et ainsi la solution générale est :

$y = y_h + y_p = Ce^{-x} + 2x + 1$

## Ordre 2