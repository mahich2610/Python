import xml.dom.minidom as minidom


FILE_NAME = 'currency.xml'
CLASS_NAME = 'Valute'
OBJECT_NAME = 'Name'
OBJECT_VALUE = 'Value'


def read_valute_course(file, class_name, obj_name, obj_value):
    xml_data = file.read()
    dom = minidom.parseString(xml_data)
    dom.normalize()
    
    elements = dom.getElementsByTagName(class_name)

    Name, Value = [], []
    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == obj_name:
                    if child.firstChild.nodeType == 3: #проверка типа узла на текст
                        Name.append(child.firstChild.data)
                if child.tagName == obj_value:
                    if child.firstChild.nodeType == 3:
                        Value.append(float(child.firstChild.data.replace(',', '.')))
    return Name, Value


if __name__ == '__main__':
    xml_file = open(FILE_NAME, 'r', encoding='windows-1251')
    Name, Value = read_valute_course(xml_file, CLASS_NAME, OBJECT_NAME, OBJECT_VALUE)
    print(Name)
    print(Value)
    
                
