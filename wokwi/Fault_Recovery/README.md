# Embedded QA Wokwi Lab

Навчальний ESP32 IoT Controller для тем:
Sleep/Wake, Watchdog, fault injection, interrupted save, recovery, data integrity.

## Вміст
- `demo/` — демонстраційна firmware;
- `homework_buggy/` — навмисно забагована домашка;
- `requirements/` — очікувана поведінка;
- `templates/` — Test Matrix та Bug Report;
- `instructor/` — ключ із навмисними дефектами.

## Wokwi hardware
- ESP32 DevKit V1
- DHT22 → GPIO15
- Button → GPIO4
- LED → GPIO2
- Relay → GPIO5

## Запуск
У Wokwi створіть новий **ESP32 Arduino** project та замініть:
- `sketch.ino`
- `diagram.json`
- `libraries.txt`

файлами з `demo/` або `homework_buggy/`.

Serial: **115200 baud**

## CLI
```text
help
status
sensor
relay on
relay off
save
sleep 5
hang
powerloss
reboot
```

## Demo flow
```text
status
sensor
relay on
sleep 5
status
hang
status
powerloss
status
```

## Homework
Студент отримує `homework_buggy/`, requirements та templates.

Завдання:
1. System Overview.
2. Scope.
3. Мінімум 5 quality risks.
4. Test Matrix.
5. Sleep/Wake tests.
6. Watchdog fault injection.
7. Recovery tests.
8. Data integrity при `powerloss`.
9. Evidence.
10. Bug Reports.
11. Entry / Exit Criteria.
12. Test Summary / Case Study.

## Brown-out note
`powerloss` тут моделює **переривання запису + reboot**. Це не заміна реальної перевірки brown-out threshold, power rail timing та Flash/NVS поведінки на фізичному стенді.
