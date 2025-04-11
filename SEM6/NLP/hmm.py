from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from hmmlearn.hmm import GaussianHMM
import numpy as np

# === 1. Cross-Domain Classification ===
tech = fetch_20newsgroups(categories=['comp.graphics'], remove=('headers', 'footers', 'quotes'))
health = fetch_20newsgroups(categories=['sci.med'], remove=('headers', 'footers', 'quotes'))

vectorizer = CountVectorizer(max_features=1000)
X_train = vectorizer.fit_transform(tech.data).toarray()
X_test = vectorizer.transform(health.data).toarray()

hmm_model = GaussianHMM(n_components=3, covariance_type='diag', n_iter=100)
hmm_model.fit(X_train)

pred_train = hmm_model.predict(X_train)
pred_test = hmm_model.predict(X_test[:len(X_train)])

print("Cross-domain HMM accuracy:", accuracy_score(pred_train, pred_test))

# === 2. Hybrid HMM + Naive Bayes ===
data = fetch_20newsgroups(categories=['comp.graphics', 'sci.med'], remove=('headers', 'footers', 'quotes'))
labels = [0 if target == 0 else 1 for target in data.target]

X = vectorizer.fit_transform(data.data).toarray()
hmm_model.fit(X)
features = hmm_model.predict_proba(X)  # Posterior probabilities

X_tr, X_te, y_tr, y_te = train_test_split(features, labels, test_size=0.3)
nb = GaussianNB()
nb.fit(X_tr, y_tr)

print("Hybrid model accuracy:", accuracy_score(y_te, nb.predict(X_te)))
