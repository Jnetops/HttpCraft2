import requests
import json
from headers import header
from cookies import *
from body import *
from params import *
from uri import *

class request(object):
    def button_pressed(uri, request_count, headers, cookies, body, request_custom, request_type):

        # build header dict
        request_headers = header.getHeaders(headers)

        # verify uri is valid
        if (uri != ""):
            request_uri = uri
        else:
            print("No URI, This is required to submit requests!")
            return

        # get cookie
        request_cookies = cookie.getCookies(cookies)

        # get body
        request_body = bodyParse.getBody(body)

        # if typical request without custom values, run selected number of times
        if (request_custom == ""):
            currCount = 1
            while (currCount <= request_count):
                request.plainRequest(request_uri, request_headers, request_cookies, request_body, request_count, request_type)
                currCount = currCount + 1
        # if custom values supplied, execute custom entry flow
        elif (request_custom != ""):
            try:
                # parse user entry to json, validate its valid format
                request_custom_dict = json.loads(request_custom)
            except:
                print("Custom Variables are not in json format")
                return
            request.customRequest(request_uri, request_headers, request_cookies, request_body, request_custom_dict, request_type)
        else:
            print("Strange, this is embarrassing, uknown error occured!")

    def customIterate(request_custom_dict, request_body, request_type, request_uri, current_val):
        
        status = paramVerify.verify(request_custom_dict, current_val)
        if ("error" in status):
            return
        elif ("status" in status):
            if (status["status"] == "complete"):
                return
            else:
                custom_iter = status["value"]
        

        if (request_type["type"] == "GET" or request_type["type"] == "DELETE"):
            if ("url" in request_custom_dict):
                iter_request_uri = uriParse.uriIter(request_custom_dict, request_uri, current_val)
            else:
                iter_request_uri = request_uri
            return {"uri": iter_request_uri, "value": custom_iter, "status": "continue"}

        elif (request_type["type"] == "POST" or request_type["type"] == "PUT" or request_type["PATCH"]):
            if ("body" in request_custom_dict):
                iter_request_body = bodyParse.bodyIter(request_custom_dict, request_body, request_type, custom_iter)
            else:
                iter_request_body = ""

            if ("url" in request_custom_dict):
                iter_request_uri = uriParse.uriIter(request_custom_dict, request_uri, current_val)
            else:
                iter_request_uri = request_uri
            return {"uri": iter_request_uri, "body": iter_request_body, "value": custom_iter, "status": "continue"}         

    def customRequest(request_uri, request_headers, request_cookies, request_body, request_custom_dict, request_type):
        # ignores request_count, utilizes start stop and stepping from custom variable json
        # request type
        if ("start" in request_custom_dict):
            currCount = int(request_custom_dict["start"])
        else:
            print("No start supplied")
            return

        if (request_type["GET"]):
            request_type["type"] = "GET"
            while currCount <= request_custom_dict["stop"]:
                requestDetails = request.customIterate(request_custom_dict, request_body, request_type, request_uri, currCount)
                if ("error" not in requestDetails):
                        if (requestDetails["status"] != "complete"):
                            r = requests.get(requestDetails["uri"], cookies=request_cookies, headers=request_headers, verify=False)
                            currCount = int(requestDetails["value"]) + 1
                            #print(str(r.content))
        elif (request_type["DELETE"]):
            request_type["type"] = "DELETE"
            while currCount <= request_custom_dict["stop"]:
                requestDetails = request.customIterate(request_custom_dict, request_body, request_type, request_uri, currCount)
                if ("error" not in requestDetails):
                        if (requestDetails["status"] != "complete"):
                            r = requests.delete(requestDetails["uri"], cookies=request_cookies, headers=request_headers, verify=False)
                            currCount = int(requestDetails["value"]) + 1
                            #print(str(r.content))
        elif (request_type["POST"]):
            # post chosen
            if (request_body["type"] == "json"):
                request_type["type"] = "POST"
                request_type["body"] = "json"
                while currCount <= request_custom_dict["stop"]:
                    requestDetails = request.customIterate(request_custom_dict, request_body["data"], request_type, request_uri, currCount)
                    if ("error" not in requestDetails):
                        if (requestDetails["status"] != "complete"):
                            r = requests.post(requestDetails["uri"], cookies=request_cookies, headers=request_headers, json=requestDetails["body"], verify=False)
                            currCount = int(requestDetails["value"]) + 1
                            #print(str(r.content))
            else:
                request_type["type"] = "POST"
                request_type["body"] = "plain"
                while currCount <= request_custom_dict["stop"]:
                    requestDetails = request.customIterate(request_custom_dict, request_body["data"], request_type, request_uri, currCount)
                    if ("error" not in requestDetails):
                        if (requestDetails["status"] != "complete"):
                            r = requests.post(requestDetails["uri"], cookies=request_cookies, headers=request_headers, data=requestDetails["body"], verify=False)
                            currCount = int(requestDetails["value"]) + 1
                            #print(str(r.content))
        elif(request_type["PUT"]):
            # put chosen
            if (request_body["type"] == "json"):
                request_type["type"] = "PUT"
                request_type["body"] = "json"
                while currCount <= request_custom_dict["stop"]:
                    requestDetails = request.customIterate(request_custom_dict, request_body["data"], request_type, request_uri, currCount)
                    if ("error" not in requestDetails):
                        if (requestDetails["status"] != "complete"):
                            r = requests.put(requestDetails["uri"], cookies=request_cookies, headers=request_headers, json=requestDetails["body"], verify=False)
                            currCount = int(requestDetails["value"]) + 1
                            #print(str(r.content))
            else:
                request_type["type"] = "PUT"
                request_type["body"] = "plain"
                while currCount <= request_custom_dict["stop"]:
                    requestDetails = request.customIterate(request_custom_dict, request_body["data"], request_type, request_uri, currCount)
                    if ("error" not in requestDetails):
                        if (requestDetails["status"] != "complete"):
                            r = requests.put(requestDetails["uri"], cookies=request_cookies, headers=request_headers, data=requestDetails["body"], verify=False)
                            currCount = int(requestDetails["value"]) + 1
                            #print(str(r.content))
        elif(request_type["PATCH"]):
            # put chosen
            if (request_body["type"] == "json"):
                request_type["type"] = "PATCH"
                request_type["body"] = "json"
                while currCount <= request_custom_dict["stop"]:
                    requestDetails = request.customIterate(request_custom_dict, request_body["data"], request_type, request_uri, currCount)
                    if ("error" not in requestDetails):
                        if (requestDetails["status"] != "complete"):
                            r = requests.patch(requestDetails["uri"], cookies=request_cookies, headers=request_headers, json=requestDetails["body"], verify=False)
                            currCount = int(requestDetails["value"]) + 1
                            #print(str(r.content))
            else:
                request_type["type"] = "PATCH"
                request_type["body"] = "plain"
                while currCount <= request_custom_dict["stop"]:
                    requestDetails = request.customIterate(request_custom_dict, request_body["data"], request_type, request_uri, currCount)
                    if ("error" not in requestDetails):
                        if (requestDetails["status"] != "complete"):
                            r = requests.patch(requestDetails["uri"], cookies=request_cookies, headers=request_headers, data=requestDetails["body"], verify=False)
                            currCount = int(requestDetails["value"]) + 1
                            #print(str(r.content))
        else:
            print('No Request Type Selected')
            return ""

    def plainRequest(request_uri, request_headers, request_cookies, request_body, request_count, request_type):
        # request type
        if (request_type["GET"]):
            # get chosen
            r = requests.get(request_uri, cookies=request_cookies, headers=request_headers, verify=False)
            #print(str(r.content))
        elif (request_type["DELETE"]):
            # delete chosen
            r = requests.delete(request_uri, cookies=request_cookies, headers=request_headers, verify=False)
            #print(str(r.content))
        elif (request_type["POST"]):
            # post chosen
            if (request_body["type"] == "json"):
                r = requests.post(request_uri, cookies=request_cookies, headers=request_headers, json=request_body["data"], verify=False)
            else:
                r = requests.post(request_uri, cookies=request_cookies, headers=request_headers, data=request_body["data"], verify=False)
            #print(str(r.content))
        elif (request_type["PUT"]):
            # put chosen
            if (request_body["type"] == "json"):
                r = requests.put(request_uri, cookies=request_cookies, headers=request_headers, json=request_body["data"], verify=False)
            else:
                r = requests.put(request_uri, cookies=request_cookies, headers=request_headers, data=request_body["data"], verify=False)
            #print(str(r.content))
        else:
            print("No Request Type Selected")
            return ""