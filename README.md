# Stepik-3.6

Перед запуском тестов обязательно установите нужные зависимости, т.к. я использую Selenium 4:

- pip install -r requirements.txt

В тесте *test_present_button_add_to_basket* в соответствии с заданием Вам необходимо добавить команду time.sleep(30).

В тесте *test_present_button_add_to_basket_with_expected_conditions* уже проводится проверка с неявным ожиданием

Запустить тесты в терминале можно командной: 
-pytest -v --tb=line test_items.py

Также Вы можете изменить язык и браузер, добавив в команду выше --browser_name=crome и --language=fr (дефолтный браузер FireFox, язык - русский)
