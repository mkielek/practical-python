# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
regular_payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
total_paid = 0.0
month = 1

while principal > 0:
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        payment = regular_payment + extra_payment
    else:
        payment = regular_payment

    rated_payment = principal * (1+rate/12)

    principal = rated_payment - payment

    if principal < 0:
        payment = rated_payment + payment + principal
        principal = 0

    total_paid = total_paid + payment

    print(f'{month:>3} {total_paid:10.2f} {principal:10.2f}')

    month = month + 1

print(f'Total paid {total_paid:0.2f}')
print(f'Total months {month - 1}')
