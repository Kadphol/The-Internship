var crawler = require('../Question-4/Crawler'); 
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());
app.use(express.urlencoded({
    extended: true
}));

app.get('/companies', (req, res) => {
    var company = []
    crawler().then(function(result) { 
        result.sort(function(a,b) { 
            return a.text.length - b.text.length;
        });
        for(var i in result) { 
            let data = {
                "logo": `https://theinternship.io/${result[i].logo}`,
            }
            company.push(data)
        }
        res.json({"companies": company});
    }) 
})

app.listen(port, () => {
    console.log(`Start server at port ${port}`);
});
