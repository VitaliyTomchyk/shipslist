# add template information to dictionary of json files
from ships_list.additional_functions.supporting_functions.json_functions \
    import write_JSON_file, read_JSON_file


def add_template_to_dict(new_created_template):

    # collecting list of templates
    list_of_dicts = read_JSON_file('ships_list/lists/templates/' +
                                   'created_template.json')
    dict_to_append = list_of_dicts['templates']

    template_name = list(new_created_template.keys())[0]

    dict_to_append[template_name] = new_created_template[template_name]

    write_JSON_file('ships_list/lists/templates/created_template.json',
                    list_of_dicts)

    print('Your new template {} has been added.'.format(template_name))


def keys_of_template_finder(template_text):
    list_of_keys = []
    for word in template_text.split():
        if word.startswith('$'):
            list_of_keys.append(word[1:-1 if not word[-1:].isalpha()
                                     else None])
    result = list(set(list_of_keys))
    return result
