def budget_splitter(names, incomes, expenses):
    combined_spending_money = sum(incomes) - sum(expenses)
    if combined_spending_money < 0:
        return "Total expenses exceed total income. Adjust your expenses."

    spending_percentages = [income / sum(incomes) for income in incomes]
    spending_amounts = [combined_spending_money * percentage for percentage in spending_percentages]

    results = []
    for name, income, expense in zip(names, incomes, expenses):
        remaining_income = income - expense
        personal_percentages = (remaining_income / sum([income - expense for income, expense in zip(incomes, expenses)])) * 100
        results.append({
            'name': name,
            'income': income,
            'expense': expense,
            'remaining_income': remaining_income,
            'personal_percentage': personal_percentages,
        })
    print("Intermediate Results:")
    for result in results:
        print(result)

    return results

