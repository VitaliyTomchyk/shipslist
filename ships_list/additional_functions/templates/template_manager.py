# template filler
from ships_list.lists.Standard.constants import FILLED_TEMPLATES_FILE
from ships_list.additional_functions.supporting_functions.json_functions \
    import append_JSON_file

input_data = {
    "company_name": input("Enter your name of the company: "),
    "company_to":
    input("Enter the name of the company you are sending the message to: ")
}


def fill_template():
    input_data

    template = (f'''
From: {input_data["company_name"]}
To: {input_data["company_to"]}
''')

    template_info = {
        'input_data': input_data,
        'text': template
    }

    append_JSON_file(template_info, FILLED_TEMPLATES_FILE)

    return print(template)
