# Initial variables
age = 28
sex = 0  # 0: Female, 1: Male
bmi = 26.2
num_of_children = 3
smoker = 0  # 0: Non-smoker, 1: Smoker

# Initial insurance estimate formula
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# Age Factor: Increasing age by 4 years
age += 4
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars")

# Reset age and increase BMI by 3.1
age = 28  # Resetting age to original
bmi += 3.1  # Increasing BMI
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars")

# Male vs. Female Factor: Changing sex from female to male
bmi = 26.2  # Resetting BMI to original
sex = 1  # Changing sex to male
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is " + str(change_in_insurance_cost) + " dollars.")

# Smoker Factor
smoker = 1  # Changing smoker status to smoker
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost for being a smoker instead of a non-smoker is " + str(change_in_insurance_cost) + " dollars.")

# Number of Children Factor
num_of_children = 5  # Changing the number of children
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing the number of children to 5 is " + str(change_in_insurance_cost) + " dollars.")
