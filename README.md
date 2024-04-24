# 📚 Mistrík's measure of readability 📚
 ![Python](https://img.shields.io/badge/python-3.x-blue.svg)  [![wheel](https://img.shields.io/badge/wheel-yes-ff00c9.svg)](https://test.pypi.org/project/mistrik/)  [![PyPI Latest Release](https://img.shields.io/pypi/v/pandas.svg)](https://test.pypi.org/project/mistrik/) [![PyPI Downloads](https://img.shields.io/pypi/dm/pandas.svg?label=PyPI%20downloads)](https://test.pypi.org/project/mistrik/) 
 [![MIT license](https://img.shields.io/badge/License-MIT-green.svg)](https://lbesson.mit-license.org/) 

## What is it?
**Mistrík** is a pure Python package that scores the readability of text using the Mistrík's measure of readability and comprehension. The Mistrík’s readability formula is calculated using the _Phrase Repetition Index_. This implies that a text becomes easier to read the more words it repeats. The metric can be used to measure the readability index (R) of Slovak texts, textbooks, research papers and many more. 
The original research by Jozef Mistrík can be found [here](https://www.juls.savba.sk/ediela/sr/1968/3/sr1968-3-lq.pdf#page=46) (pp.171-178). 📑

### Why we made this? 🤔
Readability measures are somewhat common in Slovakia, but not as widespread as they are abroad. Our goal was to support the use of readability measures, especially Mistrík’s, by creating an open-source Python library, _since there is still no library or tool that we can freely use for texts or for research._ 🙃 
At the same time, we wanted to make this metric _more accessible_ because improving reading comprehension skills not only improves comprehension but also supports lifelong learning by enabling individuals to effectively absorb informa- tion in a variety of areas. 📈

## 💿 Getting started - installation: 💿
```python
pip install

from Mistrik import readability
```

## Examples of use: 🧑🏻‍💻👩🏻‍💻 
_Note:_ The readability metric provides a `score` attribute.

_Note <sup>2</sup>:_ In all examples below `r` is:

```python
r = readability.mistrik_readability(text)
```
You have the option of saving the chosen text in its text variable (e.g., text) or loading the text from a specified file to apply the metric to this variable.

### def mistrik_readability() :

```python
"""
The function returns a number of sentences, V = average length of sentences in number of words,
S = average length of words in number of syllables, I = word repetition index, R =readability score, 
  @param:
         text (str): The text for which the readability rate is to be calculated.
  @returns:
         int: number of sentences,
         int: V, S, I 
         int/float: Measure of text readability according to the Mistrík formula.
  @raises:
         ValueError: If the input text is an empty string.
"""
text = "Morfológia čiže tvaroslovie je jazykovedná náuka o gramatických tvaroch
slov, ako aj o slovách, ktoré majú funkciu tvarov. Morfológia je teda náuka
o tvarovej rovine v systéme jazyka."

r = readability.mistrik_readability(text)
```
#### Output: 
```{r df-drop-ok, class.source="bg-success"}
MISTRIK READABILITY METRIC:
SENTENCES:  2
V:  14 (14.0)
S:  2.3 (2.321)
N:  28
L:  23
I:  1.217
R:  24 (23.541)
24
```
## License

[📜 MIT](LICENSE)

## Supoort us 🌟
<a href="[[[https://www.buymeacoffee.com/m97tA5c](https://buymeacoffee.com/ducducdevs)]" target="_blank](https://buymeacoffee.com/ducducdevs
)"><img src="https://bmc-cdn.nyc3.digitaloceanspaces.com/BMC-button-images/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>
