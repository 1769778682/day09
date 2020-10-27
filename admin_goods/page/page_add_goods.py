from selenium.webdriver.common.by import By



# 对象库层
from admin_goods.base.base_add_goods import BaseAdd, BaseAction


class FindElem(BaseAdd):
    def __init__(self):
        super().__init__()
        self.goods_name = (By.NAME, "goods_name")
        self.summary = (By.NAME, "goods_remark")
        self.article_num = (By.NAME, "goods_remark")
        self.spu = (By.NAME, "SPU")
        self.sku = (By.NAME, "SKU")
        self.category01 = (By.NAME, "cat_id")
        self.category02 = (By.NAME, "cat_id_2")
        self.category03 = (By.NAME, "cat_id_3")
        self.brand = (By.NAME, "brand_id")
        self.supplier = (By.NAME, "suppliers_id")
        self.shop_price = (By.NAME, "shop_price")
        self.market_price = (By.NAME, "market_price")
        self.cost_price = (By.NAME, "cost_price")
        self.commission = (By.NAME, "commission")
        self.weight = (By.NAME, "weight")
        self.free_mail = (By.XPATH, "//div[@class='onoff']/label[@for='is_free_shipping1']")
        self.store_count = (By.NAME, "store_count")
        self.keywords = (By.NAME, "keywords")

    def find_name(self):
        return self.driver.find_element(self.goods_name)  # 商品名称

    def find_summary(self):
        return self.find_elem(self.summary)  # 商品简介

    def find_article_num(self):
        return self.find_elem(self.article_num)  # 商品货号

    def find_spu(self):
        return self.find_elem(self.spu)  # SPU

    def find_sku(self):
        return self.find_elem(self.sku)  # SKU

    def find_category01(self):
        return self.find_elem(self.category01)  # 商品类别

    def find_category02(self):
        return self.find_elem(self.category02)  # 商品类别

    def find_category03(self):
        return self.find_elem(self.category03)  # 商品类别

    def find_brand(self):
        return self.find_elem(self.brand)  # 商品品牌

    def find_supplier(self):
        return self.find_elem(self.supplier)  # 供应商

    def find_shop_price(self):
        return self.find_elem(self.shop_price)  # 本店售价

    def find_market_price(self):
        return self.find_elem(self.market_price)  # 市场价

    def find_cost_price(self):
        return self.find_elem(self.cost_price)  # 成本价

    def find_commission(self):
        return self.find_elem(self.commission)  # 佣金

    def find_weight(self):
        return self.find_elem(self.weight)  # 商品重量

    def find_free_mail(self):
        return self.find_elem(self.free_mail)  # 是否包邮

    def find_store_count(self):
        return self.find_elem(self.store_count)  # 库存总量

    def find_keywords(self):
        return self.find_elem(self.keywords)  # 商品关键词


class Action(BaseAction):
    def __init__(self):
        self.driver = FindElem()

    def input_name(self, goods_name):
        self.input_text(self.driver.find_name(), goods_name)

    def input_summary(self, summary):
        self.input_text(self.driver.find_summary(), summary)  # 商品简介

    def input_article_num(self, article_num):
        self.input_text(self.driver.find_article_num(), article_num)  # 商品货号

    def input_spu(self, spu):
        self.input_text(self.driver.find_spu(), spu)  # SPU

    def input_sku(self, sku):
        self.input_text(self.driver.find_sku(), sku)  # SKU

    def select_category01(self, category01):
        self.select(self.driver.find_category01(), category01)  # 商品类别

    def select_category02(self, category02):
        self.select(self.driver.find_category02(), category02)  # 商品类别"1"

    def select_category03(self, category03):

        self.select(self.driver.find_category03(), category03)  # 商品类别"123"

    def select_brand(self, brand):
        self.select(self.driver.find_brand(), brand)  # 商品品牌"146"

    def select_supplier(self, supplier):
        self.select(self.driver.find_supplier(), supplier)  # 供应商"1"

    def input_shop_price(self, shop_price):
        self.input_text(self.driver.find_shop_price(), shop_price)  # 本店售价

    def input_market_price(self, market_price):
        self.input_text(self.driver.find_market_price(), market_price)  # 市场价

    def input_cost_price(self, cost_price):
        self.input_text(self.driver.find_cost_price(), cost_price)  # 成本价

    def input_commission(self, commission):
        self.input_text(self.driver.find_commission(), commission)  # 佣金

    def input_weight(self, weight):
        self.input_text(self.driver.find_weight(), weight)  # 商品重量

    def input_free_mail(self):
        self.driver.find_free_mail().click()  # 是否包邮

    def input_store_count(self, store_count):
        self.input_text(self.driver.find_store_count(), store_count)  # 库存总量

    def input_keywords(self, keywords):
        self.input_text(self.driver.find_keywords(), keywords)  # 商品关键词


class Work(object):
    def __init__(self):
        self.add = Action()

    def add_goods(self, goods_name, summary, article_num, spu, sku,
                  category01, category02, category03, brand, supplier, shop_price,
                  market_price, cost_price, commission, weight, store_count, keywords):
        self.add.input_name(goods_name)
        self.add.input_summary(summary)
        self.add.input_article_num(article_num)
        self.add.input_spu(spu)
        self.add.input_sku(sku)
        self.add.select_category01(category01)
        self.add.select_category02(category02)
        self.add.select_category03(category03)
        self.add.select_brand(brand)
        self.add.select_supplier(supplier)
        self.add.input_shop_price(shop_price)
        self.add.input_market_price(market_price)
        self.add.input_cost_price(cost_price)
        self.add.input_commission(commission)
        self.add.input_weight(weight)
        self.add.input_free_mail()
        self.add.input_store_count(store_count)
        self.add.input_keywords(keywords)
