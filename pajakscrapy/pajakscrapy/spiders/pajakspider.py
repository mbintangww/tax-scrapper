import scrapy
from pajakscrapy.items import PajakscrapyItem

class PajakspiderSpider(scrapy.Spider):
    name = "pajakspider"
    start_urls = ["https://putusan3.mahkamahagung.go.id/direktori/index/kategori/pajak-2.html"]
    headers = {
    'authority': 'www.google-analytics.com',
    'accept': '*/*',
    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-length': '0',
    'content-type': 'text/plain',
    'origin': 'https://putusan3.mahkamahagung.go.id',
    'pragma': 'no-cache',
    'referer': 'https://putusan3.mahkamahagung.go.id/',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36'
    }
    def parse(self, response):
        print(response.url)
        books = response.css('.spost .entry-c strong a::attr(href)').getall()
        for book in books:
            yield scrapy.Request(
                url=book,
                headers=self.headers,
                callback=self.parse_book
            )
    
        next_page_url = response.css('.pagination li:nth-last-child(2) a::attr(href)').getall()[1]
        if next_page_url:
            yield response.follow(next_page_url, callback=self.parse)
     

    def parse_book(self, response):
        table = response.css("table")
        card = response.css('.card-body')
        pajak_item = PajakscrapyItem()
    
        pajak_item['url'] = response.url,
        pajak_item['nomor'] = table.css('tr:nth-child(2) td:nth-child(2)::text').get(),
        pajak_item['tingkat_proses'] = table.css('tr:nth-child(3) td:nth-child(2)::text').get(),
        pajak_item['klasifikasi' ] = table.css('tr:nth-child(4) td:nth-child(2) a::text').getall()[1],
        pajak_item['kata_kunci'] = table.css('tr:nth-child(5) td:nth-child(2)::text').get().strip(),
        pajak_item['tahun'] = table.css('tr:nth-child(6) td:nth-child(2)::text').get().strip(),
        pajak_item['tanggal_register'] = table.css('tr:nth-child(7) td:nth-child(2)::text').get().strip(),
        pajak_item['lembaga_peradilan'] = table.css('tr:nth-child(8) td:nth-child(2) a::text').get(),
        pajak_item['jenis_lembaga_peradilan']=  table.css('tr:nth-child(9) td:nth-child(2)::text').get().strip(),
        pajak_item['hakim_ketua'] = table.css('tr:nth-child(10) td:nth-child(2)::text').get().strip(),
        pajak_item['hakim_anggota'] = table.css('tr:nth-child(11) td:nth-child(2)::text').get().strip(),
        pajak_item['panitera'] = table.css('tr:nth-child(12) td:nth-child(2)::text').get().strip(),
        pajak_item['download_pdf'] = card.css('li:nth-child(6) a::attr(href)').get(),
    
        yield pajak_item
