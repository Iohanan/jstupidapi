
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
	def calculate_interest():
		pass                                                                                                         
	
	@staticmethod
	def calculate_time_interest():
		pass


if __name__ == '__main__':
	pass