# Sal's Shipping

Sal's Shipping is a Python program developed as part of the Learn Python 3 course on Codecademy. This program represents Sal's Shippers, the biggest shipping company in the tri-county area. The primary goal of this program is to provide customers with the most affordable shipping options based on the weight of their packages.

## Features

- **Ground Shipping**: Calculates shipping cost based on the weight of the package with a small flat charge.
- **Ground Shipping Premium**: Offers shipping at a higher flat charge without weight-based pricing.
- **Drone Shipping**: A new shipping method that charges based on weight but has no flat charge, typically at a higher rate than ground shipping.

## Shipping Rates

### Ground Shipping

| Weight of Package      | Price per Pound | Flat Charge |
|------------------------|-----------------|-------------|
| 2 lb or less           | $1.50           | $20.00      |
| Over 2 lb up to 6 lb   | $3.00           | $20.00      |
| Over 6 lb up to 10 lb  | $4.00           | $20.00      |
| Over 10 lb             | $4.75           | $20.00      |

### Ground Shipping Premium

- Flat charge: $125.00

### Drone Shipping

| Weight of Package      | Price per Pound | Flat Charge |
|------------------------|-----------------|-------------|
| 2 lb or less           | $4.50           | $0.00       |
| Over 2 lb up to 6 lb   | $9.00           | $0.00       |
| Over 6 lb up to 10 lb  | $12.00          | $0.00       |
| Over 10 lb             | $14.25          | $0.00       |

## Usage

Run `shipping.py` and enter the weight of your package when prompted. The program will then display the cheapest shipping method and the corresponding cost using Sal’s Shippers.

## Note

This program is part of the 'Learn Python 3' course on Codecademy. It provides a practical application of Python basics, including functions, conditionals, and user input handling.

Feel free to explore and modify the code to better understand the underlying logic and Python syntax!
