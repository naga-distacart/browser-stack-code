# -*- coding: utf-8 -*-
class Locators():

    # Home page locators
    search_textbox_xpath = "//div/form[@class='search__form']/input[@name='q']"
    home_button_xpath = "//div[contains(@class,'logo')]/a[@title='Distacart']"
    shop_by_categories_xpath = "//li/a[text()='Shop by Categories']"
    product_main_menu_xpath = "//a[@data-dropdown-rel='{}']"
    pick_currency_div_xpath = "//ul[@class='menu right']/form/div/span[@class='current']"
    currency_select_id = "currencies"
    currency_select_xpath = "//ul[@class='menu right']/form/div/ul[@class='list']/li[text()='{}']"
    login_register_xpath = "//a[@title='My Account ']/span[text()='Login or Register']"
    user_name_id = "customer_email"
    user_password_id = "customer_password"
    login_button_xpath = "//form[@id='customer_login']/input[@class='btn action_button']"
    referral_button_id = "rewardify-referral"
    my_account_xpath = "//div[@class='cart-user-search']/ul/li/a/span[text()='My Account']"
    logout_xpath = "//span/a[@id='customer_logout_link']"
    currencies_list_xpath = "//ul[@class='menu right']/form/div/ul/li"
    cart_popup_order_notes_xpath = "//div[@class='div_note']//textarea[@id='note']"
    cart_popup_checkout_xpath = "//li[@class='cart-popup-top']/button[@name='checkout']"
    cart_popup_total_xpath = "//div[@class='freeze_cart_subtotal']/div[@class='cart-popup-customize your-cart cart_subtotal js-cart_subtotal']/span/span[@class='money']"
    cart_popup_item_price_xpath = "//ul[@class='cart_items js-cart_items clearfix']/li[@class='mini-cart__item clearfix']/div/div/strong/span[@class='money']"
    free_shipping_link_xpath = "//a[text()='Free Shipping']"
    returns_policy_link_xpath = "//a[text()='Free Returns']"
    suggest_a_product_homepage = "//li/a[text()='Suggest a Product']"
    suggest_product_page_title ="//li[@class='breadcrumbs__item']/a[text()='Suggest a Product']"
    suggest_product_page_element_cs = "//div/h5[text()='CONTACT US:']"
    suggest_a_product_page_element_name = "//div[text()='Name:']"
    send_button = "//input[@value='Send']"
    contact_us_link = "//li/a[text()='Contact Us']"
    contact_us_page_title = "//li[@class='breadcrumbs__item']/a[text()='Contact']"
    contact_us_page_email = "//a[text()='happy@distacart.com']"
    email_input_box = "//input[@type='email' ]"
   # notify_me_via_email_button = "//input[@value='Notify me via email']"

    # Cart slider locators
    #cart_free_shipping_msg_xpath = "//p[@class='freeShippingBarTxt']"
    cart_free_shipping_progress_bar_xpath = "//div[@class='myShippingBar']"
    cart_slider_quantity_plus_button_xpath = "//div[@class='mini-cart__item--content']/div[@class='mini-cart__item__title']/div[contains(@class,'product-quantity-box')]/span[@data-func='minus']"
    cart_slider_quantity_minus_button_xpath = "//div[@class='mini-cart__item--content']/div[@class='mini-cart__item__title']/div[contains(@class,'product-quantity-box')]/span/span[@class='icon-minus']"
   # cart_slider_product_shipping_info_xpath = "//span[@class='delivery_desc']"

    # Product page locators
    product_title_xpath = "//h1[@class='product_name']"
    product_vendor_xpath = "//p[@class='vendor-box']/span[contains(@class,'wk_seller')]/a"
    product_fulfilled_xpath = "//p/span[contains(@class,'vendor_padding')]/a"
    product_detail_star_badges_xpath = "//div[@class='seven columns medium-down--one-whole  omega']/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-prev-badge__stars']"
    product_detail_stars_xpath = "//div[@class='seven columns medium-down--one-whole  omega']/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-prev-badge__text']"
    product_detail_qa_icon_xpath = "//div[@class='seven columns medium-down--one-whole  omega']/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-qa-badge ']/span[@class='jdgm-qa-badge__icon']"
    product_detail_qa_text_xpath = "//div[@class='seven columns medium-down--one-whole  omega']/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-qa-badge ']/span[@class='jdgm-qa-badge__text']"
    product_page_price_xpath = "//div[@class='modal_price']/div/span/span/span"
    product_not_available_xpath = "//div[@class='product_availability_check']/p/b"
    product_sold_out_xpath = "//div[@class='product_availability_check']/p/span[text()='Sold Out']"
    product_notify_button_xpath = "//a[text()='Notify Me When Available']"
    product_variant_xpath = "//div[@value='{}']"
    product_notify_variant_xpath = "//div[@id='container']/form/div/div/select[@id='variants']"
    product_notify_email_xpath = "//input[@id='email']"
    product_notify_me_button_xpath = "//button[text()='Notify me when available']"

    product_xpath = "//span[text()='{}']"
    product_available_xpath = "//a[contains(@href,'{}')]/div/span/span[@class='current_price']/../../span[@class='title']"
    product_soldout_xpath = "//a[contains(@href,'{}')]/div/div[text()='Sold out']/../span[@class='title']"
    product_name_xpath = "//div[@class='product-details']/span[@itemprop='name']"
    product_category_title = "//h1[text()='{}']"
    add_to_cart_button_xpath = "//div[@class='seven columns medium-down--one-whole  omega']//div[@class='purchase-details']/div[contains(@class,'purchase-details__buttons')]/button/span[contains(text(),'Add to Cart')]"
    buy_it_now_button_xpath = "//button[text()='Buy it now']"
    sold_out_button_xpath = "//div[@class='seven columns medium-down--one-whole  omega']/div[@class='product_availability_check']/p/span[text()='Sold Out']"
    quantity_plus_button_xpath = "//div[@class='seven columns medium-down--one-whole  omega']//div[@class='purchase-details']/div[contains(@class,'purchase-details__quantity')]/span/span[@class='icon-plus']"
    quantity_minus_button_xpath = "//div[@class='seven columns medium-down--one-whole  omega']//div[@class='purchase-details']/div[contains(@class,'purchase-details__quantity')]/span/span[@class='icon-minus']"
    load_more_button_xpath = "//span/a[contains(@class,'load-more__btn')]"
    buy_it_now_display_none_xpath = "//div[@class='shopify-payment-button' and @style='display: none;']"
    product_price_xpath = "//div[@class='seven columns medium-down--one-whole  omega']/div/p[@class='modal_price']/span/span/span/span/span"
    added_button_xpath = "//button[@class='cbb-also-bought-add-to-cart-button']/span[text()='Added']"
    shipping_info_xpath = "//div[@class='seven columns medium-down--one-whole  omega']//span[@class='delivery_desc']"
    quantity_input_xpath = "//div[@class='seven columns medium-down--one-whole  omega']//div[@class='purchase-details']/div[contains(@class,'purchase-details__quantity')]/input[@id='quantity']"
    max_quantity_msg_xpath = "//div[@class='seven columns medium-down--one-whole  omega']//div[@class='purchase-details']/p[@id='variant_qty_exceeds_msg']"
    notify_button_xpath = "//div[@class='seven columns medium-down--one-whole  omega']//div[@class='purchase-details']/div[contains(@class,'purchase-details__buttons')]/a[text()='Notify Me When Available']"

    # Cart page elements
    cart_quantity_plus_button_xpath = "//div[@class='product-quantity-box left']/span[@data-func='plus']"
    cart_quantity_minus_button_xpath = "//div[@class='product-quantity-box left']/span[@data-func='minus']"
    cart_count_xpath = "//div[@class='top-bar--right-menu']//div[@class='cart-container']/a/span[@class='cart_count']"
    cart_link_xpath = "//div[@class='top-bar--right-menu']//div[@class='cart-container']/a[@class='icon-bag mini_cart ']"
    cart_item_price = "//div[@class='two-thirds columns medium-down--one-whole cart_content_info cart__item--content']//p[@class='modal_price']/span/span"
   # cart_max_quantity_msg_xpath = "//div[@class='eleven columns omega cart_content_info']/p[contains(@class,'warning')]"
   # cart_shipping_info_xpath = "//div[@class='eleven columns omega cart_content_info']/span[@class='delivery_desc']"
    #cart_total_shipping_info_xpath = "//div[contains(@class,clearfix)]/div[contains(@class,'medium-down--one-whole')]/span[@class='description']"
    cart_page_total_price_xpath = "//div[@class='//div[@class='one-half column medium-down--one-whole']/div[@class='subtotal']/div/p/span/span/span[@class='money']']"
    #cart_item_price_currency_code_xpath = "//div[@class='eleven columns omega cart_content_info']/p[@class='modal_price']/span"
    #cart_page_total_currency_code_xpath = "//div[@class='five columns medium-down--one-whole']/div/div/p/span/span[@class='money']"
    cart_page_remove_button_xpath = "//div[@class='cart-quantity-remove']/div/a[@data-remove-item='cart-template']"
    cart_page_heading = "//h1[text()='Shopping Cart']"
    checkout_buttom= "//button[@id='checkout']"
    continue_shopping_link="//div[@class='one-half column medium-down--one-whole']//a[text()='Continue Shopping']"

    # Checkout page elements
    checkout_button_id = "checkout"
    checkout_page_total_price_xpath = "//td[@class='total-line__price payment-due']/span[@class='payment-due__price skeleton-while-loading--lg']"
    checkout_item_count_xpath = "//span[@class='product-thumbnail__quantity']"

#need to change paths for product tile elements
    # Product tile elements
    product_tile_thumbnail_xpath = "//div[@class='product-wrap']/div/div[@class='thumbnail-overlay']/a[contains(@href,'collections')]"
    product_tile_stars_badge_xpath = "//div[@class='product-wrap']/a[contains(@href,'collections')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-prev-badge__stars']"
    product_tile_stars_xpath = "//div[@class='product-wrap']/a[contains(@href,'collections')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-prev-badge__text']"
    product_tile_qa_icon_xpath = "//div[@class='product-wrap']/a[contains(@href,'collections')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-qa-badge ']/span[@class='jdgm-qa-badge__icon']"
    product_tile_qa_text_xpath = "//div[@class='product-wrap']/a[contains(@href,'collections')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-qa-badge ']/span[@class='jdgm-qa-badge__text']"
    product_tile_reviews_display_xpath = "//div[@class='product-wrap']/a[contains(@href,'collections')]/div/div/div/span[@class='jdgm-prev-badge__text']"
    product_tile_price_xpath = "//div[@class='product-wrap']/a[contains(@href,'collections')]/div/span[@class='price ']/span/span[@class='money']"

    # Related product elements
    related_product_thumbnail_xpath = "//section[contains(@class,'datacue-similar')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]"
    related_product_name_xpath = "//section[contains(@class,'datacue-similar')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/p[@class='datacue-rec-product-title']/a"
    related_product_stars_badge_xpath = "//section[contains(@class,'datacue-similar')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-prev-badge__stars']"
    related_product_stars_xpath = "//section[contains(@class,'datacue-similar')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-prev-badge__text']"
    related_product_qa_icon_xpath = "//section[contains(@class,'datacue-similar')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-qa-badge ']/span[@class='jdgm-qa-badge__icon']"
    related_product_qa_text_xpath = "//section[contains(@class,'datacue-similar')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-qa-badge ']/span[@class='jdgm-qa-badge__text']"
    related_product_reviews_display_xpath = "//div[@class='product-wrap']/a[contains(@href,'collections')]/div/div[@class='shopify-reviews reviewsVisibility--true']"
    #product_tile_price_xpath = "//section[contains(@class,'datacue-similar')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/p/span[@class='datacue-rec-current-price']/span/span[@class='money']"
    related_product_price_xpath = "//section[contains(@class,'datacue-similar')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/p/span/span[@class='money']"

    # Customer who bought this item also bought elements
    cbb_product_image_xpath = "//ul[@class='cbb-also-bought-slider-list']/li[@class='cbb-also-bought-product']/a/div[@class='cbb-also-bought-product-image']"
    cbb_product_name_xpath = "//ul[@class='cbb-also-bought-slider-list']/li[@class='cbb-also-bought-product']/h3[@class='cbb-also-bought-product-name']/a[contains(@href,'products')]"
    cbb_product_variant_xpath = "//ul[@class='cbb-also-bought-slider-list']/li[@class='cbb-also-bought-product']/select[contains(@class,'variant-select')]"
    cbb_product_price_xpath = "//ul[@class='cbb-also-bought-slider-list']/li[@class='cbb-also-bought-product']/div[@class='cbb-also-bought-product-price-container']"
    cbb_product_add_to_cart_xpath = "//ul[@class='cbb-also-bought-slider-list']/li[@class='cbb-also-bought-product']/button[@class='cbb-also-bought-add-to-cart-button']"
    cbb_product_current_price_xpath = "//ul[@class='cbb-also-bought-slider-list']/li[@class='cbb-also-bought-product']/div[@class='cbb-also-bought-product-price-container']/span/span[@class='money']"
    cbb_section_xpath = "//div[@class='cbb-also-bought-container cbb-desktop-view']"

    # Recommended for you elements
    rec_product_image_xpath = "//section[contains(@class,'datacue-rec-section')]/div/div/div/ul/li/div/a/img"
    rec_product_name_xpath = "//section[contains(@class,'datacue-rec-section')]/div/div/div/ul/li/p/a"
    rec_product_price_xpath = "//section[contains(@class,'datacue-rec-section')]//ul/li/p/span/span[@class='money']"
    rec_product_stars_badge_xpath = "//section[contains(@class,'datacue-rec-section')]//ul/li/div[@class='datacue-rec-product-rating-placeholder']/div/div[contains(@class,'jdgm-prev-badge')]/span[@class='jdgm-prev-badge__stars']"
    rec_product_stars_xpath = "//section[contains(@class,'datacue-rec-section')]//ul/li/div[@class='datacue-rec-product-rating-placeholder']/div/div[contains(@class,'jdgm-prev-badge')]/span[@class='jdgm-prev-badge__text']"
    rec_product_current_price_xpath = "//section[contains(@class,'datacue-rec-section')]/div/div/div/ul/li[@class='datacue-rec tns-item tns-slide-active']/p/span[@class='datacue-rec-current-price']/span"

    # Recently viewed product elements
    #recent_product_thumbnail_xpath = "//section[contains(@class,'datacue-recent')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/div/a"
    recent_product_name_xpath = "//div[@class='js-recently-viewed-product']/div/a/div/span"
    recent_product_stars_badge_xpath = "//div[@class='js-recently-viewed-product']/div//a/div/div/div/span[@class='jdgm-prev-badge__stars']"
    #recent_product_stars_xpath = "//section[contains(@class,'datacue-recent')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/div/div[contains(@class,'jdgm-widget')]/div/span[@class='jdgm-prev-badge__text']"
    recent_product_qa_icon_xpath = "//div[@class='js-recently-viewed-product']/div//a/div/div/div/span/span[@class='jdgm-qa-badge__icon']"
    recent_product_qa_text_xpath = "//div[@class='js-recently-viewed-product']/div//a/div/div/div/span[@class='jdgm-prev-badge__text']"
    recent_product_price_xpath = "//div[@class='js-recently-viewed-product']//div[@class='product-details']//span[@class='current_price']/span/span[@class='money']"
    #recent_product_current_price_xpath = "//section[contains(@class,'datacue-recent')]/div/div/div/ul/li[contains(@class,'tns-slide-active')]/p[@class='datacue-rec-prices']/span/span[@class='money']"
    #Recently Viewed Elements
    recently_viewed_section = "//h2[contains(text(),'Recently viewed products')]"
    recently_viewed_product_element = "//a[@title='Patanjali Divya Coronil Kit - Coronil Tablet, Anu Taila, Swasari Vati']/../../../../../../../h3[text()='Recently viewed']"

    #In Stock Elements
    in_stock_text_xpath ="//div[contains(text(),'Show in stock only')]"
    in_stock_checkbox_xpath ="//input[@type='checkbox' and @id='show_in_stock_only']"
    no_stock_page_title = "//h1[text()='No products in stock currently in this category']"
    sold_out_xpath = "//div[text()='Sold out']"

    # Seller profile page elements
    seller_profile_xpath = "//div[contains(@class,'mp-store-name')]/span"

    #Shipping text box elements
    shipping_box_xpath = "//div[@id='shipping_info_div']"
    shipping_info_header = "//div/b[text()='Shipping Information']"
    #Shipping info for USD
    shipping_details_xpath_USD  = "//div[text()='Free Express shipping to all over  United States on orders of $49 USD or more']"
    shipping_delay_xpath_USD = "//div[text()='Due to COVID19 situation, please expect delay in delivery(5 - 7 business days)']"
    shipping_custom_duties_xpath_USD = "//div[text()='100% Satisfaction Guaranteed']"
    #Shipping info for AUD
    shipping_details_xpath_AUD = "//div[text()='Free Express shipping to all over  Australia on orders of $68.99 AUD or more']"
    #Shipping info for CAD
    shipping_details_xpath_CAD = "//div[text()='Free Express shipping to all over  Canada  on orders of $65 CAD or more']"
    #Shipping info for CHF
    shipping_details_xpath_CHF = "//div[text()='  Free express shipping to  Switzerland  on orders over SFr. 47 or more']"
    # Shipping info for EUR
    shipping_details_xpath_EUR = "//div[text()='Free Express shipping to all over European Countries on orders of €44 or more']"
    # Shipping info for GBP
    shipping_details_xpath_GBP = "//div[text()='Free shipping to all over  United Kingdom  on orders of £50 or more']"
    # Shipping info for INR
    shipping_details_xpath_INR = "//div[text()='Free shipping from India to USA, Canada, Netherlands and UK on Orders of Rs. 3000 or more']"
    #Shipping info for SGD
    shipping_details_xpath_SGD = "//div[text()='Free Express shipping to all over  Singapore on orders of $67.30 SGD or more']"
    #Shipping info for MXN
    shipping_details_xpath_MXN = "//div[text()='Free Express shipping to all over  Mexico on orders of $998 MXN or more']"
    #patanjali product page elements
    patanjali_giloy_product_page_element = "//div/span/a/span[text()='Home']/../../../span/a/span[text()='Products']/../../../span/a/span[text()='Patanjali Giloy Ghanvati (40 GM)']"

    #Recently Viewed Elements
    recently_viewed_section = "//h2[contains(text(),'Recently viewed products')]"
    recently_viewed_product_element = "//a[@title='Patanjali Divya Coronil Kit - Coronil Tablet, Anu Taila, Swasari Vati']/../../../../../../../h3[text()='Recently viewed']"

    #cart_slider_express_checkout_elements
    shoppay_element = "//div[@role='button' and @data-testid='ShopifyPay-button']"
    googlepay_element ="//div[@role='button' and @data-testid='GooglePay-button']"
    shoppay_checkout_page_element= "//h2[text()='Quick checkout']"
    quick_checkout_element = "//h3[text()='Order summary']"

    #add_to_cart_elements
    ayurvedic_random_product_element = "//div[@class='product-details']/span"
    add_to_cart_button_card = "//div[@class='collection_addtocart']/button[text()='Add to Cart']/../../../../../div[@class='product-details']/span[text()='{}']"

    # Blog page elements
    blog_next_button_xpath = "//span[@class='next']/a"
    blog_prev_button_xpath = "//span[@class='prev']/a"
    blog_read_more_button_xpath = "//div[@class='sixteen columns equal-columns--outside-trim equal-columns--clear']/div/a[text()='Read More']"