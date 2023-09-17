def budget_splitter(names, incomes, expenses):
    combined_spending_money = sum(incomes) - sum(expenses)
    if combined_spending_money < 0:
        return "Total expenses exceed total income. Adjust your expenses."

    spending_percentages = [income / sum(incomes) for income in incomes]
    spending_amounts = [combined_spending_money * percentage for percentage in spending_percentages]

    results = []
    for name, income, expense, spending_amount in zip(names, incomes, expenses, spending_amounts):
        remaining_income = income - expense
        personal_percentages = (remaining_income / sum([income - expense for income, expense in zip(incomes, expenses)])) * 100
        individual_spending = remaining_income + spending_amount
        results.append({
            'name': name,
            'income': income,
            'expense': expense,
            'spending_amount': spending_amount,
            'remaining_income': remaining_income,
            'individual_spending': individual_spending,
            'personal_percentage': personal_percentages,
        })
    print("Intermediate Results:")
    for result in results:
        print(result)

    return results

