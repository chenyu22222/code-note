const http = require("http")
const config = require("./config").config

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader("Content_Type", "text/plain");
    
    switch(req.url){
        case "/": {
            res.end("hello world\n");
            break;
        };
        case "/about": res.end("This is about page.\n");
            break;
        case "/home": res.end("This is home page!");
            break;
        default:  res.end("not found.");
    }
    
    
})

server.listen(config.port, config.hostname, ()=> {
    console.log(`Server running at http://${config.hostname}:${config.port}/`)
})