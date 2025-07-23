import string

# Pre-programmed signs
signs = {}

# Letters A-Z assigned to A1 - A26
for i, letter in enumerate(string.ascii_uppercase, start=1):
    signs[letter] = f"A{i}"

# Numbers 1-9 assigned to B1 - B9
for i in range(1, 10):
    signs[str(i)] = f"B{i}"

def lookup_sign():
    print("\nLookup Sign")
    sign_name = input("Enter the sign's name (letter A-Z or number 1-9): ").strip().upper()
    code = signs.get(sign_name)
    if code:
        print(f"\n'{sign_name}' is in group #{code}")
    else:
        print(f"\nNo record found for '{sign_name}'.")
    input("\nPress Enter to return to menu...")

def list_all_signs():
    print("\nAll Signs")
    for name, code in sorted(signs.items()):
        print(f"- {name}: {code}")
    input("\nPress Enter to return to menu...")

def main():
    while True:
        print("\nSign Organizer (Pre-Programmed A-Z & 1-9)")
        print("----------------------------------------")
        print("1. Lookup a sign")
        print("2. List all signs")
        print("3. Exit")
        choice = input("\nSelect an option (1-3): ").strip()
        if choice == '1':
            lookup_sign()
        elif choice == '2':
            list_all_signs()
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter 1-3.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
