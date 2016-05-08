import numpy as np 
_sample_ = 10
_attribute_ = 5
_class_ = 3

W = np.random.randint(0, 10, _class_ * _attribute_).reshape(_class_, _attribute_)
X = np.random.randint(0, 10, _attribute_ * _sample_).reshape(_attribute_, _sample_)
y = np.random.randint(0, _class_ - 1, _sample_)

scores = W.dot(X)
print W[y]




d = np.zeros((_sample_, _attribute_))
d = d + np.dot(np.array([np.diag(np.dot(test, test.T))]).T, [np.ones(_attribute_)])
d = d + np.dot(np.array([np.ones(_sample_)]).T, [np.diag(np.dot(train, train.T))])
d = d - 2 * np.dot(test, train.T)

k = 5
print 'train:\t\tlabel:'
for i in xrange(_attribute_):
	print '%d\t'%i + str(train[i]) + '\t\t' + str(y[i])
print 'test:'
print test
print 'distance matrix'
print d

pred = np.zeros(_sample_)
for i in xrange(_sample_):
	print '************row %d*************'%i
	print str(test[i]) + ':'
	closest_y = []
	nearest_train = d[i].argsort()
	for j in xrange(k):
		print '%d\t'%nearest_train[j] + str(train[nearest_train[j]]) + '\t%d'%y[nearest_train[j]]
		closest_y.append(y[nearest_train[j]])
	print closest_y
	y_type = list(set(closest_y))
	vote = []
	a_y = []
	for w in xrange(len(y_type)):
		vote.append(closest_y.count(y_type[w]))
		a_y.append(y_type[w])
	_max_ = max(vote)
	key = 0
	flag = 0
	for w in xrange(len(y_type)):
		if vote[w] == _max_:
			key = w
			flag = flag + 1
	if flag == 1:
		pred[i] = y_type[key]
	else:
		pred[i] = None
print pred