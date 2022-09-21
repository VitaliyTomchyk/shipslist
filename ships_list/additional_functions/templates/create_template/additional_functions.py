# add template information to dictionary of json files
from ships_list.additional_functions.supporting_functions.json_functions \
    import write_JSON_file, read_JSON_file
from ships_list.lists.Standard.constants import KEYS_OF_TEMPLATES_FILE


def add_template_to_list(new_created_template):

    # collecting list of templates
    list_of_templates = read_JSON_file(KEYS_OF_TEMPLATES_FILE)

    template_name = list(new_created_template.keys())[0]

    list_of_templates.append(new_created_template)

    write_JSON_file(KEYS_OF_TEMPLATES_FILE,
                    list_of_templates)

    print('Your new template {} has been added.'.format(template_name))


def keys_of_template_finder(template_text):
    list_of_words = template_text.split()
    list_of_keys = list(filter(lambda x: x.startswith('$'), list_of_words))
    updated_list_of_keys = list(set(map(
        lambda x: x[1:-1 if not x[-1:].isalpha() else None],
        list_of_keys)))
    return updated_list_of_keys
