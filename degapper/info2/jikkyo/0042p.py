import http.server
PORT = '192.168.0.0'
address = ('', PORT)
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi-bin']
server = http.server.ThreadingHTTPServer(address, handler)
print('ポート', PORT, 'でwebサーバ稼働中')
print('終了はブラウザを閉じ、Ctrl+Cを押す。')
server.serve_forever()