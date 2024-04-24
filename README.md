# 📚 Mistrík's measure of readability 📚
 ![Python](https://img.shields.io/badge/python-3.x-blue.svg)  [![wheel](https://img.shields.io/badge/wheel-yes-ff00c9.svg)](https://test.pypi.org/project/mistrik/)  [![PyPI Latest Release](https://img.shields.io/pypi/v/pandas.svg)](https://test.pypi.org/project/mistrik/) [![PyPI Downloads](https://img.shields.io/pypi/dm/pandas.svg?label=PyPI%20downloads)](https://test.pypi.org/project/mistrik/) 
 [![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](https://lbesson.mit-license.org/) 

## What is it?
**Mistrík** is a pure Python library/module that scores the readability of Slovak text using Mistrík's measure of readability and comprehension. The Mistrík’s readability formula is calculated using the _Phrase Repetition Index_. This implies that a text becomes easier to read the more words it repeats. The metric can be used to measure the readability index (R) of Slovak texts, textbooks, research papers, and many more. 
The original research by Jozef Mistrík can be found [here](https://www.juls.savba.sk/ediela/sr/1968/3/sr1968-3-lq.pdf#page=46) (pp.171-178). 📑

### Why we made this? 🤔
Readability measures are somewhat common in Slovakia, but not as widespread as they are abroad. Our goal was to support the use of readability measures, especially Mistrík’s, by creating an open-source Python library, _since there is still no public library or tool that focuses on Slovak texts that we can freely use._ 🙃 
At the same time, we wanted to make this metric _more accessible_ because improving reading comprehension skills not only improves comprehension but also supports lifelong learning by enabling individuals to effectively absorb informa- tion in a variety of areas. 📈

### Description of measure 🖊️ 
S = average length of words in number of syllables\
V = average length of sentences in number of words\
N = number of words\
L = number of unique words\
I = word repetition index (I = N/L)\
R = readability score (50 - ((S * V) / I))\

| Score |    Difficulty     |
|:---:|:---:|
|50 - 40| Very Easy         |
| 40-30 | Standard          |
| 30-20 | Fairly Difficult  |
| 20-10 | Difficult         |
| 10-0 |  Very Confusing    |

In practice, this means that a text that scores between 40 and 50 is typical for fairy tales. On the contrary, a text that achieves a score of up to 20 is suitable for experts in the field to which the text relates or for university students.

## 💿 Getting started - installation: 💿
```python
pip install
```

### 📦 Import module: 📦
```python
from mistrik import Mistrik
```

### 👩🏻‍💻 Examples of use: 🧑🏻‍💻 
```python
text = 
"""
Danka a Janka sú sestričky dvojčence a sú navlas
rovnaké. Danka má oči celkom ako Janka, hnedé a veselé
ani gaštančeky. A Janka má vlasy celkom ako Danka,
plavé a ostrihané na ofinu. Ešte aj nosy majú rovnaké:
trošku vyhrnuté a veľmi všetečné.
Danka a Janka sa rovnako aj obliekajú. Danka má
vždy taký istý kabát ako Janka a Janka také isté šaty ako
Danka. Aj čiapky a topánky majú vždy celkom rovnaké.
"""

M = Mistrik(text)
R = M.readability()
print (R)
```
#### Output: 
```{r df-drop-ok, class.source="bg-success"}
MISTRIK MEASURE OF READABILITY:
SENTENCES: 7
SYLLABLES: 143
V: 10 (10.429)
S: 2.0 (1.959)
N: 73
L: 41
I: 1.78
R: 39 (38.523)
```
#### You can also access all variables like this:
```python
M = Mistrik(text)
R = M.readability()
print ("Sentences:",R.SEN," Syllables:",R.SYL)
print ("The readability of the text is:", R.R)
```
#### Output: 
```{r df-drop-ok, class.source="bg-success"}
Sentences: 7  Syllables: 143
The readability of the text is: 39
```

## Support us 🌟

<a href="https://buymeacoffee.com/ducducdevs" target="_blank](https://buymeacoffee.com/ducducdevs
)"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>

## License

[📜 MIT](LICENSE)

