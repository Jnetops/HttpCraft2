

class cookie(object):
    def getCookies(cookies):
        # this grabs first portion of cookie before = and all portions after, adds to dict
        # when parsed by requests it rebuilds with key + = + value
        request_cookie = cookies
        cookieDict = {}

        if (request_cookie != ""):
            cookieEqualSplit = request_cookie.split("=", 1)
            cookieDict[cookieEqualSplit[0]] = cookieEqualSplit[1]
        return cookieDict