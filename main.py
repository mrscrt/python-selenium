from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Путь к веб-драйверу (замените путь на свой)
WEBDRIVER_PATH = '/path/to/your/webdriver'

# Функция для выполнения поиска в Google
def google_search(search_query):
    # Инициализируем веб-драйвер (замените 'chrome' на 'firefox', если используете Firefox)
    driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH)
    
    # Открываем Google
    driver.get('https://www.google.com')
    
    # Находим поле поиска и вводим запрос
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(search_query)
    
    # Выполняем поиск (нажимаем Enter)
    search_box.send_keys(Keys.RETURN)
    
    # Чтобы не закрывалось сразу окно, раскомментируйте следующую строку:
    # input('Press Enter to close the browser...')
    
    # Закрываем браузер после выполнения поиска
    driver.quit()

# Пример использования
search_query = 'OpenAI GPT-3'
google_search(search_query)
