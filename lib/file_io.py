def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w') as f:
        f.write(file_content)

    '''with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    assert file_content_read == file_content'''

    print(f"File '{file_name}.txt' created successfully.")

    f.close()

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a') as f:
        f.write(append_content)
        print(f"Appended content to '{file_name}.txt' successfully.")
        f.close()
    

def read_file(file_name):
    with open(f'{file_name}.txt', 'r') as f:
        file_content_read = f.read()
    return file_content_read

# Example usage:
# write_file("test_file", "This is a test content.")

    

