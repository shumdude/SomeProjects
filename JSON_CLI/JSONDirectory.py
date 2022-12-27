import os, json, mimetypes, click


class JSONCreator:
    def __init__(self):
        self.data = {}

    def recursion_function(self, some_dir: str, go_inside=None) -> None:  # это именно функция **рекурсии**
        if go_inside is None:
            go_inside = self.data

        walk = os.walk(some_dir)  # генератор древа каталогов и прочего
        folder_name = os.path.basename(some_dir)  # имя папки, в которой находимся
        go_inside[folder_name] = {}  # создаём в части data эл-т, где ключ - папка в которой находимся
        go_inside = go_inside[folder_name]  # go_inside - это внутренняя часть словаря, в которым находимся

        self.logic_method(walk, go_inside)
        # может вынести в отдельный класс логику ...
        # for dir_path, dir_names, file_names in walk:
        #     for file_name in filter(self.is_binary_or_text, file_names):  # отсеиваем неподходящих типов файлы
        #         file_path = os.path.join(dir_path, file_name)
        #         # file_mimetype = mimetypes.guess_type(file_path)[0]
        #         go_inside[file_name] = {
        #             "type_file": self.type_file(file_path),
        #             "size": self.size_file(file_path)
        #         }
        #     for dir_name in dir_names:
        #         new_path = os.path.join(dir_path, dir_name)
        #         self.recursion_function(new_path, go_inside)
        #     break

    def create_json_element(self):
        pass

    def logic_method(self, generator, go_inside):
        for dir_path, dir_names, file_names in generator:
            # создание эл-та в json файле
            for file_name in filter(self.is_binary_or_text, file_names):  # отсеиваем неподходящих типов файлы
                file_path = os.path.join(dir_path, file_name)
                go_inside[file_name] = {
                    "type_file": self.type_file(file_path),
                    "size": self.size_file(file_path)
                }
            for dir_name in dir_names:
                new_path = os.path.join(dir_path, dir_name)
                self.recursion_function(new_path, go_inside)
            break

    @staticmethod
    def is_binary_or_text(file_name):
        match mimetypes.guess_type(file_name)[0]:
            case "application/octet-stream" | "text/plain":
                return True
            case _:
                return False

    @staticmethod
    def size_file(path_to_file):
        postfix, size_file = None, None
        match mimetypes.guess_type(path_to_file)[0]:
            case "application/octet-stream":
                postfix = " bites"
                size_file = str(os.path.getsize(path_to_file))
            case "text/plain":
                postfix = " lines"
                size_file = str(sum(1 for line in open(path_to_file)))
            case _:
                print('ERROR')
        return size_file + postfix

    @staticmethod
    def type_file(path_to_file):
        type_file = None
        match mimetypes.guess_type(path_to_file)[0]:
            case "application/octet-stream":
                type_file = "binary"
            case "text/plain":
                type_file = "text"
            case _:
                print('ERROR')
        return type_file


class CLIWork:

    @staticmethod
    @click.command()
    @click.option('--input_path', prompt='Please, enter the PATH')
    def run_cli_application(input_path):
        jc = JSONCreator()
        jc.recursion_function(input_path)
        json_string = json.dumps(jc.data, indent=4)
        click.echo(f"{json_string}")


# jc = JSONCreator()
# jc.run_cli_application()
# cl = CLIWork()
# cl.run_cli_application()


jc = JSONCreator()
jc.recursion_function("C:\\Test")
json_string = json.dumps(jc.data, indent=4)
print(json_string)
# with open("data.json", "w") as w:
#     json.dump(jc.data, w, indent=4)


# @click.command()
# @click.option('--input_path', prompt='Please, enter the PATH')
# def start_CLI(input_path):
#     jc = JSONCreator()
#     jc.recursion_function(input_path)
#     json_string = json.dumps(jc.data, indent=4)
#     click.echo(f"{json_string}")
# start_CLI()
