#!C:\Python311\python.exe
print ("Content-type: text/html\r\n\r\n")

import cgi

# Read form data
form = cgi.FieldStorage()
username = form.getvalue('username')
password = form.getvalue('password')

# Check authentication

if username == 'logeshwaran' and password == 'Logesh1997':
    authenticated = True
    print('<h2>Authentication Success</h2>')
else:
    authenticated = False
    print('<h2>Authentication Failed</h2>')
# Generate authentication code
if authenticated:
    authentication_code = '007'  # Replace with your desired code
else:
    authentication_code = 'Invalid credentials'

# Generate HTML response
print('Content-Type: text/html\r\n\r\n')
print('')
print('<html>')
print('<head>')
print('  <title>Authentication Result</title>')
print('</head>')
print('<body>')
print("<h2>")
print("<style>")
print('''body {background-image: url('image2.jpg');
          background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;

}''')
print("</style>")
print('''<h1>
    <p style="text-align:center;">''')
print('  <h2>Authentication Result</h2>')
print('  <p>Authentication Code: ' + authentication_code + '</p>')
print("</h1>")
print("</p>")
print("</h2>")
int("<br>")
print("<br>")
print("<form action='submit.py'>")
print("<input type='submit' value='next'>")
print("</form>")
print('</body>')
print('</html>')

  




      
