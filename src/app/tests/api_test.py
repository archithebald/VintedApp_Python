from utils import cookies
from api import search

auth = cookies.load_auth_cookie()

c = {
    auth[0]: auth[1]
}

search(cookies=c, page=1)