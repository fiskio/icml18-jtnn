# Junction Tree Variational Autoencoder for Molecular Graph Generation

<img src="https://github.com/wengong-jin/icml18-jtnn/blob/master/paradigm.png" width="400">

Implementation of our Junction Tree Variational Autoencoder [https://arxiv.org/abs/1802.04364](https://arxiv.org/abs/1802.04364)

# Requirements
* Linux (We only tested on Ubuntu)
* RDKit (version >= 2017.09)
* Python (version >= 3.5)
* PyTorch (version >= 0.2)

To install RDKit, please follow the instructions here [http://www.rdkit.org/docs/Install.html](http://www.rdkit.org/docs/Install.html)

We highly recommend you to use conda for package management.

# Quick Start
This repository contains the following directories:
* `jtnn/bo/` includes scripts for Bayesian optimization experiments. Please read `jtnn/bo/README.md` for details.
* `jtnn/molvae/` includes scripts for training our VAE model only. Please read `jtnn/molvae/README.md` for training our VAE model.
* `jtnn/molopt/` includes scripts for jointly training our VAE and property predictors. Please read `jtnn/molopt/README.md` for details.
* `jtnn/jtnn/` contains codes for model formulation.

# Contact
Wengong Jin (wengong@csail.mit.edu)
