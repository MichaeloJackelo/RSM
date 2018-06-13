from decimal import Decimal, getcontext


def calculate_pi_Bailey_Borwein_Plouffe_formula(start, end):
    getcontext().prec=6000
    print(sum(1/Decimal(16)**k *
          (Decimal(4)/(8*k+1) -
           Decimal(2)/(8*k+4) -
           Decimal(1)/(8*k+5) -
           Decimal(1)/(8*k+6)) for k in range(start, end)))


calculate_pi_Bailey_Borwein_Plouffe_formula(0, 4000)