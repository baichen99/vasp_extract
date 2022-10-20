import xml.etree.ElementTree as ET
from xml.dom import minidom
import pickle


xml = minidom.Document()


def create_str_node(name, value):
    node = xml.createElement(name)
    node.appendChild(xml.createTextNode(str(value)))
    return node


def create_value_with_unit_node(name, value, unit):
    node = xml.createElement(name)
    _vwu = xml.createElement("_vwu")
    _value = xml.createElement('_value')
    _unit = xml.createElement('_unit')
    _vwu.appendChild(_value)
    _vwu.appendChild(_unit)
    _value.appendChild(xml.createTextNode(value))
    _unit.appendChild(xml.createTextNode(unit))
    node.appendChild(_vwu)
    return node


def create_file_list_node(name, filenames, paths):

    node = xml.createElement(name)
    if len(filenames) == 0:
        _file = xml.createElement("_file")
        _file.setAttribute("array", "true")
        _name = xml.createElement("_name")
        _url = xml.createElement("_url")

        _file.appendChild(_name)
        _file.appendChild(_url)
        node.appendChild(_file)
        return node
    for filename, path in zip(filenames, paths):
        _file = xml.createElement("_file")
        _file.setAttribute("array", "true")
        _name = xml.createElement("_name")
        _url = xml.createElement("_url")

        _name.appendChild(xml.createTextNode(filename))
        _url.appendChild(xml.createTextNode('import:' + path))
        _file.appendChild(_name)
        _file.appendChild(_url)
        node.appendChild(_file)
    return node


def create_table_node(name, columns, units, data: list[list], headless=False):
    """_summary_

    Args:
        name: element name
        columns: 列名
        units: 每列的单位
        data: 表数据, 是2d list
        headless: 是否显示列名
    """
    if type(data) != list:
        raise Exception('node type error')
    node = xml.createElement(name)
    if headless:
        node.setAttribute("headless", "true")
    for record in data:
        record_node = xml.createElement(tagName=f"{name}-_record")
        record_node.setAttribute("array", "true")
        for i, col_name in enumerate(columns):
            value = record[i] if i < len(record) else ''
            if units[i] != "":
                record_node.appendChild(
                    create_value_with_unit_node(col_name, value, units[i]))
            else:
                record_node.appendChild(create_str_node(col_name, value))
        node.appendChild(record_node)
    return node


def create_empty_node(name):
    node = xml.createElement(name)
    return node


def save_to_xml(dom, save_path):
    with open(save_path, 'w', encoding='utf-8') as f:
        dom.writexml(f)
