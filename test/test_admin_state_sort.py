
def test_state_sort(app):
    wd = app.wd
    wd.implicitly_wait(10)
    app.session.admin_login()

    assert wd.find_element_by_css_selector('#box-apps-menu').is_displayed()

    wd.get('http://localhost/litecart/admin/?app=countries&doc=countries')

    ls = []

    ls_zones = []

    def normalize(st):
        if st[0] == 'Å':
            return 'Aland Islands'
        else:
            return st

    for element in wd.find_elements_by_xpath("//tr//td[5]//a[contains(text(),'')]"):
        ls.append(element.get_attribute('textContent'))
    assert ls == sorted(ls, key=normalize)

    i = 0
    rows = wd.find_elements_by_xpath("//tbody//tr")
    # leng = len(list(rows))

    for row in rows:
        cells = row.find_elements_by_xpath('//td')
        el_val = cells[5].get_attribute('textContent')
        if el_val != '0':
            ls_zones.append(i)
        i = i + 1

    for item in ls_zones:
        element = wd.find_elements_by_xpath("//tbody//tr")[item]
        element.find_element_by_xpath("//td[5]//a[contains(text(),'')]").click()
        ls_val = []
        for zone in wd.find_elements_by_xpath("//tbody//tr"):
            ls_val.append(zone.find_element_by_xpath("td[3]//input").get_attribute('value'))
        assert ls == sorted(ls)
        wd.find_element_by_xpath("//button[@name='cancel']").click()



