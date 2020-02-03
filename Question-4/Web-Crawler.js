const axios = require('axios')
const cheerio = require('cheerio')

const url = 'https://theinternship.io'

axios(url)
    .then(response => {
        const html = response.data;
        const $ = cheerio.load(html);
        const link = [];

        $('div.partner').each(function () {
            const src = $(this).find('a > img').attr('src');
            const text = $(this).find('span').text();
            link.push({
                src,
                text,
            });
        });
        var byText = link.slice(0);
        byText.sort(function(a,b) {
            return a.text.length - b.text.length;
        });
        //console.log(link)
        for(var company in byText) {
            console.log(byText[company].src);
        }
    })
    .catch(console.error);