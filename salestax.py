square_feet = 115
paint_gallon = 1
hours = 8
charges = 20.00

#User input the square feet of wall space and price per gallon of the paints.

square_feet_space = float(input('Enter the square feet of wall space.'));
price_per_gallon = float(input('Enter the price of the paint per gallon.'));

#Calculations.

number_of_gallons = square_feet_space / square_feet
hours_required = number_of_gallons * hours
cost_of_paint = price_per_gallon * number_of_gallons
labor_charges = hours_required * charges
total_job_cost = cost_of_paint + labor_charges

#printing out results.

print('The number of  gallons of paint required :' , number_of_gallons )
print('The hours of labor required :', hours_required)
print('The cost of the paint is: ' , cost_of_paint)
print('The labor charges is :' , labor_charges)
print('The total cost of the paint job is :' '$', total_job_cost)
