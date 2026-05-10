import time 

while True:
    print("\n==== DREAMS FILE MANAGER ====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        file = open("dreams.txt", "r")
        print("\n-----------------------------------------")
        print("\t--- Inspiring Messages ---")
        print("-----------------------------------------")
        content = file.read()
        print(content)
        file.close()
        time.sleep(1)
        print("-----------------------------------------")
        file = open("dreams.txt", "w")
        file.write("\n-Ang buhay dapat ine-enjoy mo lang, ganon wag pahirapan ang sarili.")
        file.write("\n-Wag kang matakot na magkamali, hindi tama yan.")
        file.write("\n-Wag kang mag papatukso sa mga tumutukso sayo, layuan mo ang tumutukso sayo para hindi ka matukso.\n\n")
        file.close()

    elif choice == "2":
        new = input("Enter your new inspiring line: ")
        file = open("dreams.txt", "a")
        print("\n-----------------------------------------")
        file.write(new + "\n")
        file.close()
        print("Your inspiration has been added!")
        time.sleep(1)
        print("-----------------------------------------")

    elif choice == "3":
        print("Warning: This will overwrite the file.")
        confirm = input("Type \"yes\" to continue: ")
        if confirm == "yes":
            new_text = input("Enter your new set of inspiring messages:\n")
            file = open("dreams.txt", "w")
            print("\n-----------------------------------------")
            file.write(new_text)
            file.close()
            print("File has been overwritten.")
            time.sleep(1)
            print("-----------------------------------------")

    elif choice == "4":
        print("\n-----------------------------------------")
        print("THANKKKKKYOUUUUUUU!!!!!!!")
        print("-----------------------------------------")
        break      
    
    else:
        print("Invalid choice!")