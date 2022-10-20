import json
import sys


# 将template.json转换成简洁的层级关系，方便作为配置文件config进行编辑


def template_to_dict(template_path: str, return_json=False) -> dict or str:
    with open(template_path, 'r', encoding='utf-8') as f:
        json_obj = json.load(f)

    def traverse(node):
        node_type = node.get('type')
        node_name = node.get('name')
        zh_name = node.get("zhCN")
        if not node_type:
            return
        if node_type == 'container':
            children = []
            for child_node in node.get('children'):
                children.append(traverse(child_node))
            return {
                "zh-name": zh_name,
                "tag_name": node_name,
                "type": node_type,
                "children": children
            }
        elif node_type in ['uncheck-stringtype', 'uncheck-numbertype']:
            return {
                "zh-name": zh_name,
                "tag_name": node_name,
                "type": node_type,
                "default": "",
                "path": "",
                "xpath": "",
                "callback": "",
                "kwargs": {}
            }
        elif node_type == 'table':
            return {
                "zh-name": zh_name,
                "tag_name": node_name,
                "type": node_type,
                "default": "",
                "path": "",
                "xpath": "",
                "callback": "",
                "kwargs": {
                    "columns": [child['name'] for child in node.get('children')],
                    "units": [child['children'][1]['fixed'] if child.get('type') == 'value-with-unit' else '' for child in node.get('children')],
                }
            }
        elif node_type == 'value-with-unit':
            unit = node.get("children")[1]['fixed']
            return {
                "zh-name": zh_name,
                "tag_name": node_name,
                "type": node_type,
                "default": "",
                "path": "",
                "xpath": "",
                "callback": "",
                "kwargs": {
                    "unit": unit
                }
            }
        elif node_type == 'file-list':
            return {
                "zh-name": zh_name,
                "tag_name": node_name,
                "type": node_type,
                'default': '',
                'path': '',
                'xpath': '',
                'callback': '',
                'kwargs': {
                    "filenames": [],
                    "paths": []
                }
            }
    config_dict = traverse(json_obj)
    if return_json:
        return json.dumps(config_dict, ensure_ascii=False, indent=4)
    return config_dict


if __name__ == '__main__':
    r = template_to_dict(template_path='template.json', return_json=False)
    json_str = json.dumps(r, ensure_ascii=False)
    with open('config.json', 'w', encoding='utf-8') as f:
        f.write(json_str)
