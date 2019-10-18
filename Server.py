from flask import Flask, request
from os import listdir, getcwd
from os.path import isdir, isfile, abspath
import jinja2 as jin
import json


root_folder = getcwd() + "/"
app = Flask(__name__, root_path=root_folder)


def generate_html(html_template_path: str, input_values: dict):
    html_temp = read_file(html_template_path)
    jin_temp = jin.Template(html_temp)
    html_rend = jin_temp.render(input_values)
    return html_rend


def read_file(file_path: str):
    with open(file_path, "r") as file:
        return "".join(file.readlines())


@app.route("/", methods=['GET'])
def folder_info(path=""):
    path = root_folder if path == "" else abspath(path) + "/"
    curr_dir_list = listdir(path)
    dir_list = list(filter(lambda f: isdir(path + f), curr_dir_list))
    files_list = list(filter(lambda f: isfile(path + f), curr_dir_list))
    dir_info = {"directory": path,
                "dir_list": dir_list,
                "files_list": files_list}
    return generate_html("static/WebModules/folder_page.html", dir_info)


@app.route("/folder_search", methods=["GET", "POST"])
def get_folder_info():
    folder_path = json.loads(request.data.decode("utf-8"))["folder_path"]
    return folder_info(folder_path)


@app.route("/file_content", methods=["GET", "POST"])
def get_file_content():
    file_path = json.loads(request.data.decode("utf-8"))["file_path"]
    return read_file(file_path)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
