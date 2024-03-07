# Constants
FLAT_CHARGE_GROUND = 20.00
GROUND_SHIPPING_PREMIUM = 125.00
COST_MESSAGE = "The cost of {} your order is: $"

def calculate_ground_shipping(weight):
    if weight <= 2:
        return 1.50 * weight + FLAT_CHARGE_GROUND
    elif weight <= 6:
        return 3.00 * weight + FLAT_CHARGE_GROUND
    elif weight <= 10:
        return 4.00 * weight + FLAT_CHARGE_GROUND
    else:
        return 4.75 * weight + FLAT_CHARGE_GROUND

def calculate_drone_shipping(weight):
    if weight <= 2:
        return 4.50 * weight
    elif weight <= 6:
        return 9.00 * weight
    elif weight <= 10:
        return 12.00 * weight
    else:
        return 14.25 * weight

# Ask user for weight
try:
    weight = float(input("Please enter the weight of your package in pounds: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()

# Calculate and print costs
ground_cost = calculate_ground_shipping(weight)
print(f"{COST_MESSAGE.format('ground shipping')} {ground_cost}")

premium_ground_cost = GROUND_SHIPPING_PREMIUM
print(f"{COST_MESSAGE.format('premium ground shipping')} {premium_ground_cost}")

drone_cost = calculate_drone_shipping(weight)
print(f"{COST_MESSAGE.format('drone shipping')} {drone_cost}")
