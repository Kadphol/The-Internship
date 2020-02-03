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

        console.log(link);
    })
    .catch(console.error);