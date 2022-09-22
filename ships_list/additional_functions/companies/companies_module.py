from ships_list.lists.Standard.constants import PARTIES_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file, read_JSON_file, write_JSON_file
from ships_list.additional_functions.supporting_functions.input_functions \
    import input_from_list
from ships_list.additional_functions.supporting_functions.additional_functions\
    import id_generator

# function to create a company


def create_company():
    # creating a party
    party = {}
    # generating id
    party['id'] = id_generator()
    # adding company name
    party['company_name'] = input('Please enter company name\n')
    # adding email
    party['email'] = input('Please enter email of party\n')
    # adding phone number
    party['phone_number'] = input('Please enter phone number of party\n')
    # adding address
    party['address'] = input('Please enter address of party\n')
    # save party to file
    append_JSON_file(party, PARTIES_FILE)


# function to remove a company
def remove_company():
    # reading parties from file
    list_of_companies = read_JSON_file(PARTIES_FILE)

    # creating list of company names
    list_of_companies = list(
        map(lambda x: x['company_name'], list_of_companies))

    # selecting company to remove
    company_to_remove = input_from_list('company to remove', list_of_companies)

    # creating new list of parties without selected company
    list_of_companies = list(filter(lambda x:
                                    x['company_name'] != company_to_remove,
                                    list_of_companies))

    # saving new list of parties to file
    write_JSON_file(list_of_companies, PARTIES_FILE)


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
