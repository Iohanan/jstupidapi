class Simple(object):
    '''class that calculate each variant of the simple interest formula'''
    @staticmethod
    def calculate_interest(principal, rate, time):
        _interest = principal * rate * time
        return float('{:.2}'.format(_interest))

    @staticmethod
    def calculate_principal(interest, rate, time):
        _principal = interest / (rate * time)
        return float('{:.2}'.format(_principal))

    @staticmethod
    def calculate_rate(interest, principal, time):
        _rate = interest / (principal * time)
        return float('{:.2}'.format(_rate))

    @staticmethod
    def calculate_time(interest, principal, rate):
        _time = interest / (principal * rate)
        return float('{:.2}'.format(_time))