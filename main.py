import os
from glob import glob
from tqdm import tqdm
from config import build_config
from extract import create_dom_with_config

xml_folder = 'xmls'
output_folder = 'outputs'
idx = 1
for file in glob(os.path.join(xml_folder, '*.xml')):
    cfg = build_config(file)
    create_dom_with_config(cfg, os.path.join(xml_folder, f'{idx}'))
    idx += 1