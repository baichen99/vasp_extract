from extract import extract_xpath_from_file

xpath = ".//generator/i[@name='date']"
filename = 'vasprun.xml'

print(extract_xpath_from_file(xpath, filename))