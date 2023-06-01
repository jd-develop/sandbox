# Letter sequences calculator.
_________________________
 This programs calculates the occurrences of couple of letters in words from a list.
 It transforms accents to normal characters (`ãëìôù` becomes `aeiou`)

## Examples
 * `["hello", "world"]` -> main.py -> `{"he": 1, "el": 1, "ll": 1, "lo": 1, "o": 1, "wo": 1, "or":1, "rl": 1, "ld": 1, "d": 1}`
 * `["this", "is", "a", "sëntênce"]` -> main.py -> `{'th': 1, 'hi': 1, 'is': 2, 's': 2, 'a': 1, 'se': 1, 'en': 2, 'nt': 1, 'te': 1, 'nc': 1, 'ce': 1, 'e': 1}`

## For French words
 I used [this file](https://www.pallier.org/liste-de-mots-francais.html) for calculating occurrences of French words. (oui, oui, baguette)
 (I'm laughing about myself because I'm French)
