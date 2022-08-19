from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "0.0.0.0"
serverPort = 5000

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        pass

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length)
        res = 'a'
        try:
            m = int(post_data.decode('utf-8'))

            res = "result: " + str( primes(m) )
            self.send_response(200)

        except:
            self.send_response(400)
            res = "the input is not a number"

        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(res.format(self.path).encode('utf-8'))

def primes(req):

    try:
        m = int(req)
        primes = list()
        co = 2
        while len(primes) < m:
            if is_prime(co):
                primes.append(co)
            co +=1

        return len(primes)
    except:
        return "the input is not a number"

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return False

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

