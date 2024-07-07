# Otus Python QA Engineer project


## Описание проекта
Это учебный проект по тестированию web и api интерфейсов в рамках курса "Otus Python QA Engineer".

## Покрытие тестов
- 1.1 Тестами покрыты следующие API:
    - Google Classrooms (с ограничением - в какой-то момент стала срабатывать квота на количество сущностей со стороны Google и пришлось остановить разработку этих тестов)
    - Open Brewery API
    - Dog API
    - JSON Placeholder API
    Последние три API не позволяют создавать объекты на своей стороне, поэтому в основном это покрытие GET-методов.
- 1.2 Тестами частично покрыт функционал OpenCart со стороны Web-интерфейса


## Используемые технологии
- Selenium
- Requests
- Allure 
- Pytest
- Selenoid
- Docker
- Jenkins
- xdist
- PageObject pattern

## Опции запуска
- browser (браузер для запуска UI-тестов, по умолчанию Chrome)
- base_opencart_url (адрес интернет-магазина OpenCart, по умолчанию локально)
- log_level (уровень логирования в файл, по умолчанию DEBUG)
- executor (адрес Selenoid-сервера, по умолчанию локально)
- vnc (булевое значение TRUE или FALSE, индикатор включения VNC)
- video (булевое значение TRUE или FALSE, индикатор  записи видео)
- bv (версия браузера)
- remote (булевое значение TRUE или FALSE, индикатор запуска на Selenoid или в локальном браузере, по умолчанию FALSE)
- threads (количество потоков запуска)
 
## Автор
Elena Chuyan
