import numpy as np 
from random import shuffle

_sample_ = 10
_attribute_ = 5
_class_ = 3

W = np.random.randint(0, 5, _class_ * _attribute_).reshape(_attribute_, _class_)
X = np.random.randint(0, 5, _attribute_ * _sample_).reshape(_sample_, _attribute_)
y = np.random.randint(0, _class_ - 1, _sample_)

score = X.dot(W)
#print score

for i in xrange(_sample_):
	score[i, :] = score[i, :] - max(score[i, :])
score = np.exp(score)
softmax = np.zeros(_sample_)
for i in xrange(_sample_):
	softmax[i] = score[i, y[i]]/sum(score[i, :])
loss = sum(-1 * np.log(softmax))/_sample_ + sum(np.square(W.reshape(_class_ * _attribute_,)))
print loss
dW = np.zeros_like(W)
for k in xrange(_attribute_):
	for j in xrange(_class_):
		for i in xrange(_sample_):
			dW[k, j] += score[i, j]/sum(score[i, :]) * W[k ,j]
print dW