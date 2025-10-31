           #TASK 3.1
''' Objective:
Build a Python program for TGNPDCL (Telangana Northern Power Distribution Company Limited) to generate an electricity bill based on 
energy consumption and type of customer.
Requirements:
1. Read inputs: previous units (PU), current units (CU), and customer type (Domestic, Commercial, or Industrial)
2. Calculate:
  - EC (Energy Charges)
  - FC (Fixed Charges)
  - CC (Customer Charges)
  - ED (Electricity Duty, 5% of EC)
  - Total Bill = EC + FC + CC + ED
3. Print a clear bill summary with all details.
4. Use simple logic for rates:
5. Use AI assistance to generate the full code structure, input handling, and output formatting.
Task:
 Generate the complete Python code for this electricity bill calculator.
'''
# ---------------------------------------------------------
# TGNPDCL Electricity Bill Generator
# ---------------------------------------------------------

# Step 1: Input details
customer_name = input("Enter customer name: ")
customer_type = input("Enter customer type (Domestic/Commercial/Industrial): ").strip().lower()
PU = float(input("Enter previous units: "))
CU = float(input("Enter current units: "))

# Step 2: Calculate number of units consumed
units_consumed = CU - PU

# Step 3: Set rates based on customer type
if customer_type == "domestic":
    FC = 50
    CC = 20
    if units_consumed <= 100:
        EC = units_consumed * 1.45
    elif units_consumed <= 200:
        EC = (100 * 1.45) + (units_consumed - 100) * 2.60
    else:
        EC = (100 * 1.45) + (100 * 2.60) + (units_consumed - 200) * 3.60

elif customer_type == "commercial":
    FC = 100
    CC = 50
    if units_consumed <= 100:
        EC = units_consumed * 3.00
    elif units_consumed <= 200:
        EC = (100 * 3.00) + (units_consumed - 100) * 4.50
    else:
        EC = (100 * 3.00) + (100 * 4.50) + (units_consumed - 200) * 6.00

elif customer_type == "industrial":
    FC = 200
    CC = 100
    if units_consumed <= 100:
        EC = units_consumed * 5.00
    elif units_consumed <= 200:
        EC = (100 * 5.00) + (units_consumed - 100) * 6.50
    else:
        EC = (100 * 5.00) + (100 * 6.50) + (units_consumed - 200) * 7.50

else:
    print("Invalid customer type!")
    exit()

# Step 4: Electricity Duty (ED)
ED = 0.05 * EC   # 5% duty on energy charges

# Step 5: Total Bill
total_bill = EC + FC + CC + ED

# Step 6: Print the Bill
print("\n---------- TGNPDCL ELECTRICITY BILL ----------")
print(f"Customer Name        : {customer_name}")
print(f"Customer Type        : {customer_type.capitalize()}")
print(f"Previous Units (PU)  : {PU}")
print(f"Current Units (CU)   : {CU}")
print(f"Units Consumed       : {units_consumed}")
print("----------------------------------------------")
print(f"Energy Charges (EC)  : ₹{EC:.2f}")
print(f"Fixed Charges  (FC)  : ₹{FC:.2f}")
print(f"Customer Charges(CC) : ₹{CC:.2f}")
print(f"Electricity Duty (ED): ₹{ED:.2f}")
print("----------------------------------------------")
print(f"Total Bill Amount    : ₹{total_bill:.2f}")
print("----------------------------------------------")
