number_of_pizzas=eval(input("Сколько пицц вы хотите заказать?"))
cost_per_pizza=eval(input("Сколько стоит пицца?"))
subtotal=number_of_pizzas*cost_per_pizza # total price
tax_rate=0.08
sales_tax=subtotal*tax_rate
yotal=sales_tax+subtotal
print("Total pizzas cost - $", subtotal, "and tax - $", sales_tax)