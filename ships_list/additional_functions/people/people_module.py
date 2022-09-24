from ships_list.lists.Standard.constants import PEOPLE_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator


# function input_email
def input_email():
    # input email
    email = input('Please enter email of person\n')
    # checking if email is valid
    if not email or '@' not in email:
        print('Email is not valid. Please try again.')
        email = input_email()
    # returning email
    return email


# function to create a person
def add_person():
    # creating a person
    person = {}
    # generating id
    person['id'] = id_generator()
    # adding person name
    person['person_name'] = input('Please enter person name\n')
    # adding email
    person['email'] = input_email()
    # adding phone number
    person['phone_number'] = input('Please enter phone number of person\n')
    # adding company
    person['company'] = input_from_list('company', list_of_companies())
    # adding role
    person['role'] = input('Please enter role of person\n')
    # save person to file
    append_JSON_file(person, PEOPLE_FILE)

    # printing created person
    print('\nCreated person with following details:\n')
    print(person)


def list_of_companies():
    # reading parties from file
    list_of_companies = read_JSON_file(PEOPLE_FILE)

    # return names of companies in list
    return list(map(lambda x: x['company_name'], list_of_companies))


# function to remove a person
def remove_person():
    # reading parties from file
    list_of_people = read_JSON_file(PEOPLE_FILE)

    if list_of_people == []:
        print('There are no people to remove.')
        return

    # creating list of person names
    list_of_names = list(
        map(lambda x: x['person_name'], list_of_people))

    # selecting person to remove
    person_to_remove = input_from_list('person to remove', list_of_names)

    # creating new list of parties without selected person
    result = list(filter(lambda x: x['person_name'] != person_to_remove,
                         list_of_people))

    # saving new list of parties to file
    write_JSON_file(PEOPLE_FILE, result)

    print('Company {} was removed'.format(person_to_remove))


# function to edit a person
def edit_person():
    # reading parties from file
    list_of_people = read_JSON_file(PEOPLE_FILE)

    # creating list of person names
    list_of_people = list(
        map(lambda x: x['person_name'], list_of_people))

    # selecting person to edit
    person_to_edit = input_from_list('person to edit', list_of_people)

    # select field to edit
    field_to_edit = input_from_list('field to edit',
                                    ['person_name', 'email',
                                        'phone_number', 'address'])
    # select new value of field
    new_value = input('Please enter new value of field\n')

    # updating value of field
    for person in list_of_people:
        if person['person_name'] == person_to_edit:
            person[field_to_edit] = new_value

    # saving new list of parties to file
    write_JSON_file(list_of_people, PEOPLE_FILE)

    # printing updated person
    print('\nUpdated person with following was saved details:\n')
    for person in list_of_people:
        if person['person_name'] == person_to_edit:
            print(person)
