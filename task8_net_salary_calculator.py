# Task 8: Develop a Net-Salary Calculator Program
# File: task8_net_salary_calculator.py

# ---------------------------------------------------------
# NOTE ON PAYE BRACKETS
# The task states PAYE should be calculated using bands of
# 0%, 4%, 5% and 6% based on the gross pay bracket, but does
# not give the exact Ksh thresholds. The following brackets
# are used for this program (adjust the numbers below if
# your instructor has provided different figures):
#
#   Gross Pay <= 10,000            -> 0%
#   Gross Pay 10,001 - 20,000      -> 4%
#   Gross Pay 20,001 - 30,000      -> 5%
#   Gross Pay above 30,000         -> 6%
# ---------------------------------------------------------

HOUSE_ALLOWANCE = 6500
MEDICAL_ALLOWANCE = 5500


# ---------------------------------------------------------
# a. Capture employee details (5 marks)
# ---------------------------------------------------------
def capture_employee_details():
    """Prompt the user for and return the employee's details."""
    payroll_number = input("Enter Payroll Number: ")
    name = input("Enter Employee Name: ")
    gender = input("Enter Gender: ")
    department = input("Enter Department: ")
    basic_salary = float(input("Enter Basic Salary (Ksh): "))

    return payroll_number, name, gender, department, basic_salary


# ---------------------------------------------------------
# b. Calculate gross pay (5 marks)
# ---------------------------------------------------------
def calculate_gross_pay(basic_salary):
    """Gross Pay = Basic Salary + House Allowance + Medical Allowance."""
    return basic_salary + HOUSE_ALLOWANCE + MEDICAL_ALLOWANCE


# ---------------------------------------------------------
# c. Calculate PAYE based on gross pay bracket (5 marks)
# ---------------------------------------------------------
def calculate_paye(gross_pay):
    """Calculate PAYE tax using if-elif-else based on gross pay bracket."""
    if gross_pay <= 10000:
        rate = 0.00
    elif gross_pay <= 20000:
        rate = 0.04
    elif gross_pay <= 30000:
        rate = 0.05
    else:
        rate = 0.06

    return gross_pay * rate


# ---------------------------------------------------------
# d. Calculate NHIF and NSSF (5 marks)
# ---------------------------------------------------------
def calculate_nhif(gross_pay):
    """NHIF = 2% of gross pay."""
    return gross_pay * 0.02


def calculate_nssf(basic_salary):
    """NSSF = 3% of basic salary."""
    return basic_salary * 0.03


# ---------------------------------------------------------
# e. Compute total deductions and net pay (5 marks)
# ---------------------------------------------------------
def calculate_net_pay(gross_pay, paye, nhif, nssf):
    """Net Pay = Gross Pay - (PAYE + NHIF + NSSF)."""
    total_deductions = paye + nhif + nssf
    net_pay = gross_pay - total_deductions
    return total_deductions, net_pay


# ---------------------------------------------------------
# f. Display all employee details and salary breakdown (5 marks)
# ---------------------------------------------------------
def display_payslip(payroll_number, name, gender, department, basic_salary,
                     gross_pay, paye, nhif, nssf, total_deductions, net_pay):
    print()
    print("=" * 45)
    print("           EMPLOYEE PAYSLIP")
    print("=" * 45)
    print(f"Payroll Number   : {payroll_number}")
    print(f"Name             : {name}")
    print(f"Gender           : {gender}")
    print(f"Department       : {department}")
    print("-" * 45)
    print(f"Basic Salary     : Ksh {basic_salary:,.2f}")
    print(f"House Allowance  : Ksh {HOUSE_ALLOWANCE:,.2f}")
    print(f"Medical Allowance: Ksh {MEDICAL_ALLOWANCE:,.2f}")
    print(f"Gross Pay        : Ksh {gross_pay:,.2f}")
    print("-" * 45)
    print(f"PAYE             : Ksh {paye:,.2f}")
    print(f"NHIF (2% gross)  : Ksh {nhif:,.2f}")
    print(f"NSSF (3% basic)  : Ksh {nssf:,.2f}")
    print(f"Total Deductions : Ksh {total_deductions:,.2f}")
    print("-" * 45)
    print(f"NET PAY          : Ksh {net_pay:,.2f}")
    print("=" * 45)


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------
def main():
    payroll_number, name, gender, department, basic_salary = capture_employee_details()

    gross_pay = calculate_gross_pay(basic_salary)
    paye = calculate_paye(gross_pay)
    nhif = calculate_nhif(gross_pay)
    nssf = calculate_nssf(basic_salary)
    total_deductions, net_pay = calculate_net_pay(gross_pay, paye, nhif, nssf)

    display_payslip(payroll_number, name, gender, department, basic_salary,
                     gross_pay, paye, nhif, nssf, total_deductions, net_pay)


if __name__ == "__main__":
    main()

