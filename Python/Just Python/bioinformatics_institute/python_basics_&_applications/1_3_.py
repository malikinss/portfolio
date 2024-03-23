'''
TODO:
        

name_spaces = {
                name_space:{
                    parent: parent_name_space,
                    name_spaces: [child_name_space1, child_name_space2,],
                    variables: [var1, var2, var3]
                } 
}
'''
def get_namespace_template():
    template = {
        'parent': None,
        'namespaces': [],
        'variables': []}
        
    return template

def update_parent_record(namespaces, parent, place_to_update, data):
    namespaces[parent][place_to_update].append(data)
    return namespaces

def add_data_to_namespace(namespaces, cur_space, key, data):
    namespaces[cur_space][key].append(data)
    return namespaces

def update_namespace_parent_key(namespaces, cur_space, data):
    namespaces[cur_space]['parent'] = data
    return namespaces

def is_namespace_exist(namespaces, namespace):
    return namespace in namespaces.keys()

def create_new_namespace(namespaces, namespace):
    if not is_namespace_exist(namespaces, namespace):
        namespaces[namespace] = get_namespace_template()

    return namespaces    

def add_var_to_namespace(namespaces, cur_space, variable):
    namespaces = create_new_namespace(namespaces, cur_space)
    namespaces = add_data_to_namespace(namespaces, cur_space, 'variables', variable)
    
    return namespaces


def add_namespace(namespaces, cur_space, parent):
    namespaces = create_new_namespace(namespaces, cur_space)


namespaces = {}
namespaces = add_var_to_namespace(namespaces, 'global', 'a')
namespaces = add_var_to_namespace(namespaces, 'global', 'b')
namespaces = add_var_to_namespace(namespaces, 'foo', 'c')
print(namespaces)


    
