## О проекте
Автотесты шаблон. Тесты написаны на Python c использованием следующих фреймворков:


1) Behave (test scenario - BDD)
2) Allure report (test report)


## Установка зависимостей проекта
###Выполнить следующие команды в терминале:

    pip3 install -r requirements.txt

## Локальный запуск тестов
###Выполнить следующие команды в терминале:

    behave -f allure_behave.formatter:AllureFormatter -o ./logs ./features --tags @smoke --no-logcapture --no-skipped
    allure serve ./logs
   
