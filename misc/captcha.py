import requests 
import pytesseract
from io import BytesIO
from PIL import Image

def solve(req):
    t = req.text
    s = t.find("/images")
    e = t.find("alt=")-2

    img_url = url+t[s:e]    
    bin_img = sess.get(img_url).content
    numeri = get_numbers(bin_img).strip()

    risposta = { 'risposta' : numeri }
    res = sess.post(url+"/next", data=risposta)
    
    print(res.text)
    return res

def get_numbers(bin_img):
    img = Image.open(BytesIO(bin_img))
    t = pytesseract.image_to_string(img)

    return t

if __name__ == '__main__':
    sess = requests.session()
    url = "http://captcha.challs.olicyber.it/"
    req = sess.get(url)

    for i in range(110):
        req = solve(req)