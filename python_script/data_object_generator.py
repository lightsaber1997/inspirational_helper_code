
from unittest import result

def get_data_object_fields_as_list(list_line):
    result = []

    for line in list_line:
        temp = []
        # delete white space in left or right
        line = line.strip()
        list = line.split(" ")
        field_name = list[0]
        field_type = list[1]
        
        temp.append(field_name)
        
        field_type_in_java = "error"

        if field_type == "int":
            field_type_in_java = "int"
        elif field_type == "timestamp":
            field_type_in_java = "Date"
        else:
            field_type_in_java = "String"
        
        temp.append(field_type_in_java)
        result.append(temp)
    return result

def create_data_object_fields(list_line):
    result = ""
    for line in list_line:
        list = line.split(" ")
        field_name = list[0]
        field_type = list[1]
        buffer = "private "

        if field_type == "int":
            buffer += "int"
        elif field_type == "timestamp":
            buffer += "Date"
        else:
            buffer += "String"
        buffer += " " + field_name + ";\n"
        result += buffer
    return result


def generate_data_object(list_line):
    result = ""
    indentation = ""
    four_space = "    "

    list_field = get_data_object_fields_as_list(list_line)

    # add imports
    import_date = False
    for field in list_field:
        name = field[0]
        type = field[1]
        if type == "Date":
            import_date = True
            break
    if import_date:
        result += "import java.util.Date;\n"
    
    result += "\n"

    result += "public class className {\n"
    indentation += four_space
    
    
    for field in list_field:
        name = field[0]
        type = field[1]

        temp = f"{indentation}private {type} {name};\n"
        result += temp
    result += "\n"

    for field in list_field:
        name = field[0]
        type = field[1]

        # add getter
        temp = f"{indentation}public {type} get{name[0].upper() + name[1:]}() {{\n"
        indentation += four_space
        temp += indentation + f"return {name};\n"
        indentation = indentation[0:-len(four_space)]
        temp += indentation + "}\n"
        result += temp

        # add setter
        temp = f"{indentation}public void set{name[0].upper() + name[1:]}({type} {name}) {{\n"
        indentation += four_space
        temp += indentation + f"this.{name} = {name};\n"
        indentation = indentation[0:-len(four_space)]
        temp += indentation + "}\n"
        result += temp
    result += "}"
    return result


# text = input("input: ")
f = open("input.txt", 'r')
list_line = f.readlines()

f.close()
# print(create_dao_fields(list_line))

print(get_data_object_fields_as_list(list_line))
print(generate_data_object(list_line))