# Bitlink

## Описание работы скрипта:
Скрипт сокращает ссылку через сервис bit.ly, а при введении сокращенной ссылки выводит количество переходов по ней.

## Зависимости
Python3:
```
pip install -r requirements.txt
```
## Окружение
.env
```
BITLY_TOKEN=f80a43cd3c1c877df9ce7d7caf24b107df923b7b
```
## Запуск скрипта в консоли
```
python3 main.py https://developer.mozilla.org/ru/

# Вы увидите
$ python3 main.py https://developer.mozilla.org/ru/
Битлинк: https://mzl.la/3IIj6Yw

# Если указать короткую ссылку (Битлинк)
$ python3 main.py https://mzl.la/3IIj6Yw
По вашей ссылке прошли: 2
```
