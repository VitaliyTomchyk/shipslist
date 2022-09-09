from ships_list.additional_functions.supporting_functions. \
    additional_functions import assurance_question
from ships_list.additional_functions.supporting_functions.json_functions \
    import write_JSON_file, read_JSON_file
from ships_list.lists.Standard.constants import SUPPORTING_FILE


# create a txt file through terminal
def create_template():

    instructions = 'This function is used to create a new template.\n\n\
Add a dollar sign ($) before the word that is a variable. After the template\n\
is created you can use the function -fill_template for your new template.\n\n\
Good luck!\n\n'
    print(instructions)
    assurance_question('create a new template')

    # input template name
    template_name = input('Write the name of the new template:\n')
    address_of_template = (f'ships_list/files/{template_name}')

    # input template text
    # TODO replace with input from file
    template_text = input('Write the text of the new template:\n')
    with open(address_of_template, 'w') as f:
        f.write(template_text)
        f.write('\n')
        f.close()

    # for every word after $ in template_text, add it to the list of words
    words = []
    for word in template_text.split():
        if word.startswith('$'):
            if word.endswith('.'):
                word = word[1:-1]
                words.append(word)
            else:
                word = word[1:]
                words.append(word)

    # add dict with template details to storage of template details
    result = {
        template_name: {
            "address_of_template": address_of_template,
            "keys_of_tmplt": words
        }}

    return add_template_to_dict(result)


# add template information to dictionary of json files


def add_template_to_dict(new_created_template):
    dict = read_JSON_file(SUPPORTING_FILE)
    dict_to_append = dict['templates']
    template_name = list(new_created_template.keys())[0]
    dict_to_append[template_name] = new_created_template[template_name]
    print(dict_to_append[template_name])
    write_JSON_file(SUPPORTING_FILE, dict_to_append)
