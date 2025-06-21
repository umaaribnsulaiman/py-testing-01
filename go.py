import math

# def exponential_growth(base, rate, periods):
#     """
#     Returns a list of numbers showing exponential growth.
#     base: initial value
#     rate: growth rate per period (e.g., 2 for doubling)
#     periods: number of periods to grow
#     """
#     values = []
#     for t in range(periods + 1):
#         value = base * (rate ** t)
#         values.append(value)
#     return values

# # Example usage:
# if __name__ == "__main__":
#     base = 1
#     rate = 2  # Doubles each period
#     periods = 20
#     growth = exponential_growth(base, rate, periods)
#     print(growth)

# hot_day=False
# cold_day=False
# # Example usage:
# if hot_day:
#     print("It's a hot day!")
#     print("Stay hydrated!")
#     print("Have a great day!")
# elif cold_day:
#     print("It's a cold day!")
#     print("Wear a warm coat!")
#     print("Have a cozy day!")
# else:
#     print("It's a pleasant day!")
#     print("Lets play fortnite!")

# price=100
# has_good_credit=True
# down_payment=0
# print(f"Down payment: ${down_payment}")
# # Determine down payment based on credit status
# if has_good_credit:
#     down_payment = price * 0.1
#     print(f'has good credit')
# else:
#     down_payment = price * 0.2
#     print(f'Does not have good credit')
    
# print(f"Down payment: ${down_payment}")


# high_income = True
# good_credit = True
# if high_income and good_credit:
#     print("Eligible for loan")
# elif high_income or good_credit:
#     print("Eligible for a part of the loan with higher interest")
# else:
#     print("Not eligible for loan")


# temperature = 10  # Example temperature in Celsius
# if temperature== 30:
#     print("It's a hot day!")
# elif temperature <= 20:
#     print("It's a cold day!")
# else:
#     print("It's a nice day, let's play outdoor!")

name='''UMAR IBN SULEIMAN'''
if len(name)<3:
     print("Name must be at least 3 characters long")
elif len(name)>50:
    print("Name can be a maximum of 50 characters long")
else:
    print("Name looks good")
    