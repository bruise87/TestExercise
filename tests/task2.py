from playwright.sync_api import sync_playwright, expect


def is_sberbank_login_fail():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://online.sberbank.ru/CSAFront/index.do", timeout=10000)

        # Ввод логина и пароля
        page.fill('input[name="login"]', 'Avtotest')
        page.fill('input[name="password"]', '123456')

        page.click('button[type="submit"]')
        expect(page.get_by_test_id("login-stage-auth").get_by_role("paragraph")).to_contain_text(
            "Неверный логин или пароль. Если не можете войти, восстановите доступ.")

        # Закрытие браузера
        browser.close()


is_sberbank_login_fail()