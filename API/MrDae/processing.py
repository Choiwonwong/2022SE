from MrDaeApi.settings import SECRET_KEY
import jwt

def getUserID(cookies):
    access = cookies.get('access_token')
    payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
    return payload.get('user_id')

def getUserInfo(request, userinfo):

    address = request.get('address', userinfo.get('address'))
    name = request.get('name', userinfo.get('name'))
    phone_number = request.get('phone_number', userinfo.get('phone_number')) 
    User_Info = {'address':address, 'name':name, 'phone_number':phone_number}
    return User_Info