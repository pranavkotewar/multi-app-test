const http = require('http');
const port = process.env.PORT || 3000;
const page = '<html><head><meta charset="UTF-8"><title>Node App</title><style>body{font-family:Segoe UI,Arial;background:#0b1220;color:#e2e8f0;text-align:center;padding-top:15vh}h1{color:#fbbf24}</style></head><body><h1>Node.js App</h1><p>Deployed with the Node template</p><p>Started: ' + new Date().toISOString() + '</p></body></html>';
http.createServer(function (req, res) {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end(page);
}).listen(port, '0.0.0.0');
