def check_credit_score(score):

    if score >= 750:
        return "Excellent"
    elif score >= 650:
        return "Good"
    elif score >= 550:
        return "Average"
    else:
        return "Poor"


def evaluate_loan(income, loan_amount, credit_score, employment_years):

    credit_category = check_credit_score(credit_score)

    if credit_category == "Excellent":

        if income >= loan_amount * 0.3:
            return "Loan Approved (Premium Rate)"
        else:
            return "Loan Approved (Standard Rate)"

    elif credit_category == "Good":

        if employment_years >= 2 and income >= loan_amount * 0.4:
            return "Loan Approved"
        else:
            return "Further Financial Review Required"

    elif credit_category == "Average":

        if employment_years >= 3 and income >= loan_amount * 0.5:
            return "Loan Approved with Conditions"
        else:
            return "Loan Rejected"

    else:

        if income >= loan_amount * 0.6 and employment_years >= 5:
            return "Loan Approved with High Interest"
        else:
            return "Loan Rejected"


def main():

    income = float(input("Enter annual income: "))
    loan_amount = float(input("Enter requested loan amount: "))
    credit_score = int(input("Enter credit score: "))
    employment_years = int(input("Years of employment: "))

    result = evaluate_loan(income, loan_amount, credit_score, employment_years)

    print("\nLoan Decision:", result)


main()
