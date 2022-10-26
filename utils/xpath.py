import xml.etree.ElementTree as ET

def extract_xpath_from_file(xpath, filename):
    try:
        tree = ET.parse(filename).getroot()
    except Exception as e:
        raise Exception('解析xml出错', e)
    
    results = tree.findall(xpath)

    return results
    