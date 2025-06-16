## Get Started

1. Clone this repository. <br>

2. Navigate this repository. <br>

```bash
cd Python_Practice
```

## Setup with uv (New package and project manager for Python)


First, why uv? when you run a single python script and you need only specific packages are need to run this script not all of your scripts need those modules or packages. Then, uv here to save your time and package management. It also helpful in project management. Comparatively, it is way faster than pip command. A great feature of uv is that, it not requires virtual environment for script files. Moreover, it automatically creates virtualenv for your python project.

```bash
pip3 install uv
```

windows:

```powershell
pip install uv
```

For newer file which not include those lines:

```ini
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests", "pandas", "bs4", "prettytable"]
# ///
```

```bash
uv  init --script filename --python < your installed python version >
```

This will some comment top of your file.

```ini
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
```

Now you can add package name in dependencies list or run command like this:

```bash
uv add --script filename "package_name"
```

Also, you can directly type package name in dependencies list. The uv read those lines before he execute the python script and install those packages for you.


### More of uv:

You can use different python version of for your own needs:

1. Listing available python version

```bash
uv python list
```

2. Install different python version:

```bash
uv python install < version_number >
```


## Old Way

<p> If your using pip for managing the packages so you can use this methods:
</p>
<b> Setup Python Virtual Environment (Linux)</b>

```bash
sudo apt install python3-virtualenv
```

<b> Create Virtual Environment </b>

```bash
virtualenv -p /usr/bin/python3 env
```
<b> Activate virtual environment </b>

```bash
source env/bin/activate
```
for deactivation

```bash
deactivate
```

<b> Install required Libraries </b>

```bash
pip3 install -r requirement.txt
```

<b> Setup Python Virtual Environment (Windows)</b>


<b> Create Virtual Environment </b>

```bash
python -m venv env
```
<b> Activate virtual environment </b>

```bash
.\env\Scripts\activate
```
for deactivation

```bash
deactivate
```
### Windows

1. Create virual env:

```powershell
python -m venv env
```

2. Activate

```powershell
env\Scripts\activate
```

3. deactivate

```powershell
deactivate
```

<b> Install required Libraries </b>

```bash
pip install -r requirement.txt
```


# Ref:

1. <a href="https://docs.astral.sh/uv/"> UV Docs </a>.

2. <a href="https://github.com/astral-sh/uv">UV GitHub</a>.