# CaBind_MCNN: Identifying Potential Calcium Channel Blocker Targets by Predicting Calcium-Binding Sites in Ion Channels and Ion Transporters Using Protein Language Models and Multi-Scale Feature Extraction
Yan-Yun Chang, Yu-Chen Liu, Wei-En Jhang, Sin-Siang Wei, Yu-Yen Ou
|[ 🎇&nbsp;Abstract](#abstract) |[📃&nbsp;Dataset](#Dataset) | [ 🚀&nbsp;Quick Prediction ](#colab)|[ 💡&nbsp;MCNN Training ](#train)|[ 💾&nbsp;Requirements](#requirement)|[ 📚&nbsp;License](#License)|
|-------------------------------|-----------------------------|------------------------------------------------|--------------------------------------|---------------------------------|
## 🎇Abstract <a name="abstract"></a>
Calcium ions (Ca²⁺) are crucial for various physiological processes, including neurotransmission and cardiac function. Dysregulation of Ca²⁺ homeostasis can lead to serious health conditions such as cardiac arrhythmias and hypertension. Ion channels and transporters play a vital role in maintaining cellular Ca²⁺ balance by facilitating Ca²⁺ transport across cell membranes. Accurate prediction of Ca²⁺ binding sites within these proteins is essential for understanding their function and identifying potential therapeutic targets, particularly for developing novel calcium channel blockers (CCBs).

This study introduces CaBind_MCNN, an innovative computational model that leverages pre-trained protein language models (PLMs) and a multi-scale feature extraction approach to predict Ca²⁺ binding sites in ion channels and transporter proteins. Our method integrates embeddings from the ProtTrans PLM with a convolutional neural network (CNN)-based multi-window scanning approach, capable of capturing diverse sequence features relevant to Ca²⁺ binding. The model, trained on a curated dataset of 27 calcium-binding protein sequences, achieves high accuracy with an area under the curve (AUC) of 0.9886, significantly outperforming some existing methods. These results demonstrate the potential of CaBind_MCNN to enhance drug discovery efforts by identifying potential CCBs targets and advancing the development of novel therapies for calcium-related disorders. 

<br>

![workflow](https://github.com/B1607/CaBind_MCNN/blob/main/figure/CaBind_workflow.png)

## 📃Dataset <a name="Dataset"></a>

| Dataset            | Protein Sequence | Ca²⁺ Binding Residues     | Non-Binding Residues     |
|--------------------|------------------|--------------------------|--------------------------|
| Training data      | 21               | 111                      | 22879                    |
| Testing data       | 6                | 31                       | 3727                     |
| Calcium Channel from ChEMBL   | 33    | 230                      | 37980                     |

## 🚀Quick Prediction <a name="colab"></a>
[<img src="https://colab.research.google.com/assets/colab-badge.svg">](https://colab.research.google.com/drive/1xW6k05tAwPRp6hSLBOqYJskjSWTi-Fp_?usp=sharing)<br>
https://colab.research.google.com/drive/1xW6k05tAwPRp6hSLBOqYJskjSWTi-Fp_?usp=sharing

### Step 1: Environment Setup
open the link of colab notebook and change the runtime type to a device other than CPU.

### Step 2: Excute the program
This Colab notebook will automatically import all necessary dependencies and download the required files.

### Step 3: Submit your fasta file and wait for the Prediction result !

Upload your own FASTA file to run the prediction.
The format of the FASTA file will be as follows:
```bash
>P61022
MGSRASTLLRDEELEEIKKETGFSHSQITRLYSRFTSLDKGENGTLSREDFQRIPELAINPLGDRIINAFFSEGEDQVNFRGFMRTLAHFRPIEDNEKSKDVNGPEPLNSRSNKLHFAFRLYDLDKDDKISRDELLQVLRMMVGVNISDEQLGSIADRTIQEADQDGDSAISFTEFVKVLEKVDVEQKMSIRFLH
>Q9JJ69
MRGQGRKESLSDSRDLDGSYDQLTGHPPGPSKKALKQRFLKLLPCCGPQALPSVSETLAAPASLRPHRPRPLDPDSVEDEFELSTVCHRPEGLEQLQEQTKFTRRELQVLYRGFKNECPSGIVNEENFKQIYSQFFPQGDSSNYATFLFNAFDTNHDGSVSFEDFVAGLSVILRGTIDDRLNWAFNLYDLNKDGCITKEEMLDIMKSIYDMMGKYTYPALREEAPREHVESFFQKMDRNKDGVVTIEEFIESCQQDENIMRSMQLFDNVI
```
(Alternatively, you may use our dataset, which contains both Testing and Calcium Channel. [⬇️link](https://github.com/B1607/CaBind_MCNN/tree/main/Colab)<br>
The result will be formatted as follows:
```bash
Fasta     :  >P61022
Amino acid:  MGSRASTLLRDEELEEIKKETGFSHSQITRLYSRFTSLDKGENGTLSREDFQRIPELAINPLGDRIINAFFSEGEDQVNFRGFMRTLAHFRPIEDNEKSKDVNGPEPLNSRSNKLHFAFRLYDLDKDDKISRDELLQVLRMMVGVNISDEQLGSIADRTIQEADQDGDSAISFTEFVKVLEKVDVEQKMSIRFLH
Prediction:  000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001010101000010000000000000000000000000000010101000000100000000000000000000
```
1 indicates the amino acid is predicted to be a Ca2+ interacting residue.<br>
0 indicates the amino acid is predicted to be a non-Ca2+ interacting residue.

## 💡&nbsp;MCNN Training <a name="train"></a>

### Step 1: Environment Setup

We recommend using Anaconda to manage the project environment. You can create the necessary environment using the following command:
```bash
conda env create -n MCNN_Ca -f environment.yml
```
Activate the conda environment
```bash
conda activate MCNN_Ca
```
### Step 2: Download the GitHub Repository and Dataset

Clone the GitHub repository using the following command:
```bash
git clone https://github.com/B1607/CaBind_MCNN.git
```
Navigate to the repository folder:
```bash
cd CaBind_MCNN
```
### Step 3: Generate the necessary data for training
#### Step 3.1: Get different feature of dataset
```bash
cd data

#RUN
python get_ProtTrans.py -in "Your FASTA file folder" -out "The destination folder of your output"

#For example:
#python get_ProtTrans.py -in ./fasta/train -out ./ProtTrans/train"
```
#### Step 3.2: Get the package of dataset
```bash
cd dataset

#RUN
python get_dataset.py -in "Your data feature Folder" -label "Your binding label folder" -out "The destination folder of your output"  -dt "datatype" -w "Setting of Sequence length." 

#For example:
#python get_dataset.py -in ../data/ProtTrans/train -label ../data/label/train -out ./Train -dt .prottrans -w 6
```

### Step 4: Navigate to the "code" folder and Run the code!
```bash
cd DIRP

python MCNN_npy.py
"""
you can also change the arguments to training model by your self
-n_fil , --num_filter
      The number of filters in the convolutional layer.
-n_hid , --num_hidden
      The number of hidden units in the dense layer.
-bs , --batch_size
      The batch size for training the model.
-ws , --window_sizes
      The window sizes for convolutional filters.
-vm , --validation_mode
      The validation mode. Options are 'cross', 'independent'.
-d , --data_type,
      The type of data. Options are 'ProtTrans', 'tape', 'esm2'
-n_feat , --num_feature
      The number of data feature dimensions. 1024 for ProtTrans, 768 for tape, 1280 for esm2.
-length , --n_length
      The length of the input sequence in residues (amino acids).
"""
```
Alternatively, utilize the Jupyter notebook:
```bash
main.ipynb
```


## 💾&nbsp;Requirements <a name="requirement"></a>
```bash
h5py==3.11.0
tqdm==4.66.4
numpy==1.26.4
scikit-learn==1.4.2
tensorflow==2.10.1
transformers==4.40.1
torch==2.3.0+cu118
```

## 📚&nbsp;License <a name="License"></a>
Licensed under the Academic Free License version 3.0
