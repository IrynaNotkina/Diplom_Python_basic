from Person_class_final import Person
import time


def selection_safe():
    select_excel_file = input('Data will be saved to the main PEOPLE BASE "PEOPLE_MAIN_DATABASE.xlsx"'
                              '. Save data to the new file - type (N): ').upper()
    if select_excel_file == 'N':
        excel_file_name1 = input('Write new file name: ').upper()
    else:
        excel_file_name1 = 'PEOPLE_MAIN_DATABASE'

    Person.save_to_excel(f'{excel_file_name1}.xlsx')
    print(f'The data has been appended to the Excel file: {excel_file_name1}.xlsx')


while True:
    cases = ['A', 'S', 'T', 'P', 'E', 'I', 'Q']
    select_action = input("""        Type A for add new entry
        Type S for make search
        Type T for get the amount of entries in the PEOPLE BASE
        Type P for print all entries in the PEOPLE BASE
        Type E for save to excel
        Type I for upload from excel
        Type Q to quit
        PLEASE MAKE YOUR SELECTION: """).upper()

    if select_action not in cases:
        print("Invalid selection. Please try again.")
        time.sleep(1)

    elif select_action == 'S':
        repeat = 'Y'
        while repeat.upper() == 'Y':
            Person.search_person()
            repeat = input('One more search request, type (Y): ').upper()
            time.sleep(1)

    elif select_action == 'A':
        repeat = 'Y'
        while repeat.upper() == 'Y':
            print(Person.create_person())
            repeat = input('One more entry, type (Y): ').upper()
            time.sleep(1)

    elif select_action == 'E':
        selection_safe()

    elif select_action == 'T':
        print('Currently amount of entries in the PEOPLE BASE: ', len(Person.PEOPLE_BASE))
        time.sleep(1)

    elif select_action == 'P':
        if not Person.PEOPLE_BASE:
            print('No entries in the PEOPLE BASE')
        else:
            for person in Person.PEOPLE_BASE:
                print(person.number, ':', person)
        time.sleep(1)

    elif select_action == 'I':
        excel_file_name = input('Enter the file name for upload data: ')
        Person.load_from_excel(f'{excel_file_name}.xlsx')
        print(f'The data has been uploaded from the Excel file: {excel_file_name}.xlsx')
        time.sleep(3)

    elif select_action == 'Q':
        if Person.PEOPLE_BASE:
            save = input('If you want to save inputs to the Excel file, write (Y): ').upper()
            if save == 'Y':
                selection_safe()
                print("You have exited the program")
                break
            else:
                print("You have exited the program without saving")
        else:
            print("No entries to save. Exiting the program.")
        break






