def order_managers(managers):
    list_managers=[]
    dict_managers={}
    for i in range(len(managers)):
        dict_managers ={
            'name':managers[i][0],
            'cpf':managers[i][1],
            'salary':managers[i][2],
            'unit':managers[i][3]
        }
        list_managers.append(dict_managers)
    return list_managers