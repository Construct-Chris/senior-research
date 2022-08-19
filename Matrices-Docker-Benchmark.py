from http.server import BaseHTTPRequestHandler, HTTPServer
import numpy as np 

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
        
            mat1 = np.random.rand(m, m)
            mat2 = np.random.rand(m, m)
            matrix_result = np.multiply(mat1, mat2)

            res = "result: " + str(matrix_result.shape)
            self.send_response(200)
            
        except:
            self.send_response(400)
            res = "the input is not a number"
        
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write(res.format(self.path).encode('utf-8'))
            
        
        
    

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

