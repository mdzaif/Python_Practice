import pdftables_api

conv = pdftables_api.Client('API_KEY')

pdf_file = input("Enter file path: ").strip()
csv_file = input("Enter file path to save: ").strip()

conv.csv(pdf_file, csv_file)

'''
1. install module: pip install git+https://github.com/pdftables/python-pdftables-api.git

2. After Installation, you need an API KEY.

3. Go to https://pdftables.com/ and signup, then visit the API Page to see your API KEY.

'''