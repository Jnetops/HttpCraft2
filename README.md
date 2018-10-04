# HttpCraft
Craft HTTP requests with options to iterate over provided values in URI or Body

Required Modules:

  Requests Library - http://docs.python-requests.org/en/master/ - pip install requests
  
  PyQt5 - https://www.riverbankcomputing.com/software/pyqt/download5 - pip install PyQt5
  
Overview:

  This tool is designed to allow a user to copy and paste http request details from proxy tools such as Fiddler (https://www.telerik.com/fiddler) and burp suite (https://portswigger.net/burp) and carry out automated bulk requests. The background being automating requests with the ability to iterate values within those requests

Usage:

  URI:
  
  Paste URI here, if custom variables supplied within URI, all occurences will be replaced
  Examples:
    http://google.com/111?post=111
    both occurences of 111 will be replaced in the iteration process


  Headers:
  
  Paste headers directly from proxy of choice, or manually enter them, line breaks are detected when building the headers
    
  Cookies:
  
  Paste headers directly from proxy or build manually
    
  POST / PUT / PATCH Body:
  
  Body will be sent based on two currently supported types.
  Current Support:
    Json
    x-www-form-urlencoded or basic
    Example:
      {"posts": [{"post1": 111}, {"post2": 222}]}
      post1=111&post2=222
        
  Request Types:
  
  Currently Supported:

  GET, POST, PUT, PATCH, DELETE
      
  Custom Variables:
  
  JSON entry that allows value manipulation in both the URI and Body or requests
  *for json, deep nested key/val pairs are supported 
  
  Example:
  
      {"body": "valKey", "url": "111", "start": 112, "end": 119, "stepping": 1}

  body value is the key in a json key/val pair, or the var title in urlencoded
  
  Example:
  
    {"posts": [{"post1": 111}, {"post2": 222}]}

  url is the value to iterate, rather than the var name
  it will replace all occurences of the value with it's updated, iterated value
  
  Example:
  
    http://www.google.com/111/post1=111

   Start / Stop:
   
    these are required and indicate the iteration span

   Stepping:
   
    how much to iterate per cycle
        
        

