from math import log10

class Acompound(object):
	''' class for calculate parts about acompound interest '''
	@staticmethod
	def calculate_amount(capital, interest, time_interest):
		_amount = capital * pow(1+interest, time_interest)
		return float('%.2f' % _amount)
	
	@staticmethod
	def calculate_capital(amount, interest, time_interest):
		_capital = amount / pow(1+interest, time_interest)
		return float('%.2f' % _capital)
	
	@staticmethod
	def calculate_interest(amount, capital, time_interest):
		_interest = pow(amount/capital, 1/time_interest) - 1
		return float('%.2f' %_interest)                                                                                                         
	
	@staticmethod
	def calculate_time_interest(amount, capital,interest):
		_time_interest = log10(amount/capital) / log10(1+interest)
		return float('%.2f' % _time_interest)
		


if __name__ == '__main__':
	pass
