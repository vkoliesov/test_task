def slice_less(my_list, lesser):
    new_list = None
    new_list = []
    for i in my_list:
        if i > lesser:
            new_list.append(i)
            
    else:
        sorted(new_list, reverse=True)
        print(new_list)
