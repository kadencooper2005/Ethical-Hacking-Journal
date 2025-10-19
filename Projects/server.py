import socket

HOST = '127.0.0.1' # create both host and port to connect to
PORT = 5555


def handle_request(conn):
    
    request_data = conn.recv(1024)
    print(f"Received request:\n{request_data.decode('utf-8')}")

    response_body = "<h1>Hello, world</h1>"
    response_headers = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"
    )
    http_response = response_headers.encode("utf-8") + response_body.encode("utf-8")
    conn.sendall(http_response)
    
    # Close the connection to the client
    conn.close()

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))

        server_socket.listen()
        print(f"Server listening on http://{HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            client_ip, client_port = addr
            print(f"Connected by: IP {client_ip}, Port {client_port}")


            handle_request(conn)


if __name__ == "__main__":
    run_server()
