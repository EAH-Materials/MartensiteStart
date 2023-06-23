# MartensiteStart
## Description
This repository provides a single python class to compute the martensite start temerature *M<sub>s</sub>* in High-Carbon Steels for a variety of common models, including the work described in the paper:

[Ingber, Jerome, and Maik Kunert. "Prediction of the Martensite Start Temperature in High‐Carbon Steels." steel research international 93.5 (2022): 2100576.](https://onlinelibrary.wiley.com/doi/full/10.1002/srin.202100576)

## Usage
Single value
```python
from MartensiteStart import MartensiteStart as Ms

Ms(C = 1.5, Mn = 0.5, Si = 0.8).T['Ingber']
# 14
```
Compare different models
```python
from MartensiteStart import MartensiteStart as Ms
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 10.0, 512)
tc_I = []
tc_P = []
for id, c in enumerate(x):
    t = Ms(C = 0.5, Mn = c).T
    tc_I.append(t['Ingber'])
    tc_P.append(t['Payson & Savage'])

plt.plot(x, tc_I, label = 'Ingber')
plt.plot(x, tc_P, label = 'Payson & Savage')
plt.xlabel('Mn [%]')
plt.ylabel('Ms [K]')
plt.legend()
plt.show(block = True)
```


## Cite

If you use this code in your research, please cite:
```bibtex
@article{ingber2022prediction,
  title={Prediction of the Martensite Start Temperature in High-Carbon Steels},
  author={Ingber, Jerome and Kunert, Maik},
  journal={steel research international},
  volume={93},
  number={5},
  pages={2100576},
  year={2022},
  publisher={Wiley Online Library}
}
```