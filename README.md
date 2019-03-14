# MKR.PyTorch

This repository is  PyTorch implementation of MKR ([arXiv](https://arxiv.org/abs/1901.08907)).

The code is heavily based on the original [TensorFlow version](https://github.com/hwwang55/MKR).

![](https://github.com/hwwang55/MKR/blob/master/framework.png)

MKR is a **M**ulti-task learning approach for **K**nowledge graph enhanced **R**ecommendation.
MKR consists of two parts: the recommender system (RS) module and the knowledge graph embedding (KGE) module. 
The two modules are bridged by *cross&compress* units, which can automatically learn high-order interactions of item and entity features and transfer knowledge between the two tasks.

### Requirements
Tested under
- Python == 3.6
- PyTorch >= 0.4
- scikit-learn, tqdm, numpy, matplotlib, tensorboardX

### Running the code
- Movie
  ```
  $ cd src
  $ python preprocess.py --dataset movie
  $ python main.py
  ```
- Book
  - ```
    $ cd src
    $ python preprocess.py --dataset book
    ```
  - open `main.py` file;
    
  - comment the code blocks of parameter settings for MovieLens-1M;
    
  - uncomment the code blocks of parameter settings for Book-Crossing;
    
  - ```
    $ python main.py
    ```
- Music
  - ```
    $ cd src
    $ python preprocess.py --dataset music
    ```
  - open `main.py` file;
    
  - comment the code blocks of parameter settings for MovieLens-1M;
    
  - uncomment the code blocks of parameter settings for Last.FM;
    
  - ```
    $ python main.py
    ```
