from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laptop Specifications</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: rgb(158, 221, 239);
          
            display: flex;
            justify-content: center;
            align-items: center;
            height: 300vh;
        }
        .specs-container {
            background-color:rgb(163, 58, 182);
            padding: 20px;
            border-radius: 10px;
            box-shadow: beige;
            width: 600px;
        }
        h1 {
            text-align: center;
            color:rgb(104, 8, 8);
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid rgb(165, 158, 158);
        }
        th {
            background-color: #c3c5cb;
        }
    </style>
</head>
<body>
    <div class="specs-container">
        <h1>Laptop Specifications<br>RISHIVARMAN R<br>(24900419)</h1>
        <table>
            <tr>
                <th>Specification</th>
                <th>Details</th>
            </tr>
            <tr>
                <td>Brand</td>
                <td>LENOVO</td>
            </tr>
            <tr>
                <td>Model</td>
                <td>ThinkPad E16 Gen 1</td>
            </tr>
            <tr>
                <td>Processor</td>
                <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
            </tr>
            <tr>
                <td>RAM</td>
                <td>16 GB (15.7 GB usable)</td>
            </tr>
            <tr>
                <td>Storage</td>
                <td>350.8 GB</td>
            </tr>
            <tr>
                <td>Graphics</td>
                <td>NVIDIA GeForce GTX 1650</td>
            </tr>
            <tr>
                <td>Display</td>
                <td>16inch Full HD</td>
            </tr>
            <tr>
                <td>Battery Life</td>
                <td>Up to 48 hours</td>
            </tr>
            <tr>
                <td>Operating System</td>
                <td>Windows 11</td>
            </tr>
            <tr>
                <td>Price</td>
                <td>70000 INR</td>
            </tr>
        </table>
    </div>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()