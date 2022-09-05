from ships_list.additional_functions.supporting_functions. \
    additional_functions import assurance_question


# create a txt file through terminal
def create_template():
    assurance_question('create a new template')

    # input template name
    template_name = input('Write the name of the new template:\n')
    print(template_name)
    # input template text
    # TODO replace with input from file
    template_text = input('Write the text of the new template:\n')

    # create list of substrings
    list_of_substrings = create_list_of_substrings(template_text)

    # find '$$$' in template text and calculate quantity of '$$$' found
    quantity_of_dollars = template_text.count('$$$')
    print('Quantity of $$$ in template text is {}'.format(quantity_of_dollars))

    # check if quantity of '$$$' is same as quantity of substrings
    if quantity_of_dollars == len(list_of_substrings):
        print('Quantity of $$$ is same as quantity of substrings')
    else:
        print('Quantity of $$$ is not same as quantity of substrings')
        print('Quantity of $$$ is {}'.format(quantity_of_dollars))
        print('Quantity of substrings is {}'.format(len(list_of_substrings)))

    # create a list of keys for template
    keys = {}
    for i in range(quantity_of_dollars):
        print(
            'Please enter key for substring:\n{}'.format(
                list_of_substrings[i]))
        key = input('Write the key of the new template:\n')
        if key not in keys:
            keys[key] = input('Write the value of the key {}:\n'.format(key))

    # TODO create file with template
    # TODO add dict with template details to storage of template details

    return


# create list of substrings from input text that are 15 symbols before  $$$
# and 18 symbols after $$$
def create_list_of_substrings(template_text):
    list_of_substrings = []
    for i in range(len(template_text)):
        if template_text[i:i + 3] == '$$$':
            list_of_substrings.append(template_text[i - 15:i + 18])
    return list_of_substrings
