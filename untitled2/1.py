

browser = webdriver.Firefox()
browser.get('https://www.coinichiwa.com')

browser.find_element_by_id("betFa").send_keys("0.00000005")
<input class="suggest__field ui-autocomplete-input ui-autocomplete-loading" type="search" autocomplete="off" name="q" placeholder="Найти вопрос, ответ, тег или пользователя" value="Selenium">