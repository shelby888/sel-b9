def test_zone_state_sort(app):
    wd = app.wd
    wd.implicitly_wait(10)
    app.session.admin_login()

    assert wd.find_element_by_css_selector('#box-apps-menu').is_displayed()

    wd.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')


    leng = len(wd.find_elements_by_xpath("//tbody//a[contains(text(),'')]"))

    for id in range(leng):
        ls = []
        wd.find_elements_by_xpath("//tbody//a[contains(text(),'')]")[id].click()
        # проверяем сортировку стран
        states = wd.find_elements_by_xpath("//tbody//tr//td[2]")
        for state in states:
            ls.append(state.get_attribute('textContent'))
        s_ls = sorted(ls)
        assert ls == s_ls
        wd.find_element_by_xpath("//button[@name='cancel']").click()
