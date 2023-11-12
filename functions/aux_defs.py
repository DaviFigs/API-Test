

def filter_search(query_list, position):
    if position == 1:
        job = 'unit'
    elif position == 2:
        job = 'function'
    elif position == 3:
        job = 'sector'
    employes_list=[]
    dictionary_employes={}
    for i in range(len(query_list)):
        dictionary_employes ={
            'name':query_list[i][0],
            'cpf':query_list[i][1],
            'salary':query_list[i][2],
            f'{job}':query_list[i][3]
        }
        employes_list.append(dictionary_employes)

    return employes_list

