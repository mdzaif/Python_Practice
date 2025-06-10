# /// script
# requires-python = ">=3.12"
# dependencies = ["nbformat", "nbconvert", "requests", "pdfkit"]
# ///

#!/usr/bin/ python3

# more task to do: more error handling needed.
# Only for google colab

# Additional package: sudo apt install wkhtmltopdf # linux
# on windows: winget install wkhtmltopdf.wkhtmltox
# edit environment variable: mostly the path is: 'C:\Program Files\wkhtmltopdf\bin\'

import nbformat
from nbconvert import HTMLExporter
import requests
import pdfkit
import sys
import platform
from pathlib import Path

def check_sys_path():

    if platform.system() == "Windows":
        return r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe" # It is good practice check your system has same path
    else:
        return "/usr/bin/wkhtmltopdf"

def basename(f):
    return Path(f).stem

print("Download the .ipynb file from google colab")
print("Collect the file id by check the browser link: https://colab.research.google.com/drive/<file_id>")
print("Make sure your notebook has public with editor option")
file_id = input("Please only type the notebook file id: ").strip()
url = f"https://drive.google.com/uc?export=download&id={file_id}"
file = input("Enter the file name: ")
try:
    r = requests.get(url)
    r.raise_for_status()
    with open(file, 'wb') as fl:
        fl.write(r.content)
    print("File downloaded successfully.")
    
except requests.exceptions.RequestException as e:
    print(f"An error occurred while downloading the file: {e}")
    sys.exit(1)
    
except IOError as e:
    print(f"An error occurred while saving the file: {e}")
    sys.exit(2)

with open(file) as f:
    nb_con = nbformat.read(f, as_version=4)

htmlexp = HTMLExporter()

(body, resources) = htmlexp.from_notebook_node(nb_con)

html_path = basename(file) + '.html'
with open(html_path, 'w') as f:
    f.write(body)

pdf_path = basename(html_path) + '.pdf'

#path_wkhtmltopdf = '/usr/bin/wkhtmltopdf'  # For Linux/macOS

path_wkhtmltopdf = check_sys_path()

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_file(html_path, pdf_path, configuration=config)

print("Done")
