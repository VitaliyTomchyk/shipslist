# import fucntion json_load
from ships_list.additional_functions.supporting_functions.json_functions \
    import read_JSON_file
from ships_list.lists.Standard.constants import SUPPORTING_FILE


def fill_template():
    # choose template
    list_of_templates = read_JSON_file(SUPPORTING_FILE)
    list_of_templates_names = list(map(lambda x: x("template_name"),
                                       list_of_templates))
    return list_of_templates_names
    # fill keys

    # print filled template
    # print(result)
