class ArtPageLocators(object):
    CSS_SLIDER = '#carousel.carousel'
    CSS_SLIDER_ELEMENTS = '.carousel-item'
    XPATH_SLIDES_TITLES = '//*[@id="carousel"]/ul/li//*[contains(@class, "text-uppercase")]'
    CSS_SLIDES_TITLES = 'h2.text-uppercase'
    CSS_ARTICLE_MINIATURE = 'article.product-miniature.js-product-miniature'
    XPATH_MOUNTAIN_FOX = '//*[@id="js-product-list"]/div[1]/article[4]/div/div[1]/h1/a'
    XPATH_BTN_ADD_TO_CHART = '//div[@class="add"]/button'
    XPATH_MODAL_BTN_PROCEED = '//a[@class="btn btn-primary"]'
    XPATH_MODAL_TITLE = '//*[@id="myModalLabel"]'


