def test_open_browser(app):
    app.session.open_start_page()

def test_login_to_admin_pannel(app):
    app.session.admin_login()