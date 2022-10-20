from config import build_config
from extract import create_dom_with_config

cfg = build_config('vasprun.xml')

create_dom_with_config(cfg, 'outputs/1')