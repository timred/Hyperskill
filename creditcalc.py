import argparse
import math
import sys

# Parse Arguments
parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", metavar="annuity|diff", type=str, help='indicates the type of payment: "annuity" or "diff" (differentiated)')
parser.add_argument("--payment", metavar="", type=float, help='the monthly payment amount')
parser.add_argument("--principal", metavar="", type=float, help='the principal sum')
parser.add_argument("--periods", metavar="", type=int, help='the number of months needed to repay the loan')
parser.add_argument("--interest", metavar="", type=float, help='specified without a percent sign')
args = parser.parse_args()


# Print Overpayment
def overpayment(loan_payments, loan_periods, loan_principal):
    if type(loan_payments) == list:
        print(f"Overpayment = {int(sum(loan_payments) - loan_principal)}")
    else:
        print(f"Overpayment = {int(loan_payments * loan_periods - loan_principal)}")


if (args.interest is None or args.interest < 0) \
        or len(sys.argv) < 4 \
        or (args.type != "annuity" and args.type != "diff") \
        or (args.type == "diff" and args.payment):
    print("Incorrect parameters")
else:
    ir = float(args.interest) / 100
    i = ir / 12

    if args.type == "annuity":
        if args.payment is None:
            principal = float(args.principal)
            periods = int(args.periods)
            payment = math.ceil(principal * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
            print(f"Your monthly payment = {math.ceil(payment)}!")
            overpayment(payment, periods, principal)
        elif args.principal is None:
            payment = float(args.payment)
            periods = int(args.periods)
            # a = float(input("Enter the annuity payment:\n"))
            # n = float(input("Enter the number of periods:\n"))
            principal = math.floor(payment * pow((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1), -1))
            print(f"Your loan principal = {principal}!")
            overpayment(payment, periods, principal)
        elif args.periods is None:
            principal = float(args.principal)
            payment = float(args.payment)
            periods = math.log(payment / (payment - i * principal), 1 + i)
            if math.ceil(periods) % 12 == 0:
                print(f"It will take {int(math.ceil(periods) / 12)} years to repay this loan!")
            elif periods < 12:
                print(f"It will take {int(math.ceil(periods))} months to repay this loan!")
            else:
                print(f"It will take {int(periods // 12)} years and {int(math.ceil(periods % 12))} months to repay this loan!")
            overpayment(payment, int(math.ceil(periods)), principal)
    elif args.type == "diff" and args.payment is None:
        principal = float(args.principal)
        periods = int(args.periods)
        month = 0
        payments = list()
        while month < periods:
            month += 1
            payment = math.ceil(principal / periods + i * (principal - principal * (month - 1) / periods))
            payments.append(payment)
            print(f"Month {month}: payment is {payment}")
        overpayment(payments, periods, principal)
