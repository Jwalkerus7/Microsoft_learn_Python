user_response = input("Would you like to continue? ")

if user_response == "yes" or user_response == "y":
    print("Continuing ...")
    print("Complete!")
elif user_response == "no" or user_response == "n":
    print("Exiting")
else:
    print("Please try again and respond with yes or no.")
    
