import http.server
import socketserver
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    A custom request handler that handles different API endpoints.
    """

    def do_GET(self):
        # Route: Root endpoint "/"
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # Route: "/data" endpoint serving JSON
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            sample_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(sample_data).encode("utf-8"))

        # Route: "/status" endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # Route: "/info" endpoint (Optional but good for practice)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info_data).encode("utf-8"))

        # Error Handling: 404 Not Found for undefined endpoints
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

# Define the server port
PORT = 8000

# Start the server
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
