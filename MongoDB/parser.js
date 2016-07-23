var jsonfile = require('jsonfile');
var path = require('path');
var file = path.resolve(__dirname, '../raw_data/h9.json');
var fs = require('fs');
var obj;

console.log(appDir);

fs.readFile(file, 'utf8', function(err, data){
    
    if (err) throw err;
    obj = JSON.parse(data);   
})






/*
jsonfile.readFile(file, function(err, obj) {
    
    for(var i = 0; i< obj.length; ++i){
        console.log("type:" + obj[i].type);
    }
     
})
*/

