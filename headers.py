

class header(object):
    def getHeaders(headers):

        # return headerDict
        request_headers = headers
        if (request_headers != ""):
            headerDict = {}
            # split at new line detection
            splitHedaers = request_headers.split("\n")
            for header in splitHedaers:
                # split header and add it to header dict
                splitHeader = header.split(": ")
                headerDict[splitHeader[0]] = splitHeader[1]
            return headerDict
        else:
            return request_headers