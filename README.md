# CaBind_MCNN

## Abstract <a name="abstract"></a>
Calcium ions (Ca²⁺) are crucial for various physiological processes, including neurotransmission and cardiac function. Dysregulation of Ca²⁺ homeostasis can lead to serious health conditions such as cardiac arrhythmias and hypertension. Ion channels and transporters play a vital role in maintaining cellular Ca²⁺ balance by facilitating Ca²⁺ transport across cell membranes. Accurate prediction of Ca²⁺ binding sites within these proteins is essential for understanding their function and identifying potential therapeutic targets, particularly for developing novel calcium channel blockers (CCBs).

This study introduces CaBind_MCNN, an innovative computational model that leverages pre-trained protein language models (PLMs) and a multi-scale feature extraction approach to predict Ca²⁺ binding sites in ion channels and transporter proteins. Our method integrates embeddings from the ProtTrans PLM with a convolutional neural network (CNN)-based multi-window scanning approach, capable of capturing diverse sequence features relevant to Ca²⁺ binding. The model, trained on a curated dataset of 27 calcium-binding protein sequences, achieves high accuracy with an area under the curve (AUC) of 0.9886, significantly outperforming some existing methods. These results demonstrate the potential of CaBind_MCNN to enhance drug discovery efforts by identifying potential CCB targets and advancing the development of novel therapies for calcium-related disorders.


<br>

## Dataset <a name="Dataset"></a>

| Dataset            | Protein Sequence | Ca²⁺ Binding Residues     | Non-Binding Residues     |
|--------------------|------------------|--------------------------|--------------------------|
| Training data      | 21               | 111                      | 22879                    |
| Testing data       | 6                | 31                       | 3727                     |
| Independent Test   | 4                | 43                       | 1801                     |