## Arvore de decisão - Capitulo 6 

#!pip install scikit-learn

#biblioteca
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X = iris.data[:, 2:]
y = iris.target

# Treino
tree_clf = DecisionTreeClassifier(max_depth = 2)
tree_clf.fit(X,y)

# Visualizaçao
from sklearn.tree import export_graphviz

export_graphviz(
   tree_clf
  ,out_file = image_path("iris_tree.dot")
  ,feature_names = iris.feature_names[2:]
  ,class_names = iris.target_names
  ,rounded = True
  ,filled = True
)
