# 🪕🪕🪕
[![npm version](https://badge.fury.io/py/fixml.svg)](https://badge.fury.io/js/nub-auth)
[![npm](https://img.shields.io/pypi/dm/fixml.svg)]()
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

A Small tools to perform specific tasks across NLP and computer vision domain.

Fixml is intended to be used for problems like, spelling correction, punctuation, comprehension, etc.

List of features avaliable:
* Questions and Answers
* Summarization
* Punctuation
* Spelling Correction

---------------------------
## 🚀 Usage
**Below is a quick way to get up and running with the model.**
1. First, install the package.
```bash
pip install fixml
```
2. Sample python code.
```python
from fixml import FixPunctuation
# The default language is 'english'
punct = FixPunctuation()
punct.punctuate("""in 2018 cornell researchers built a high-powered detector that in combination with an algorithm-driven process called ptychography set a world record
by tripling the resolution of a state-of-the-art electron microscope as successful as it was that approach had a weakness it only worked with ultrathin samples that were
a few atoms thick anything thicker would cause the electrons to scatter in ways that could not be disentangled now a team again led by david muller the samuel b eckert
professor of engineering has bested its own record by a factor of two with an electron microscope pixel array detector empad that incorporates even more sophisticated
3d reconstruction algorithms the resolution is so fine-tuned the only blurring that remains is the thermal jiggling of the atoms themselves""")
# Outputs the following:
# In 2018, Cornell researchers built a high-powered detector that, in combination with an algorithm-driven process called Ptychography, set a world record by tripling the
# resolution of a state-of-the-art electron microscope. As successful as it was, that approach had a weakness. It only worked with ultrathin samples that were a few atoms
# thick. Anything thicker would cause the electrons to scatter in ways that could not be disentangled. Now, a team again led by David Muller, the Samuel B. 
# Eckert Professor of Engineering, has bested its own record by a factor of two with an Electron microscope pixel array detector empad that incorporates even more
# sophisticated 3d reconstruction algorithms. The resolution is so fine-tuned the only blurring that remains is the thermal jiggling of the atoms themselves.
```

-----------------------------------------------
## 🎯 

More readme info coming!!!
-----------------------------------------------
## ☕ Connect with contributors 
Contact [Kolade Gideon](kolade199@gmail.com) for questions, feedback and/or requests for new feature.

-----------------------------------------------
