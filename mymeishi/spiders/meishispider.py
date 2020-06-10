import scrapy
from mymeishi.items import MymeishiItem
from scrapy.http import Request

class MeishiSpider(scrapy.Spider):
    name = "meishi"
    allowed_domains = ["home.meishichina.com"]
    start_urls = ["https://home.meishichina.com/recipe-10.html"]

    def parse(self, response):
        id = 9
        while id < 400000:
            id = id +1
            url = 'https://home.meishichina.com/recipe-'+str(id)+'.html'
            yield Request(url = url, callback = self.parse_detail)

    def parse_detail(self, response):
        item = MymeishiItem()
        item['name'] = response.xpath('//a[@id="recipe_title"]/text()').get()   
        item['categories'] = response.xpath('//a[@class="vest"]/text()').getall()

        main_ingredients = response.xpath('//fieldset[@class="particulars"][1]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s1"]/a/b/text() | //fieldset[@class="particulars"][1]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s1"]/b/text()').getall()
        main_amounts = response.xpath('//fieldset[@class="particulars"][1]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s2"]/text()').getall()
        item['main_ingredients'] = [main_ingredient+main_amount for main_ingredient, main_amount in zip(main_ingredients, main_amounts)]

        auxiliary_ingredients = response.xpath('//fieldset[@class="particulars"][2]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s1"]/a/b/text() | //fieldset[@class="particulars"][2]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s1"]/b/text()').getall()
        auxiliary_amounts = response.xpath('//fieldset[@class="particulars"][2]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s2"]/text()').getall()
        item['auxiliary_ingredients'] = [auxiliary_ingredient+auxiliary_amount for auxiliary_ingredient, auxiliary_amount in zip(auxiliary_ingredients, auxiliary_amounts)]

        seasonings = response.xpath('//fieldset[@class="particulars"][3]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s1"]/a/b/text()  | //fieldset[@class="particulars"][3]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s1"]/b/text()').getall()
        seasoning_amounts = response.xpath('//fieldset[@class="particulars"][3]/div[@class="recipeCategory_sub_R clear"]/ul/li/span[@class="category_s2"]/text()').getall()
        item['seasonings'] = [seasoning+seasoning_amount for seasoning, seasoning_amount in zip(seasonings, seasoning_amounts)]

        item['craft'] = response.xpath('//div[@class="recipeCategory_sub_R mt30 clear"]/ul/li[2]/span[@class="category_s1"]/a/text()').get()
        item['taste'] = response.xpath('//div[@class="recipeCategory_sub_R mt30 clear"]/ul/li[1]/span[@class="category_s1"]/a/text()').get()
        yield item