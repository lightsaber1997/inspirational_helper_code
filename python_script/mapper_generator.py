import xml.etree.ElementTree as ET

def get_parameter_names_from_a_method(code):
    result = []
    param_annot = "@Param("
    
    while True:
        index = code.find(param_annot)
        if index < 0:
            break
        code = code[index+len(param_annot):]
        index1 = code.find("\"")
        index2 = code.find("\"", index1+1)
        param_name = code[index1+1:index2]
       
        result.append(param_name)
    return result


def create_xml_object(list_method, path_to_dao, path_to_data_object, table_name):
    xml_data = ET.Element("mapper")
    xml_data.set("namespace", path_to_dao)
    for method in list_method:
        return_type = method[0]
        method_name = method[1]
        parameter_names = method[2]
        try:
            if "select" == method_name[:len("select")]:
                element1 = ET.SubElement(xml_data, "select")
                element1.set("id", method_name)
                element1.set("resultType", path_to_data_object)
                if len(parameter_names) == 0:
                    element1.text = f"\nselect\n\t*\nfrom\n\t`{table_name}`\n"
                else:
                    after_where = ""
                    for i in range(len(parameter_names)):
                        parameter_name = parameter_names[i]
                        after_where += f"{parameter_name} = #{{{parameter_name}}}"
                        
                        if i < (len(parameter_names) - 1):
                            after_where += " and\n"
                    element1.text =  f"\nselect\n\t*\nfrom\n\t`{table_name}`\nwhere\n{after_where}\n"
        except:
            pass

        try:
            if method_name.find("insert") == 0:
                element1 = ET.SubElement(xml_data, "insert")
                element1.set("id", method_name)
                part1 = f"\ninsert into\n\t`{table_name}`\n"
                part2 = "\t("
                for i in range(len(parameter_names)):
                    parameter_name = parameter_names[i]
                    part2 += f"{parameter_name}"
                    
                    if i < (len(parameter_names) - 1):
                        part2 += ", "
                part2 += ")\n"
                part3 = "values\n"
                part4 = "\t("
                for i in range(len(parameter_names)):
                    parameter_name = parameter_names[i]
                    part4 += f"#{{{parameter_name}}}"
                    
                    if i < (len(parameter_names) - 1):
                        part4 += ", "
                part4 += ")\n"
                element1.text = f"{part1}{part2}{part3}{part4}"
        except:
            pass

        try:
            if method_name.find("delete") == 0:
                element1 = ET.SubElement(xml_data, "delete")
                element1.set("id", method_name)
                after_where = ""
                for i in range(len(parameter_names)):
                    parameter_name = parameter_names[i]
                    after_where += f"{parameter_name} = #{{{parameter_name}}}"
                    
                    if i < (len(parameter_names) - 1):
                        after_where += " and\n"
                element1.text =  f"\ndelete from\n\t`{table_name}`\nwhere\n{after_where}\n"
        except:
            pass
    return xml_data



def dao_to_mapper(java_code_file_name, table_name=""):
    java_code = ""
    with open(java_code_file_name) as f:
        java_code = f.read()
    # change all whitespace to a single space
    java_code = ' '.join(java_code.split())
    original_code = java_code
    # find the package name that includes the java code
    index_package = java_code.find("package")
    index_semicolon = java_code.find(";", index_package)
    string_including_package_name = java_code[index_package:index_semicolon]
    string_including_package_name = string_including_package_name.strip()
    package_name = string_including_package_name.split()[1]
    
    # find interface name
    index_interface = java_code.find("interface")
    index_semicolon = java_code.find(";", index_interface)
    string_containing_interface_name = java_code[index_interface: index_semicolon]
    string_containing_interface_name = string_containing_interface_name.strip()

    interface_name = string_containing_interface_name.split()[1]

    java_code = java_code[java_code.find("{")+1:]

    list_method = []
    while True:
        # read each method
        index = java_code.find(";")

        if index < 0:
            break
        
        list_for_a_method = []

        java_method_code = java_code[0:index]
        java_method_code = java_method_code.strip()
        index_of_parenthesis = java_method_code.find("(")
        java_method_code_before_parenthesis = java_method_code[:index_of_parenthesis]
        return_type = java_method_code_before_parenthesis.split()[1]
        method_name = java_method_code_before_parenthesis.split()[2]
        list_java_method_code = [return_type, method_name]
        parameter_names = get_parameter_names_from_a_method(java_method_code)
        list_java_method_code.append(parameter_names)
        list_method.append(list_java_method_code)

        java_code = java_code[index+1:]
    # find data transfer object name
    data_transfer_object_name = ""
    for method in list_method:
        return_type = method[0]
        method_name = method[1]
        if method_name.find("select") == 0:
            if return_type.find("<") >= 0:
                index1 = return_type.find("<")
                index2 = return_type.find(">")
                data_transfer_object_name = return_type[index1:index2]
            else:
                data_transfer_object_name = return_type

    # find path to the data transfer object
    path_data_object = f"{package_name}.{data_transfer_object_name}"
    java_code = original_code
    while True:
        index1 = java_code.find("import")
        if index1 < 0:
            break    
        index2 = java_code.find(";", index1)
        import_line = java_code[index1:index2]
        import_line = import_line.strip()
        path = import_line.split()[1]
        class_name = path.split(".")[-1]

        if class_name == data_transfer_object_name:
            path_data_object = path

        java_code = java_code[index2:]
    
    # guess table name if the user did not provide it
    if len(table_name) == 0:
        table_name = data_transfer_object_name
    
    xml_data = create_xml_object(list_method, f"{package_name}.{interface_name}", path_data_object, table_name)
    xml_data_binary = ET.tostring(xml_data)
    with open("mapper.xml", "wb") as f:
        f.write('<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" \n"http://mybatis.org/dtd/mybatis-3-mapper.dtd">'.encode('utf8'))
        f.write(xml_data_binary)

dao_to_mapper("User.java")