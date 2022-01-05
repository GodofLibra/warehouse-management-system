/*In oder to run this file please follow these steps 
1. Download NodeJs in your system.
2. download the entire folder in your system.
3. open terminal in this folder and run the following command
"npm i"
4. once you run this command a folder of node modules will be created, if you see this folder, you are good to go :)

*/


const http = require('http');
const xlsx = require('xlsx')
const path = require("path");

const filePath = path.resolve(__dirname, "Sample Data.xlsx");

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