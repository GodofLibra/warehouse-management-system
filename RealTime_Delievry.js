/* This File is not ready so please do not use it */

const http = require('http')
const xlsx = require('xlsx')
const path = require("path")

const port = 3000;

const server = http.createServer((req, res) => {
    console.log(req);
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    function Callfile(file) {
        const filePath = path.resolve(__dirname, file);

        const workbook = xlsx.readFile(filePath)
        const sheetNames = workbook.SheetNames;

        const data = xlsx.utils.sheet_to_html(workbook.Sheets[sheetNames[0]])

        res.write(data)
        // res.write(Callfile('test.xlsx'))
        res.write("code ended")
    }
    res.write('<input type="button" value="Refresh" onclick="msg()">')


})

server.listen(port, () => {
    console.log(`server listening at ${port}`)
});