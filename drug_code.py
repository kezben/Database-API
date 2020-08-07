import requests

codes = ['369844bf', '64d064bf', '32d064bf', '372ce4bf', 'bbfcf518']

for i in codes:
    request = requests.get('https://api.universalcodes.msupply.org.nz/v1/items?code='+i)
    code, name = request.text.split(',', 1)
    code = code.split(':')[1].strip('"')
    name = name.split(':')[1].strip('"}]')
    if "NotFound" in name:
        print("Error: Drug name not found.\n")
    else:
        print("Drug name: ", name, "\nCode:", code, "\n")
