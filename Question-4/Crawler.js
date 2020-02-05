const axios = require('axios');
const cheerio = require('cheerio');


const url = 'https://theinternship.io';

var crawler = function getCompanies(){
    const link = [];
    return axios(url).then(response => {
        const html = response.data;
        const $ = cheerio.load(html);

        $('div.partner').each(function () { //for each div className partner
            const logo = $(this).find('a > img').attr('src'); //find src attribute in img tag
            const text = $(this).find('span').text(); //find text in span tag
            link.push({
                logo,
                text,
            });
        });
        return link;
    }).catch();
}
module.exports = crawler; //export crawler module