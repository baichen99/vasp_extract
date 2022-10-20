import xml.etree.ElementTree as ET

def extract_xpath_from_file(xpath, filename):
    try:
        tree = ET.parse(filename).getroot()
    except Exception as e:
        raise Exception('解析xml出错', e)
    
    results = tree.findall(xpath)
    if len(results) == 1:
        return results[0].text
    return [res.text for res in results]
    