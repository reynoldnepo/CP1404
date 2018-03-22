"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of total_months."""
    incomes = []
    total_months = int(input("How many total_months? "))

    for month in range(1, total_months + 1):
        income = float((input("Enter income for month  {} : ".format(month))))
        incomes.append(income)
    report_income(total_months,incomes)

def report_income(total_months,incomes):

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()