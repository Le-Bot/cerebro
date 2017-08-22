import abc

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier


class AbstractClassifier(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fit(self, features, labels):
        raise NotImplementedError()

    @abc.abstractmethod
    def predict(self, features):
        raise NotImplementedError()


class CerebroClassifier(AbstractClassifier):
    def __init__(self):
        self.clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', SGDClassifier(max_iter=5, tol=None)),
        ])

    def fit(self, features, labels):
        self.clf.fit(features, labels)

    def predict(self, features):
        return self.clf.predict(features)
