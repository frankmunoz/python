from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# https://sites.google.com/chromium.org/driver/downloads?authuser=0
# https://chromedriver.storage.googleapis.com/index.html?path=100.0.4896.60/
url = "https://www.homecenter.com.co/homecenter-co/"

driver = webdriver.Chrome("/Users/franciscomunoz/Documents/Development/selenium/drivers/chromedriver")
driver.get(url)

driver.find_element(By.CLASS_NAME,"DesktopSearchBar-module_searchbox-input__HXYgR").send_keys('Cemento')
driver.find_element(By.CLASS_NAME,"DesktopSearchBar-module_searchbox-input__HXYgR").send_keys(Keys.RETURN)

#driver.find_element_by_class_name("DesktopSearchBar-module_searchbox-input__HXYgR").send_keys('Cemento')
#driver.find_element_by_class_name("DesktopSearchBar-module_searchbox-input__HXYgR").send_keys(Keys.RETURN)
#driver.find_element_by_css_selector("input[type=\"submit\" i]").click()


#<div class="jsx-110785930 product-brand-badge"><div class="jsx-110785930 product-brand"><a href="/homecenter-co/product/13846/cemento-argos-gris-50kg/13846/?queryId=bddbb8ca-c78d-4031-9855-86e63f1aaf22" id="testId-Link-brand-pdp-link" rel="" class="jsx-4282314783 link link-inherit "><div class="jsx-110785930 brand-name">ARGOS</div></a></div></div>

'''
resultProducts = driver.find_elements(By.CLASS_NAME, "search-results-products-container-list-view")
productBrands = driver.find_elements(By.CLASS_NAME, "product-brand")
for productBrand in productBrands:
    #   print(productBrand.text)
    brand = resultProducts.fin_element(By.CLASS_NAME, "product-brand")
    print(brand.text)
'''

items = driver.find_elements(By.CLASS_NAME, "product-container")
for item in items:
    brand = item.find_element(By.CLASS_NAME,"product-brand")
    price = item.find_element(By.XPATH,'//span[@class="jsx-4135487716"]')
    priceUnit = item.find_element(By.XPATH,'//span[@class="jsx-4135487716 price-unit"]')
    print(' Brand:' +  brand.text, ' Price:', price.get_attribute("textContent"), ' Unit:', priceUnit.get_attribute("textContent"))
#TypeError: can only concatenate str (not "WebElement") to str
