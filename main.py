from numbers import num_perfume, num_medicine, num_cosmetics



def main_menu():
    input("Press any button to start ")
    assign_area_and_number(num_perfume, num_medicine, num_cosmetics)


def assign_area_and_number(num_perfume, num_medicine, num_cosmetics):
    procedure_choice = input("What procedure do you want to perform?\n"
                             "choose P for 'Perfume, M for 'Medicine or"
                             " C for 'Cosmetics ")
    if procedure_choice == "P":
        num_perfume = next(num_perfume)
        print (f"Your number is {procedure_choice}-{num_perfume}")
        print('*' * 23)
        print ("Please, wait for your turn")
    elif procedure_choice == "M":
        num_medicine = next(num_medicine)
        print(f"Your number is {procedure_choice}-{num_medicine}")
        print('*' * 23)
        print("Please, wait for your turn")
    elif procedure_choice == "C":
        num_cosmetics = next(num_cosmetics)
        print(f"Your number is {procedure_choice}-{num_cosmetics}")
        print('*' * 23)
        print("Please, wait for your turn")
    another_number()


def another_number():
    user_input2 = input("Do you need another number?\n"
          "Y/N " )
    if user_input2 == "Y":
        assign_area_and_number(num_perfume, num_medicine, num_cosmetics)
    else:
        main_menu()
assign_area_and_number(num_perfume, num_medicine, num_cosmetics)