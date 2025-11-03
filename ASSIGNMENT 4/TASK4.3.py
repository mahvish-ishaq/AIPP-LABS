def format_name(full_name):

    # Handle empty or None input
    if not full_name:
        return ""
        
    # Split the name into parts
    parts = full_name.strip().split()
    
    # Handle single name case
    if len(parts) == 1:
        return parts[0]
        
    # Extract last name and remaining parts
    last_name = parts[-1]
    first_and_middle = " ".join(parts[:-1])
    
    # Return formatted name
    return f"{last_name}, {first_and_middle}"

def main():
    print("Name Formatter (Last, First)")
    print("Enter 'quit' to exit\n")
    
    # Example demonstrations
    examples = [
        "John Smith",
        "Mary Jane Wilson",
        "James"
    ]
    
    print("Examples:")
    for example in examples:
        formatted = format_name(example)
        print(f'Input: "{example}" → Output: "{formatted}"')
    
    print("\nNow try your own:")
    while True:
        # Get user input
        name = input("\nEnter a name: ")
        
        # Check for quit command
        if name.lower() == 'quit':
            print("Goodbye!")
            break
            
        # Format and display result
        try:
            formatted_name = format_name(name)
            print(f'Formatted: "{formatted_name}"')
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()