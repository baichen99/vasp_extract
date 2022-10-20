

def optimized_unit_cell_parameters_callback(res_list, **kwargs):
    # 如果匹配成功res_list应该是下面这样，需要转成一个3x3的list
    # ['8.17620077       0.00000000      -0.00000000',
    # '-0.00000000       8.65476744       0.00000000',
    # '-0.00000000       0.00000000       8.65476744']
    if not res_list:
        return []
    data = []
    for row in res_list:
        data.append(row.split())
    return data