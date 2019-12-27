link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    button = len(browser.find_elements_by_css_selector("button.btn.btn-lg"))
    assert button > 0, 'Кнопка добавления в корзину не найдена.'

# Команда time.sleep(30) должна быть добавлена проверяющим.
