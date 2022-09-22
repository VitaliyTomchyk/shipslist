from ships_list.lists.Standard.constants import PARTIES_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator


# function input_email
def input_email():
    # input email
    email = input('Please enter email of company\n')
    # checking if email is valid
    if not email or '@' not in email:
        print('Email is not valid. Please try again.')
        email = input_email()
    # returning email
    return email


# function to create a company
def add_company():
    # creating a company
    company = {}
    # generating id
    company['id'] = id_generator()
    # adding company name
    company['company_name'] = input('Please enter company name\n')
    # adding email
    company['email'] = input_email()
    # adding phone number
    company['phone_number'] = input('Please enter phone number of company\n')
    # adding address
    company['address'] = input('Please enter address of company\n')
    # save company to file
    append_JSON_file(company, PARTIES_FILE)

    # printing created company
    print('\nCreated company with following details:\n')
    print(company)


# function to remove a company
def remove_company():
    # reading parties from file
    list_of_companies = read_JSON_file(PARTIES_FILE)

    if list_of_companies == []:
        print('There are no companies to remove.')
        return

    # creating list of company names
    list_of_names = list(
        map(lambda x: x['company_name'], list_of_companies))

    # selecting company to remove
    company_to_remove = input_from_list('company to remove', list_of_names)

    # creating new list of parties without selected company
    result = list(filter(lambda x: x['company_name'] != company_to_remove,
                         list_of_companies))

    # saving new list of parties to file
    write_JSON_file(PARTIES_FILE, result)

    print('Company {} was removed'.format(company_to_remove))


# function to edit a company
def edit_company():
    # reading parties from file
    list_of_companies = read_JSON_file(PARTIES_FILE)

    # creating list of company names
    list_of_companies = list(
        map(lambda x: x['company_name'], list_of_companies))

    # selecting company to edit
    company_to_edit = input_from_list('company to edit', list_of_companies)

    # select field to edit
    field_to_edit = input_from_list('field to edit',
                                    ['company_name', 'email',
                                        'phone_number', 'address'])
    # select new value of field
    new_value = input('Please enter new value of field\n')

    # updating value of field
    for company in list_of_companies:
        if company['company_name'] == company_to_edit:
            company[field_to_edit] = new_value

    # saving new list of parties to file
    write_JSON_file(list_of_companies, PARTIES_FILE)

    # printing updated company
    print('\nUpdated company with following was saved details:\n')
    for company in list_of_companies:
        if company['company_name'] == company_to_edit:
            print(company)
