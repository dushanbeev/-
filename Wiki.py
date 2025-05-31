from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера (Chrome)
driver = webdriver.Chrome()

try:
    # 1. Открыть Wikipedia
    driver.get("https://www.wikipedia.org")

    # 2. Найти поле поиска
    search_input = driver.find_element(By.NAME, "search")

    # 3. Ввести запрос
    search_input.send_keys("Python (programming language)")

    # 4. Нажать Enter
    search_input.send_keys(Keys.RETURN)

    # 5. Явное ожидание: заголовок страницы должен появиться
    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )

    # ✅ Проверка: заголовок содержит нужный текст
    assert "Python (programming language)" in heading.text

    print("Тест пройден успешно!")

finally:
    # Закрыть браузер
    driver.quit()
