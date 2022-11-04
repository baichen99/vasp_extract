def atomic_position_callback(s, **kwargs):
    rows = s.split('\n')
    elements = rows[5].strip().split()
    nums = [int(num) for num in rows[6].strip().split()]
    eles = []
    for (element, num) in zip(elements, nums):
        eles += [element]*num
    pos = [ [eles[i]] + row.strip().split() for i, row in enumerate(rows[8:len(eles)+1])]
    # print(pos)
    return pos

def optimized_unit_cell_parameters_callback(res_list, **kwargs):
    # 如果匹配成功res_list应该是下面这样，需要转成一个3x3的list
    # ['8.17620077       0.00000000      -0.00000000',
    # '-0.00000000       8.65476744       0.00000000',
    # '-0.00000000       0.00000000       8.65476744']
    if not res_list:
        return []
    res_list = [e.text for e in res_list[-1]]
    data = []
    for row in res_list:
        data.append(row.split())
    return data

def lattice_parameters_callback(res_list, **kwargs):
    if not res_list:
        return []
    res_list = [e.text for e in res_list[-1]]
    data = []
    for row in res_list:
        data.append(row.split())
    return data

def K_Point_list_callback(res_list, **kwargs):
    if not res_list:
        return []
    res_list = [e.text for e in res_list[-1]]
    data = []
    for row in res_list:
        data.append(row.split())
    return data
