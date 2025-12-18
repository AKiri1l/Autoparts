import requests

url = 'http://msi-http.at.remote.it:33000/login/'
response = requests.get(url)

print("Cookies:", response.cookies)
print("CSRF Token in cookies:", response.cookies.get('csrftoken'))

if 'csrfmiddlewaretoken' in response.text:
    print("CSRF token found in HTML form")
else:
    print("ERROR: CSRF token NOT found in HTML form")