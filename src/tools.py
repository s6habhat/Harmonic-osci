import numpy as np

def getMinima(lambda_):
	# mimina at +/- sqrt(-a/(2b))
	return np.sqrt(-1 / (2 * lambda_))

def distanceToParameter(distance):
	# calculate lambda parameter from distance
	return -1/2 * (distance / 2)**-2

def bootstrap(num, values):
	# bootstrap function
	means = [np.mean(np.random.choice(values, size = len(values) // 2) / (len(values) // 2)) for n in range(num)]
	return np.std(means)

STATE_INIT, STATE_LEFT, STATE_RIGHT = None, 1, 2

class TransitionCounter:
	def __init__(self):
		self.transitions = -1
		self.lastState = STATE_INIT

	def registerValue(self, value):
		state = STATE_LEFT
		if value > 0:
			state = STATE_RIGHT
		if state != self.lastState:
			self.lastState = state
			self.transitions += 1

	def getTransitions(self):
		return self.transitions

def Potential(mu, lambda_):
	# Potential function with parameters
	def wrapper(x, mu=mu, lambda_=lambda_):
		return mu * (x ** 2 + lambda_ * x ** 4)
	return wrapper

def Action(tau, mass, potential):
	# Action function with parameters
	def wrapper(x_new, x_old, tau=tau, mass=mass, potential=potential):
		return tau * (mass * (x_new - x_old) ** 2 / (2 * tau ** 2) + potential(x_new))
	return wrapper

class Metropolis:
	# Metropolis algorithm
	def __init__(self, stop, func, borders = [-5, 5]):
		self.stop = stop
		self.func = func
		self.borders = borders
		self.value = np.random.uniform(*self.borders)
		self.action = self.func(self.value, self.value)

	def __iter__(self):
		# calculate steps
		num = 0
		while num < self.stop:
			changed = False
			while not changed:
				newValue = np.random.uniform(*self.borders)
				newAction = self.func(newValue, self.value)
				deltaAction = newAction - self.action
				if deltaAction < 0 or np.exp(-deltaAction) > np.random.rand():
					self.value = newValue
					self.action = newAction
					changed = True
			yield self.value
			num += 1

	def __len__(self):
		return self.stop


if __name__ == '__main__':
	# Test Case TransitionCounter
	tC = TransitionCounter()
	values = np.random.uniform(-1, 1, 10)
	for v in values:
		tC.registerValue(v)
	print(tC.getTransitions(), values)

	# Test Case getMinima, distanceToParameter
	for d in range(1, 17):
		print(distanceToParameter(d), 2 * getMinima(distanceToParameter(d)))

	# Test Case bootstrap:
	#values = np.random.normal(loc=0, scale=1, size=100)
	#bootstrap_values = bootstrap(10000, values)
	#print(bootstrap_values)