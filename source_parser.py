import re

def parse_signature(source_code, max_params=10):
    type_name = "[a-zA-Z0-9\_:<>]+"
    variable_name = "[a-zA-Z0-9\_:<>]+"
    space = "\s+"
    any_space = "[\\n\\r\s]*"
    beginning_characters = "[^a-zA-Z0-9\_]*"
    #modifiers = f"(?:const)|[*&]" # TODO
    #declaration = f"(?:const{space}(?:[&\*]{any_space})?)?{type_name}{any_space}[&\*]?{space}[&\*]?{variable_name}"
    declaration = f"{type_name}{any_space}[&\*]*{space}[&\*]*{variable_name}"
    parameter = lambda capture: f"(?:{any_space}(?:const{space})?{('(' if capture else '') + declaration + (')' if capture else '')},?{any_space})"
    regex_string = f"{beginning_characters}(?:const{space})?({declaration}){any_space}\\({(parameter(True) + '?')*(max_params)}{parameter(False)}*\\){any_space}(?:const{any_space})?\\{{.*"
    regex = re.compile(regex_string)
    result_tuples = regex.findall(source_code)
    result_list = list(map(lambda signature_tuple: list(signature_tuple), result_tuples))
    return result_list