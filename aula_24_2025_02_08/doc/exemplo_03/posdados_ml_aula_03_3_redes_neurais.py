# -*- coding: utf-8 -*-
"""PosDados_ML - Aula 03.3 - Redes Neurais.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-FSCVY9kflGxexfyNMQ45oxkE7WHGTFJ

## **Importação das bibliotecas**
"""



!pip install keras.utils
!pip install np_utils

# Commented out IPython magic to ensure Python compatibility.
import re
import nltk

import pandas as pd
import numpy as np

import pandas.testing as tm

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
english_stemmer=nltk.stem.SnowballStemmer('english')

from sklearn.feature_selection import SelectKBest, chi2, f_classif
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier, SGDRegressor
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import random
import itertools

import sys
import os
import argparse
from sklearn.pipeline import Pipeline
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import CountVectorizer
import six
from abc import ABCMeta
from scipy import sparse
from scipy.sparse import issparse
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils import check_X_y, check_array
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.preprocessing import normalize, binarize, LabelBinarizer
from sklearn.svm import LinearSVC

from keras.preprocessing import sequence
from tensorflow.python.keras.utils import np_utils
# from keras.utils import np_utils
from keras.models import Sequential
# from keras.layers.core import Dense, Dropout, Activation, Lambda
from tensorflow.keras.layers import Dense, Dropout, Activation, Lambda
from keras.layers import Embedding
from keras.layers import LSTM, SimpleRNN, GRU
from tensorflow.keras.preprocessing.text import Tokenizer
from collections import defaultdict
from keras.layers import Convolution1D
from tensorflow.keras import backend as K

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
# %matplotlib inline
plt.style.use('ggplot')

"""## **Preparando as amostras**

### **Segmentação da Amostra**
"""

data = pd.read_csv('/content/amazon.csv') #link: https://drive.google.com/open?id=1JmGqiLEh_wUeLilLF7Hv_w4jgUNbG0Q_
data.head()

data = data[:1000] #só para rodar mais rápido durante a aula
data

data = data[data['Reviews'].isnull()==False]

train, test = train_test_split(data, test_size = 0.3)

sns.countplot(data['Rating'])

"""### **Pré-processamento do texto**

"""

# Função para pré-processamento do texto
# Converte o documento em uma sequencia de palavras e remove algumas stop words.
# Retorna uma lista de palavras
def review_to_wordlist( review, remove_stopwords=True):

    # 1. Remover HTML
    review_text = BeautifulSoup(review).get_text()

    # 2. Remover caracteres numéricos
    review_text = re.sub("[^a-zA-Z]"," ", review)
    #
    # 3. Converte palavras para minúsculas e sem espaços
    words = review_text.lower().split()
    #
    # 4. Remover opcionalmente as stop words (True - default)
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]

    b=[]
    stemmer = english_stemmer #PorterStemmer()
    for word in words:
        b.append(stemmer.stem(word))

    # 5. Returna uma lista de palavras
    return(b)

nltk.download('stopwords') #Lista para palavras em inglês

clean_train_reviews = []
for review in train['Reviews']:
    clean_train_reviews.append( " ".join(review_to_wordlist(review)))

clean_test_reviews = []
for review in test['Reviews']:
    clean_test_reviews.append( " ".join(review_to_wordlist(review)))

#Convert a collection of raw documents to a matrix of TF-IDF features.
vectorizer = TfidfVectorizer( min_df=2, max_df=0.95, max_features = 200000, ngram_range = ( 1, 4 ), sublinear_tf = True )

vectorizer = vectorizer.fit(clean_train_reviews)
train_features = vectorizer.transform(clean_train_reviews)

test_features = vectorizer.transform(clean_test_reviews)

fselect = SelectKBest(chi2 , k=100) #10000. #Select features according to the k highest scores.
train_features = fselect.fit_transform(train_features, train["Rating"])
test_features = fselect.transform(test_features)

"""## **Outros Modelos - SGD, Random Forest, Gradient Boosting**"""

model1 = MultinomialNB(alpha=0.001) #Naive Bayes
model1.fit( train_features, train["Rating"] )

model2 = SGDClassifier(loss='modified_huber', random_state=0, shuffle=True) #outra variação do SVM
model2.fit( train_features, train["Rating"] )

model3 = RandomForestClassifier()
model3.fit( train_features, train["Rating"] )

model4 = GradientBoostingClassifier()
model4.fit( train_features, train["Rating"] )

pred_1 = model1.predict( test_features.toarray() )
pred_2 = model2.predict( test_features.toarray() )
pred_3 = model3.predict( test_features.toarray() )
pred_4 = model4.predict( test_features.toarray() )

#Implementando uma Naive Bayes
class NBSVM(six.with_metaclass(ABCMeta, BaseEstimator, ClassifierMixin)):

    def __init__(self, alpha=1.0, C=1.0, max_iter=10000):
        self.alpha = alpha
        self.max_iter = max_iter
        self.C = C
        self.svm_ = [] # fuggly

    def fit(self, X, y):
        X, y = check_X_y(X, y, 'csr')
        _, n_features = X.shape

        labelbin = LabelBinarizer()
        Y = labelbin.fit_transform(y)
        self.classes_ = labelbin.classes_
        if Y.shape[1] == 1:
            Y = np.concatenate((1 - Y, Y), axis=1)

        Y = Y.astype(np.float64)

        # Contagem dos registros dos dados
        n_effective_classes = Y.shape[1]
        self.class_count_ = np.zeros(n_effective_classes, dtype=np.float64)
        self.ratios_ = np.full((n_effective_classes, n_features), self.alpha,
                                 dtype=np.float64)
        self._compute_ratios(X, Y)

        # flugglyness
        for i in range(n_effective_classes):
            X_i = X.multiply(self.ratios_[i])
            svm = LinearSVC(C=self.C, max_iter=self.max_iter)
            Y_i = Y[:,i]
            svm.fit(X_i, Y_i)
            self.svm_.append(svm)

        return self

    def predict(self, X):
        n_effective_classes = self.class_count_.shape[0]
        n_examples = X.shape[0]

        D = np.zeros((n_effective_classes, n_examples))

        for i in range(n_effective_classes):
            X_i = X.multiply(self.ratios_[i])
            D[i] = self.svm_[i].decision_function(X_i)

        return self.classes_[np.argmax(D, axis=0)]

    def _compute_ratios(self, X, Y):
        '''Contar ocorrências de recursos e proporções de computação.'''
        if np.any((X.data if issparse(X) else X) < 0):
            raise ValueError("Entrada X deveria ser positiva")

        self.ratios_ += safe_sparse_dot(Y.T, X)  # ratio + feature_occurrance_c
        normalize(self.ratios_, norm='l1', axis=1, copy=False)
        row_calc = lambda r: np.log(np.divide(r, (1 - r)))
        self.ratios_ = np.apply_along_axis(row_calc, axis=1, arr=self.ratios_)
        check_array(self.ratios_)
        self.ratios_ = sparse.csr_matrix(self.ratios_)


def f1_class(pred, truth, class_val):
    n = len(truth)

    truth_class = 0
    pred_class = 0
    tp = 0

    for ii in range(0, n):
        if truth[ii] == class_val:
            truth_class += 1
            if truth[ii] == pred[ii]:
                tp += 1
                pred_class += 1
                continue;
        if pred[ii] == class_val:
            pred_class += 1

    precision = tp / float(pred_class)
    recall = tp / float(truth_class)

    return (2.0 * precision * recall) / (precision + recall)


def semeval_senti_f1(pred, truth, pos=2, neg=0):

    f1_pos = f1_class(pred, truth, pos)
    f1_neg = f1_class(pred, truth, neg)

    return (f1_pos + f1_neg) / 2.0;


def main(train_file, test_file, ngram=(1, 3)):
    print('carregando...')
    train = pd.read_csv(train_file, delimiter='\t', encoding='utf-8', header=0,
                        names=['text', 'label'])

    test = pd.read_csv(test_file, delimiter='\t', encoding='utf-8', header=0,
                        names=['text', 'label'])

    print('vetorizando...')
    vect = CountVectorizer()
    classifier = NBSVM()

    # create pipeline
    clf = Pipeline([('vect', vect), ('nbsvm', classifier)])
    params = {
        'vect__token_pattern': r"\S+",
        'vect__ngram_range': ngram,
        'vect__binary': True
    }
    clf.set_params(**params)

    print('treinando...')
    clf.fit(train['text'], train['label'])

    print('classificando...')
    pred = clf.predict(test['text'])

    print('teste...')
    acc = accuracy_score(test['label'], pred)
    f1 = semeval_senti_f1(pred, test['label'])
    print('NBSVM: acc=%f, f1=%f' % (acc, f1))


model5 = NBSVM(C=0.01)
model5.fit( train_features, train["Rating"] )

pred_5 = model5.predict( test_features )
pred_5

print(classification_report(test['Rating'], pred_2, target_names=['1','2','3','4','5']))

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Matriz de confusão',
                          cmap=plt.cm.Blues):
    '''
     Esta função imprime e plota a matriz de confusão.
     A normalização pode ser aplicada configurando `normalize = True`.
    '''
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Matriz de confusão normalizada")
    else:
        print('Matriz de confusão, não normalizada')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

# Calculando a matriz de confusão
cnf_matrix = confusion_matrix(test['Rating'], pred_5)


plot_confusion_matrix(cnf_matrix, classes=['1','2','3','4','5'],title='Matriz de confusão, sem normalização')

print('predição 1 - accuracy: ', accuracy_score(test['Rating'], pred_1))
print('predição 2 - accuracy: ', accuracy_score(test['Rating'], pred_2))
print('predição 3 - accuracy: ', accuracy_score(test['Rating'], pred_3))
print('predição 4 - accuracy: ', accuracy_score(test['Rating'], pred_4))
print('predição 5 - accuracy: ', accuracy_score(test['Rating'], pred_5))

"""## **Deep Learning**

### **Modelo MLP**
"""

vectorizer = TfidfVectorizer( min_df=2, max_df=0.95, max_features = 1000, ngram_range = ( 1, 3 ),sublinear_tf = True )

vectorizer = vectorizer.fit(clean_train_reviews)
train_features = vectorizer.transform(clean_train_reviews)

test_features = vectorizer.transform(clean_test_reviews)

batch_size = 32 #Tamanho do lote (Batch Size)
nb_classes = 5

X_train = train_features.toarray()
X_test = test_features.toarray()

print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
y_train = np.array(train['Rating']-1)
y_test = np.array(test['Rating']-1)

#Criacao dos Modelos com SKlearn

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier(
    solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10,), random_state=1)

#treinamento
clf.fit(X_train, y_train)

#teste
y_prev = clf.predict(X_test)

print('predição MLP (SKLearn) - accuracy: ', accuracy_score(y_test, y_prev))

#MLP com Keras

X_train = train_features.toarray()
X_test = test_features.toarray()

print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)
y_train = np.array(train['Rating']-1)
y_test = np.array(test['Rating']-1)

Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

# pre-processamento: dividindo pelo max e pela subtração da média
scale = np.max(X_train)
X_train /= scale
X_test /= scale

mean = np.mean(X_train)
X_train -= mean
X_test -= mean

input_dim = X_train.shape[1]

# Criação do Modelo de Deep Dumb MLP (DDMLP)
model = Sequential()
model.add(Dense(256, input_dim=input_dim)) #camada 1 256 neurônio #input_dim
model.add(Activation('relu'))
model.add(Dropout(0.4))
model.add(Dense(128))  #camada 2 - 128 neurônios
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(256))  #camada 2 - 128 neurônios
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(nb_classes)) #camada 3 - saida
model.add(Activation('softmax'))

# usaremos xent categórico para a perda e o RMSprop como otimizador
model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

#Treinamento
model.fit(X_train, Y_train, epochs=30, batch_size=16, validation_split=0.1)

#Testando o modelo
preds_x = model.predict(X_test)
preds = np.argmax(preds_x, axis=1)
print('Predição MLP (Keras) -accuracy: ', accuracy_score(test['Rating'], preds+1))

"""### **Modelo LSTM**"""

max_features = 20000
EMBEDDING_DIM = 100
VALIDATION_SPLIT = 0.2
maxlen = 70
batch_size = 32
nb_classes = 5

# vetorizando as amostras de texto em um tensor inteiro 2D
tokenizer = Tokenizer(num_words=max_features)
tokenizer.fit_on_texts(train['Reviews'])
sequences_train = tokenizer.texts_to_sequences(train['Reviews'])
sequences_test = tokenizer.texts_to_sequences(test['Reviews'])

print('Pad sequences (samples x time)')
X_train = sequence.pad_sequences(sequences_train, maxlen=maxlen)
X_test = sequence.pad_sequences(sequences_test, maxlen=maxlen)

Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)


print('X_train shape:', X_train.shape)
print('X_test shape:', X_test.shape)

#Construindo o Modelo
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(nb_classes)) #camada de saida
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#treinamento
print('Treinamento...')
model.fit(X_train, Y_train, batch_size=batch_size, epochs=1,validation_data=(X_test, Y_test))

#testando o modelo
score, acc = model.evaluate(X_test, Y_test,batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)


print("Gerando as Previsões...")
preds_x = model.predict(X_test)
preds = np.argmax(preds_x, axis=1)

print('prediction 7 - accuracy: ', accuracy_score(test['Rating'], preds+1))

"""### **Modelo ConveNet - CNN**"""

nb_filter = 32
filter_length = 3
hidden_dims = 250
nb_epoch = 2

#Criacao do Modelo
model = Sequential()
model.add(Embedding(max_features, 128))

# nós adicionamos um Convolution1D, que aprenderá nb_filter
# Grupo de palavras filtradas pelo filter_length:
model.add(Convolution1D(32, 3,
                        padding='valid',
                        activation='relu'))

def max_1d(X):
    return K.max(X, axis=1)

model.add(Lambda(max_1d, output_shape=(nb_filter,)))
model.add(Dense(hidden_dims))
model.add(Dropout(0.2))
model.add(Activation('relu'))
model.add(Dense(nb_classes))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#treinamento
print('Treinamento...')
model.fit(X_train, Y_train, batch_size=batch_size, epochs=1,validation_data=(X_test, Y_test))

#testando o modelo
score, acc = model.evaluate(X_test, Y_test,batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)


print("Gerando as Previsões...")
preds_x = model.predict(X_test)
preds = np.argmax(preds_x, axis=1)

print('prediction 8 - accuracy: ', accuracy_score(test['Rating'], preds+1))