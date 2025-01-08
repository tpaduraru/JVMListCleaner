import io

class JVMList:
    input_file_path = ''
    output_file_path = ''
    fields =[]
    field_dict = {}
    dropdown_options = []
    read_rows = 0
    successful_rows = 0
    error_rows = 0
    overwrite_input_file = False