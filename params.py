
class paramVerify(object):

    def verify(request_custom_dict, current_val):
        '''
            {
                "url": "variableName",
                "body": "variabelName",
                "start": 100,
                "stop": 200,
                "stepping": 2
            }
            this is expected format, you can optionally include url or body paramters but start stop and stepping are required
        '''
        if ("start" in request_custom_dict and request_custom_dict["start"] != ""):
            iterStart = request_custom_dict["start"]
        else:
            print('invalid custom json supplied: no start value')
            return {"error": "invalid custom json supplied: no start value"}
        if ("stop" in request_custom_dict and request_custom_dict["stop"] != ""):
            iterStop = request_custom_dict["stop"]
        else:
            print('invalid custom json supplied: no end value')
            return {"error": "invalid custom json supplied: no end value"}

        if ("stepping" in request_custom_dict and request_custom_dict["stepping"] != ""):
            custom_iter = current_val
            if (int(custom_iter) > int(iterStop)):
                return {"status": "complete"}
            else:
                return {"status": "continue", "value": custom_iter}
        else:
            print('invalid custom json supplied: no end value')
            return {"error": "invalid custom json supplied: no end value"}