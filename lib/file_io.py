def write_file(file_name, file_content):
     with open(f"{file_name}.txt", 'w') as file:
        file.write(file_content)
        pass

def append_file(file_name, append_content):
   with open(f"{file_name}.txt", 'r')as file:
    file.write(append_content)
    pass

def read_file(file_name):
    pass
