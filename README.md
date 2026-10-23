# ADSAI Coursework

Selected programming and maths assignments from my first year of the Applied Data Science & AI program at Zuyd University of Applied Sciences.

## Algorithms (Python)

- `algorithms/cube_solver.py`: solves a scrambled 2x2 Rubik's cube with breadth-first search over cube states, represented as tuples and moved with permutation tables.
- `algorithms/social_network.py`: loads a friendship graph from `network.txt`, prints network statistics, ranks friend suggestions by mutual friends and finds shortest paths between users.

## Linear Algebra for ML (NumPy)

- `linear-algebra/part_a_embeddings_and_rank.ipynb`: linear embeddings of words as vectors, analogy and cosine similarity ranking, and matrix rank as a measure of semantic diversity.
- `linear-algebra/part_b_svd_and_pca.ipynb`: singular value decomposition, rank-1 compression with reconstruction error and explained variance, and PCA to project 2D data onto one dimension.

## How to run

```bash
pip install numpy jupyter
python algorithms/cube_solver.py
python algorithms/social_network.py   # run from inside algorithms/
```
