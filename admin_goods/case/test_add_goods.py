import logging
import time

import pytest

from admin_goods.page.page_add_goods import Work
from admin_goods.utils import Driver


@pytest.mark.run(order=2)
class TestAdd:
    def setup_class(self):
        self.driver = Driver.get_driver()
        self.input = Work()

    def setup(self):
        time.sleep(3)
        self.driver.get("http://localhost/index.php/Admin/Index/index")
        self.driver.find_element_by_xpath("//*[@data-param='shop']/a").click()
        self.driver.find_element_by_xpath("//li[@class='active']/a").click()
        self.driver.switch_to.frame(self.driver.find_element_by_id("workspace"))
        self.driver.find_element_by_xpath("// div[ @ title = '添加商品'] / span").click()

    def teardown_class(self):
        time.sleep(2)
        # self.driver.switch_to.frame(self.driver.find_element_by_id("workspace"))
        self.driver.find_element_by_class_name("ncap-btn-big").click()
        # self.driver.switch_to.default_content()
        Driver.quit_web()

    @pytest.mark.parametrize(("goods_name", "summary", "article_num", "spu", "sku",
                              "category01", "category02", "category03", "brand", "supplier", "shop_price",
                              "market_price", "cost_price", "commission", "weight", "store_count", "keywords"),
                             [("华为nova6", "", "", "", "", "电脑、办公", "1", "123", "146", "1", "3000",
                               "3400", "2500", "", "250", "100", "华为 nova6 手机 电器")])
    def test_add_goods(self, goods_name, summary, article_num, spu, sku,
                       category01, category02, category03, brand, supplier, shop_price,
                       market_price, cost_price, commission, weight, store_count, keywords):
        logging.info("start->proxy")
        self.input.add_goods(goods_name, summary, article_num, spu, sku,
                             category01, category02, category03, brand, supplier, shop_price,
                             market_price, cost_price, commission, weight, store_count, keywords)
        # self.driver.find_element_by_name("goods_name").send_keys("华为nova6")  # 商品名称
        # self.driver.find_element_by_name("goods_remark").send_keys("")  # 商品简介
        # self.driver.find_element_by_name("goods_sn").send_keys("")  # 商品货号
        # self.driver.find_element_by_name("SPU").send_keys("")  # SPU
        # self.driver.find_element_by_name("SKU").send_keys("")  # SKU
        # Select(self.driver.find_element_by_name("cat_id")).select_by_visible_text("电脑、办公")  # 商品类别
        # time.sleep(2)
        # Select(self.driver.find_element_by_name("cat_id_2")).select_by_value("1")  # 商品类别
        # time.sleep(2)
        # Select(self.driver.find_element_by_name("cat_id_3")).select_by_value("123")  # 商品类别
        # time.sleep(2)
        # Select(self.driver.find_element_by_name("brand_id")).select_by_value("146")  # 商品品牌
        # Select(self.driver.find_element_by_name("suppliers_id")).select_by_value("1")  # 供应商
        # self.driver.find_element_by_name("shop_price").send_keys("3000")  # 本店售价
        # self.driver.find_element_by_name("market_price").send_keys("3400")  # 市场价
        # # self.driver.execute_script("window.scrollTo(900,1000)")
        # # time.sleep(3)
        # self.driver.find_element_by_name("cost_price").send_keys("2500")  # 成本价
        # self.driver.find_element_by_name("commission").send_keys("")  # 佣金
        # # 图片
        # # self.driver.find_element_by_class_name("type-file-file").send_keys("")
        # # self.driver.switch_to.frame(self.driver.find_element_by_id("layui-layer-iframe3"))
        # # self.driver.find_element_by_xpath("//div[@id='filePicker']/div/label").click()
        # self.driver.find_element_by_name("weight").send_keys("250")  # 商品重量
        # self.driver.find_element_by_xpath("//div[@class='onoff']/label[@for='is_free_shipping1']").click()  # 是否包邮
        # self.driver.find_element_by_name("store_count").send_keys("100")  # 库存总量
        # self.driver.find_element_by_name("keywords").send_keys("华为 nova6 手机 电器")  # 商品关键词
        self.driver.find_element_by_xpath("//div[@class='onoff']/label[@for='is_virtual1']").click()
        self.driver.switch_to.frame(self.driver.find_element_by_id("ueditor_0"))
        self.driver.find_element_by_xpath("//body/p").send_keys("嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻嘻寻")  # 商品详情描述
        self.driver.switch_to.default_content()
