import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.links import Links
from config.data import Data

"""
Фикстура для инициализации драйвера Chrome с использованием Options для запуска браузера с определенными опциями 
для запуска тестов в ci 
"""
@pytest.fixture(autouse=True, scope="function")
def driver_1(request):

    options = Options()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.media_stream_camera": 1})

    driver_1 = webdriver.Chrome(options=options)

    request.cls.driver_1 = driver_1 # Для создания объекта драйвера внутри тестовых классов (тестов)
    yield driver_1
    driver_1.quit()

"""  
Здесь дополнительно можно расписать различные фикстуры для быстрого вополнения в тестах, например фикстурудля авторизации,
фикстуры для подготовки среды перед выполнением тестов и возвращения ее в исходное состояние после выполнения тестов. 
"""
