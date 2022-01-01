const http = require('http');
const xlsx = require('xlsx')
const path = require("path");

const filePath = path.resolve(__dirname, "test.xlsx");

const workbook = xlsx.readFile(filePath)
const sheetNames = workbook.SheetNames;

const data = xlsx.utils.sheet_to_html(workbook.Sheets[sheetNames[0]])
const port = 3000;
const server = http.createServer((req, res) => {
    console.log(req);
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    res.write(data)

})
server.listen(port, () => {
    console.log(`server listening at ${port}`)
});