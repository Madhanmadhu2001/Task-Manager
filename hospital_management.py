def main():
    try:
        # Initialize patients list
        patientsList = []
        with open("patientsList.txt", "r") as infile:
            line = infile.readline()
            while line:
                patientsList.append(line.rstrip("\n").split(","))
                line = infile.readline()

    except FileNotFoundError:
        print("The 'patientsList.txt' file is not found.")
        print("Starting a new patients list!")
        patientsList = []
    
    choice = 0
    while choice != 5:
        print("\n*** Hospital Management System ***")
        print("1. Add a Patient")
        print("2. Get Patient Information")
        print("3. Display All Patients")
        print("4. Delete a Patient")
        print("5. Quit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            print("Adding a patient...")
            name = input("Enter the patient's name: ")
            patient_id = input("Enter the patient's ID: ")
            Medican = input("Enter the patient's Medican: ")
            room_number = input("Enter the patient's room number: ")

            patientsList.append([name, patient_id, Medican, room_number])

        elif choice == 2:
            print("Looking up a patient...")
            keyword = input("Enter the name of the patient: ")
            found = False
            for patient in patientsList:
                if keyword.lower() in patient[0].lower():  # case-insensitive search for patient name
                    print(patient)
                    found = True
            if not found:
                print("No patient found with that name.")

        elif choice == 3:
            print("Displaying all patients...")
            if patientsList:
                for i, patient in enumerate(patientsList):
                    print(f"{i+1}. Name: {patient[0]}, ID: {patient[1]}, Medican: {patient[2]}, Room: {patient[3]}")
            else:
                print("No patients in the list.")

        elif choice == 4:
            print("Deleting a patient...")
            delete_name = input("Enter the name of the patient to delete: ")
            found = False
            for i, patient in enumerate(patientsList):
                if delete_name.lower() == patient[0].lower():  # case-insensitive comparison
                    del patientsList[i]
                    print(f"Deleted patient: {patient[0]}")
                    found = True
                    break
            if not found:
                print(f"No patient found with the name '{delete_name}'.")

        elif choice == 5:
            print("Quitting Program")

    print("Program Terminated")

    # Saving the patients to the external file
    with open("patientsList.txt", "w") as outfile:
        for patient in patientsList:
            outfile.write(",".join(patient) + "\n")

if __name__ == "__main__":
    main()
