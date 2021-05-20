goal = int(input("What is your savings goal: "))
deposit = int(input("What is your monthly deposit: "))
interest = int(input("What is the annual interest rate: "))
print("")

total = 1000
month = 1

while total <= goal:
  monthly_interest = total / 120
  format_total = "{:.2f}".format(total)
  print(f"Month {month}: You have saved: ${format_total}")
  total += deposit + monthly_interest
  month += 1
  if total > goal:
    format_total = "{:.2f}".format(total)
    print(f"Month {month}: You have saved: ${format_total}")


print(f"It will take {month} months to save ${goal}")


