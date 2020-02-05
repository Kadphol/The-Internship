var crawler = require('../Question-4/Crawler'); //import crawler module

crawler().then(function(result) { //capture result of promise
    result.sort(function(a,b) { //sort by description length
        return a.text.length - b.text.length;
    });
    for(var i in result) { //print logo url
        console.log(result[i].logo)
    }
}).catch(function(error) {
    console.error(error);
})

