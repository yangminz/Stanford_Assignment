import numpy as np 
num_test = 5
num_train = 10
dim = 3

train = np.random.randint(0, 10, num_train * dim).reshape(num_train, dim)
y = np.random.randint(0, 10, num_train)
test = np.random.randint(0, 10, num_test * dim).reshape(num_test, dim)

d = np.zeros((num_test, num_train))
d = d + np.dot(np.array([np.diag(np.dot(test, test.T))]).T, [np.ones(num_train)])
d = d + np.dot(np.array([np.ones(num_test)]).T, [np.diag(np.dot(train, train.T))])
d = d - 2 * np.dot(test, train.T)

k = 5
print 'train:\t\tlabel:'
for i in xrange(num_train):
	print '%d\t'%i + str(train[i]) + '\t\t' + str(y[i])
print 'test:'
print test
print 'distance matrix'
print d

pred = np.zeros(num_test)
for i in xrange(num_test):
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