def cm_to_inches(centimeters):

    # Conversion ratio: 1 inch = 2.54 centimeters
    return round(centimeters / 2.54, 2)

def main():
    try:
        # Get input from user
        cm = float(input("Enter length in centimeters: "))
        
        # Validate input
        if cm < 0:
            print("Error: Length cannot be negative!")
            return
            
        # Convert and display result
        inches = cm_to_inches(cm)
        print(f"\n{cm} centimeters = {inches} inches")
        
        # Show example calculation
        print("\nExample verification:")
        print("25.4 centimeters = 10.0 inches")
        
    except ValueError:
        print("Error: Please enter a valid number!")

if __name__ == "__main__":
    main()