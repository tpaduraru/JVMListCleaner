import io

class JVMList:
    input_file = io.StringIO()
    output_file = io.StringIO()
    input_file_path = ''
    output_file_path = ''
    fields =[]
    field_dict = {}
    dropdown_options = []
    read_rows = 0
    successful_rows = 0
    error_rows = 0