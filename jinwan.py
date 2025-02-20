
result_list = []
tree_dict = {}

for item in result_tree:
    tree_dict[item['id']] = item

    if item['parent'] is None : 
        result_list.append(item)
    elst :
        parent = tree_dict[item['parent']]
        if 'children' not in parent : parent['children'] = []
        parent['children'].append(item)

    