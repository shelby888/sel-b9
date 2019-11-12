
def test_login_to_admin_pannel(app):
    wd = app.wd
    wd.implicitly_wait(10)

    app.open_home_page()

    # assert wd.find_element_by_css_selector('#box-apps-menu').is_displayed()

    products = wd.find_elements_by_css_selector('.product')

    for product in products:
        assert len(product.find_elements_by_css_selector('.sticker')) == 1
