import base64
import jwt
import datetime

with open('baby.jpg', 'rb') as f:
    base = base64.b64encode(f.read())

img = base64.b64decode(base)
with open('temp.jpg', 'wb') as ff:
    ff.write(img)

# data = {"user_id": 1, "openid": "123456",  "loginTime": str(datetime.datetime.now())}
# secret = 'Camera~348#fgEHz24$9deHPfL'
# print(jwt.encode(data, secret, algorithm="HS256").decode())