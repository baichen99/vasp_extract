import os
from glob import glob
from tqdm import tqdm
from config import build_config
from extract import create_dom_with_config
from template_tools.src.upload import upload_zip

def parse_keyword(xml_path, sep=" "):
    keywords = [element.text for element in ET.parse(xml_path).findall(
        './/atomic_position-_record/element') if element.text]
    return sep.join(list(set(keywords)))

xml_folder = '/home/baichen/vasp_raw_xmls'
output_folder = 'outputs'
files_count = len(os.listdir(xml_folder))

start = 0
step = files_count

for idx in tqdm(range(start, start+step)):
    file = os.path.join(xml_folder, f'/{idx}/vasprun.xml')
    fsize = os.path.getsize(file)
    if not os.path.exists(file) or fsize > 50 * 1024 * 1024:
        continue
    try:
        cfg = build_config(file)
        create_dom_with_config(cfg, os.path.join(output_folder, f'{idx}'))
        keyword = parse_keyword(file)
        upload_zip(os.path.join(output_folder, f'{idx}'), f'第一性原理计算数据vasp_{keyword}_{idx}',  '第一性原理计算数据', '第一性原理计算数据')
    except Exception as e:
        print(e)
        continue
    # upload
    finally:
        idx += 1