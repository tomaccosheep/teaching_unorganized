in_number = input('Give me a number between 10 and 20\n:')
if int(in_number) < 10:
    print("That number is too small!")
elif int(in_number) > 20:
    print("That number is too large!")
elif int(in_number) <= 20 and int(in_number) >= 10:
    print("Thank you :)")
