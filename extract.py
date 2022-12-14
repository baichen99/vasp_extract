from utils.xpath import extract_xpath_from_file
from utils.createNodes import *
import shutil
import os
import ipdb
import re

def create_dom_with_config(config_dict: dict, output_path: str):
    """
    Params:
        output_path: 应该是一个folder, 不是文件
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    def traverse(dict_node: dict):
        if not dict_node:
            return
        
        name = dict_node.get('tag_name')
        node_type = dict_node['type']
        
        if name == 'calculating_time':
            a = 1
            pass
        
        if node_type == 'container':
            node = create_empty_node(name)
            for child in dict_node['children']:
                child_element = traverse(child)
                if child_element:
                    node.appendChild(child_element)
            return node
        
        path = dict_node.get('path')
        xpath = dict_node.get('xpath')
        regex = dict_node.get('regex')
        default_value = dict_node.get('default')
        callback = dict_node.get('callback')
        kwargs = dict_node.get('kwargs', {})
        
        data = None
        
        if xpath and path:
            data = extract_xpath_from_file(xpath, path)
            if callback:
                data = callback(data, **kwargs)
            elif len(data) == 1:
                data = data[0].text
            else:
                data = [d.text for d in data]
        elif regex and path:
            with open(path, 'r', encoding='UTF-8') as f:
                s = f.read()
            # pattern = re.compile(regex)
            # data = pattern.findall(s)
            if callback:
                data = callback(s, **kwargs)
                
        data = data or default_value or ''
        
        if node_type == 'uncheck-stringtype':
            return create_str_node(name, data)
        
        elif node_type == 'table':
            # table 的 data 要特殊处理
            if data:
                table_node = create_table_node(name, data=data, **kwargs)
            else:
                table_node = create_table_node(name, data=[], **kwargs)
            return table_node
        
        elif node_type == 'value-with-unit':
            return create_value_with_unit_node(name, data, unit=kwargs.get('unit', ''))

        elif node_type == 'uncheck-numbertype':
            return create_str_node(name, data)

        elif node_type == 'file-list':
            filenames = kwargs.get('filenames', [])
            paths = kwargs.get('paths', [])
            new_paths = []
            if paths:
                for path in paths:
                    fname = os.path.split(path)[-1]
                    shutil.copy(path, os.path.join(output_path, fname))
                    new_paths.append(fname)
            return create_file_list_node(name, filenames, new_paths)
        elif not data:
            create_empty_node(name)
    dom = traverse(config_dict)
    save_to_xml(dom, os.path.join(output_path, 'data.xml'))