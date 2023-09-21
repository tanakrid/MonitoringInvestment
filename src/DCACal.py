from Fund import Fund

def find_monthly_investment(initial_investment, monthly_investment, annual_growth_rate, years, target):

    # Initialize variables
    total_investment = initial_investment

    # Calculate the number of months
    months = years * 12

    # Simulate DCA over time
    for month in range(months):
        # Calculate the monthly growth
        monthly_growth = (1 + annual_growth_rate / 12)
        # Add the monthly investment
        total_investment += monthly_investment
        # Calculate the new investment value
        total_investment *= monthly_growth
    
    if total_investment < target:
        return find_monthly_investment(initial_investment, monthly_investment + 1000, annual_growth_rate, years, target)
    else:
        return monthly_investment


def calculate_dca(initial_investment, monthly_investment, annual_growth_rate, years, target):
    # Initialize variables
    investment_values = []
    total_investment = initial_investment
    investment_capital = initial_investment
    my_age = 25
    milestone = [36,42,48,54,60]

    # indicator
    time_to_free_finance = 0
    time_to_retire = 0

    milestone_36 = 0
    milestone_42 = 0
    milestone_48 = 0
    milestone_54 = 0
    milestone_60 = 0

    # Calculate the number of months
    months = years * 12
    month = 0

    # Simulate DCA over time
    while True:
        # Calculate the monthly growth
        monthly_growth = (1 + annual_growth_rate / 12)
        # Add the monthly investment
        total_investment += monthly_investment
        # Calculate the new investment value
        total_investment *= monthly_growth
        investment_capital += monthly_investment

        if total_investment > target:
            time_to_retire = month/12
            break
        if total_investment * (annual_growth_rate / 12) > 30000 and time_to_free_finance == 0:
            time_to_free_finance = month/12
        month += 1        

        if month/12 + my_age in milestone:
            print(f"Years {month/12} -> total_investment: [${total_investment:,.2f}], investment_capital: [${investment_capital:,.2f}], diff: [${total_investment - investment_capital:,.2f}], profit: [${total_investment * (annual_growth_rate / 12):,.2f}]")

    print(f"time_to_free_finance: {time_to_free_finance}")
    print(f"time_to_retire: {time_to_retire}")

def get_revenue_per_year(): 
    # Example usage
    initial_investment = 10000  # Initial investment amount
    monthly_investment = 20000   # Monthly investment amount
    annual_growth_rate = 0.08  # Annual growth rate (8%)
    years = 30                  # Number of years
    target = 30000000

    monthly_investment = find_monthly_investment(initial_investment, monthly_investment, annual_growth_rate, years, target)
    print(f"satisfy monthly_investment: {monthly_investment} on target: {target}")
    calculate_dca(initial_investment, monthly_investment, annual_growth_rate, years, target)

    test = Fund('HP', '10.00')
    print(f"name: {test.name}, nav: {test.nav}")

main()