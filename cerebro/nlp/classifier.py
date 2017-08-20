import abc

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier


class AbstractClassifier(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def fit(self, features, labels):
        return

    @abc.abstractmethod
    def predict(self, features):
        return


class CerebroClassifier(AbstractClassifier):
    def __init__(self):
        self.clf = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', SGDClassifier()),
        ])

    def fit(self, features, labels):
        self.clf.fit(features, labels)

    def predict(self, features):
        return self.clf.predict(features)