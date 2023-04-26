## Model-Aware Contrastive Learning: Towards Escaping Dilemmas

![](fig1.jpeg)

## Citing:
If you use MACL in your research or wish to refer to the baseline results published here, please use the following BibTeX entry.

```BibTeX
@inproceedings{ICML23_MACL,
      title={Model-Aware Contrastive Learning: Towards Escaping the Dilemmas},
      author={Huang Zizheng and Chen Haoxing and Wen Ziqi and Zhang Chao and Li Huaxiong and Wang Bo and Chen Chunlin},
      booktitle={International Conference on Machine Learning},
      year={2023}
}
```


## Todo list:
- [x] Release core code of MACL.
- [x] Pre-trained models.

## Pre-trained Models
We have uploaded pre-trained models of [SimCLR-256-e800](https://huggingface.co/HaoxingChen/MACL_ICML23/tree/main/simclr_256_e800) and [SimCLR-2048-e200](https://huggingface.co/HaoxingChen/MACL_ICML23/tree/main/simclr_2048_e200). You can choose them as you need through the links.

## Model Performance
Top1 linear evaluation accuracies on ImageNet1K:

Batch size | 256 | 512 | 1024 | 2048
--- |:---:|:---:|:---:|:---:
SimCLR | 61.9 | 64.0 | 65.3 | 66.1 
w/ MACL |  **64.3**| **65.2** | **66.5** | **66.9**

Sentence embedding performance on STS tasks:

STS Tasks | STS12| STS13 | STS14 | STS15 | STS16 | STSB  | SICKR | Avg. 
--- |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
SimCSE-BERT | **68.40** | 82.41  | 74.38  | 80.91  | 78.56  |76.85  | 72.23  | 76.25  
SimCSE-BERT+MACL | 67.16 | **82.78** | **74.41**| **82.52**| **79.07**| **77.69**| **73.00**| **76.66**
SimCSE-RoBERT | 70.16  | **81.77** | 73.24  | 81.36 | 80.65 | 80.22 | 68.56 | 76.57 
SimCSE-RoBERT+MACL|**70.76** | 81.43  |**74.29** |**82.92** |**81.86** |**81.17** |**70.70**|**77.59**

Graph representation learning performance:
Dataset | NCI1  | PROTEINS | MUTAG| RDT-B | DD | IMDB-B
--- |:---:|:---:|:---:|:---:|:---:|:---:
GraphCL | 77.87 | 74.39 | 86.80| 89.53| 78.62| 71.14
w/ MACL | **78.41**| **74.47**| **89.04**| **90.59**| **78.80**|**71.42**

## Contacts
Please feel free to contact us if you have any problems.

Email: [hx.chen@hotmail.com](hx.chen@hotmail.com) or [zizhenghuang@smail.nju.edu.cn](zizhenghuang@smail.nju.edu.cn)


## Acknowledgement
Many thanks to the nice work of [MMSelfsup](https://github.com/open-mmlab/mmselfsup). Our codes and configs follow [MOCO](https://github.com/facebookresearch/moco) and [SimCLR](https://github.com/google-research/simclr).


