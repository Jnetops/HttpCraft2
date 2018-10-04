import json

class bodyParse(object):
    def getBody(body):
        # start body detection
        request_body = body
        if (request_body != ""):
            try:
                json_body = {"type": "normal", "data": request_body}
                return json_body
            except:
                return {"type": "normal", "data": request_body}
        else:
            # return empty body, requests ignores this when supplied
            return request_body

    # handy recursive method to dig into nested json. find/replace value
    def jsonReplace(jsonVar, k, v):
        for key in jsonVar.keys():
            if key == k:
                jsonVar[key] = v
            elif type(jsonVar[key]) is dict:
                bodyParse.jsonReplace(jsonVar[key], k, v)
            elif type(jsonVar[key]) is list:
                for d in jsonVar[key]:
                    bodyParse.jsonReplace(d, k, v)
            else:
                # not something iterable, pass over it, str int float etc, more than likely a list of strings or similar
                continue
        return jsonVar

    def bodyIter(request_custom_dict, request_body, request_type, custom_iter):
        # check if json or not
        bodyVar = request_custom_dict["body"]
        if (request_type["body"] == "json"):
            # mess with body as json
            iter_request_body = bodyParse.jsonReplace(request_body, bodyVar, custom_iter)
        elif (request_type["body"] == "plain"):
            bodyVar = request_body.split(str(request_custom_dict["body"]))
            iter_request_body = ""
            count = 1
            for val in bodyVar:
                if (val != ""):
                    if count < len(bodyVar):
                        iter_request_body = iter_request_body + val + str(custom_iter)
                    else:
                        iter_request_body = iter_request_body + val
                    count = count + 1
        return iter_request_body  