const axios = require('axios');
const cheerio = require('cheerio');


const url = 'https://theinternship.io';

var crawler = function getCompanies(){
    const link = [];
    return axios(url).then(response => {
        const html = response.data;
        const $ = cheerio.load(html);

        $('div.partner').each(function () {
            const logo = $(this).find('a > img').attr('src');
            const text = $(this).find('span').text();
            link.push({
                logo,
                text,
            });
        });
        return link;
    }).catch();
}
module.exports = crawler;