
def test_login_to_admin_pannel(app):
    wd = app.wd
    wd.implicitly_wait(10)
    app.session.admin_login()

    assert wd.find_element_by_css_selector('#box-apps-menu').is_displayed()

    menu_elements = wd.find_elements_by_css_selector('#box-apps-menu li')

    list = []
    for item in menu_elements:
        list.append(item.get_attribute('id'))
    for item in list:
        wd.find_element_by_xpath(f"//li[@id='{item}']").click()
        assert wd.find_element_by_xpath('//h1').is_displayed()