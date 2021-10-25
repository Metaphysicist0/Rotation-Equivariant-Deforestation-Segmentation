# Rotation Equivariant Deforestation Segmentation

This is a PyTorch implementation of a rotation equivariant U-Net model for segmentation and classification of deforestation areas as described in our paper:



## Installation

python setup.py install

## Requirements

## Data

The dataset used in this project is from https://stanfordmlgroup.github.io/projects/forestnet/ and can be dowloaded from their page.

Download the dataset into the roteqseg folder and unzip:

```
unzip ForestNetDataset.zip
```

## Run the examples

We provide both a non-rotation equivariant model and a rotation equivariant model to allow a comparison to be made between the two models.

```
cd roteqseg
mkdir Outputs
python trainer.py --savedir 'code_test' --epochs 12 --model 'unet'
python trainer.py --savedir 'eq_code_test' -- epochs 12 --model 'unet_eq'
```

## Cite

Please cite our paper if you make use of our work:




