# Séries de Fourier

## Définition

$T$ : période de la fonction $f(t)$

## Développable ?

- $f(t)$ est périodique de période $T$
- $f(t)$ est intégrable sur un intervalle de longueur $T$
- $f(t)$ est continue par morceaux


## Paire ou impaire

- Paire : $f(-t) = f(t)$

_En gros symétrique par rapport à l'axe des ordonnées._

- Impaire : $f(-t) = -f(t)$

_En gros symétrique par rapport à l'origine._

- Si $f(t)$ est paire, alors $b_n = 0$.
- Si $f(t)$ est impaire, alors $a_n = 0$, donc $a_0 = 0$.

## Formulaires

### Coefficients de Fourier trigonométriques :

#### Valeur moyenne de la fonction

Si $f(t)$ est **paire**, alors :

$a_0 = \frac{4}{T} \int_0^{T/2} f(t) dt$ 

_On calcule que la moitié de l'aire, et on multiplie par 2._

Si $f(t)$ est **impaire**, alors : 

$a_0 = 0$.

_Car elle s'annule sur la période._

Sinon :

$a_0 = \frac{2}{T} \int_{-T/2}^{T/2} f(t) dt$

#### Reste des coefficients pour $n \geq 1$ :

$a_n = \frac{2}{T} \int_0^T f(t) \cos{(nwt)} dt$

$b_n = \frac{2}{T} \int_0^T f(t) \sin{(nwt)} dt$

avec :

$T = \frac{2\pi}{w}$ donc $w = \frac{2\pi}{T}$

### Série de Fourier :

$(S_f)_N(t) = a_0 + \sum_{n=1}^{\infty} [a_n \cos{(nwt)} + b_n \sin{(nwt)}] = f(t)$

### Coefficients de Fourier complexes :

$C_n = \frac{1}{T} \int_0^T f(t) e^{-inwt} dt$