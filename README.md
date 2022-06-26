# Restaurant-Menu-Analysis

## Clustering Word Embeddings of Restaurant Brands' Menu Item
**PLEASE READ BELOW README FIRST**

- Run main notebook file on GPU: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alexdseo/Restaurant-menu-Analysis/blob/master/REMA.ipynb)

## Workflow

### 1. Data Preprocessing

`data_preprocessing.py`

- In this python script we take `MenuItem.csv` as an input which has 4,524 entries of data with Restaurant name and their menu item. While looking at the dataset, we found that there are about 340 unique restaurant names. However, looking deeper into the dataset, there were some restaurants with multiple names or names with a typo. For example, there were names with 'Dukes' and 'Duke's' or something like 'Kaizen' and 'Kaizen Naturals'. For latter example, even though it has a different name it was actually the same brand/subsidaries (according to the 'Nutrionix', which is the source of the data). To ease the job for the later steps, we unified all these restaurants with multiple names.

- Next, we found that the Menu item data had a lot of commas but in reverse order. For example, the menu item would look something like (Coke, Regular). Therefore, we removed the commas and reversed the order so it could be (Regular Coke). Then, we removed all the useless punctuations in the dataset including () and &(stopwords). But leave numbers for now since there are a lot of data with something like '16 oz'. 

- Finally, to make our data ready to be used for embedding models, we concatenate all the menu items for each restaurants. This process reduces the length of the datset to 308. Between each menu item we only added white space as in later step it will be all tokenized. One additional thing that we noticed from the dataset was that the menu item does not necessarily represent the restaurant's signiture items. For example, Portillo's 'Original food Item' did not include hotdogs, where the restaurant is famous for Chicago style hotdogs.

  - Input: `MenuItem.csv`
  - Output: `MenuItem_cleaned.csv`

### 2. Sentence Embedding & Dimensionality Reduction

`REMA.ipynb`

- In this notebook file we take `MenuItem_cleaned.csv` as an input file after data preprocessing work and apply embedding models and dimensionality reduction methods to make a clustering analysis. We considered 3 different embedding models. `SBERT`,  `FastText`  and lastly `TF-IDF`. The reason why we considered 3 different models is that, since our menu item that will be feed into the embedding model is not really a 'sentence' and just an array of menu items from each restaurant brands. Therefore, we considered a model that is a transformer based sentence embedding method(SBERT) and a word2vec like word embedding method(FastText) and lastly a traditional statistical approach for text featurization(TF-IDF) so we can compare the quality these different approaches.

- Next, we consider 3 different dimensionality reduction methods for all 3 embedding models. As dimensionality reduction methods come in handy when doing a clustering analyis and making a visualization, soemtimes these methods can lose a lot of information and not be compatible with certain embedding models. As we only have limited data we consider 3 different dimensionaility reduction methods, `PCA`, `t-SNE`, and `UMAP`. Therefore, we can compare different dimensionality methods for all cases and choose which methods to use for each embedding models.

### 3. Clustering & Visualization

`REMA.ipynb`

- Finally we consider 3 clustering models for all 9 cases of embedding models and dimensionality reduction methods. Since we chose 3 different dimensionality reduction methods, it is worth a work to try different clustering algorithm to find the best result for each cases. Therefore, we will use some widely used clustering algorithms like `k-means`, `Gaussian Mixture Models`, and `HDBSCAN`.

- Then, We calculate the clustering quality for every 27 cases using cosine similiarities. In each cases of embedding-dimensionality reduction-clustering, we will calculate the cosine similiarities of original word embeddings before dimensionality reduction within the clusters and average them. Then, we will take an average of all cluster's cosine similiarty and set it as each cases' clustering quality. Finally, we will only visualize clustering with the highest clustering quality for each embedding models. The list of clustering quality for all cases can be seen in the notebook file.

## Visualization of clustering with best quality for each embedding methods

![alt text](https://github.com/alexdseo/Restaurant-Menu-Analysis/blob/master/SBERT.png)

- SBERT-UMAP-HDBSCAN had the highest clustreing quality among SBERT cases with 0.49.


![alt text](https://github.com/alexdseo/Restaurant-Menu-Analysis/blob/master/FastText.png)

- FastText-UMAP-HDBSCAN had the highest clustreing quality among FastText cases with 0.44.

![alt text](https://github.com/alexdseo/Restaurant-Menu-Analysis/blob/master/TF-IDF.png)

- TF-IDF-PCA-kmeans had the highest clustreing quality among TF-IDF cases with 0.54.

- Surprisingly, the result from using traiditional text featurization method, most basic dimensionality reduction method, and most basic clustering method had the best result!! As UMAP and HDBSCAN worked well with trendy state of the art embedding models like SBERT and FastText, TF-IDF mathced well with PCA and kmeans.

- Looking at the clusters, interestingly, we could consistently find clusters with **Pizza brands, Grocery brands, Seafood brands, American food brands, and Dessert food brands** among all cases.

## Quickstart for Data preprocessing

1. Set up your environment. You can either use your base environment or create a conda virtual environment. Assuming anaconda is installed and using Python 3.8+:


```
conda create -n venv
conda activate venv
```

2. Set working directory:
`cd (To this repository)`

3. Install requirements:
```
conda install pip
pip install -r requirements.txt
```

4. Run Python scripts:
```
python data_preprocessing.py
```

5. Then, run the main notebook above to run all the rest steps including visualization.
