class FileUtils():

    def read_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"The file {file_path} does not exist.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None
    def remove_blank(text):
        newText = text.replace('\n','')
        return newText