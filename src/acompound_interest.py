from math import pow

class Acompound(object):
	''' class for calculate parts about acompound interest '''
	@staticmethod
	def calculate_amount(capital_rate, interest_rate, time_interest):
		_amount = capital_rate * pow(1+interest_rate, 2)
		return _amount


if __name__ == '__main__':
	pass