# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PajakscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    url = scrapy.Field()
    nomor = scrapy.Field()
    tingkat_proses = scrapy.Field()
    klasifikasi = scrapy.Field()
    kata_kunci = scrapy.Field()
    tahun = scrapy.Field()
    tanggal_register = scrapy.Field()
    lembaga_peradilan = scrapy.Field()
    jenis_lembaga_peradilan= scrapy.Field()
    hakim_ketua = scrapy.Field()
    hakim_anggota = scrapy.Field()
    panitera = scrapy.Field()
    download_pdf = scrapy.Field()

    
