# Удаление из реестра случаев и персональных данных, соответствующих списку полисов

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Как работает?

Для работы нужен `python`

Необходимо приготовить 3 файла. Случаи - `IN_ZAP.xml`, персональные данные - `IN_PERS.xml`, список полисов для удаления - `polis.txt`

Далее:

```bash
python delRec.py IN_ZAP.xml IN_PERS.xml polis.txt
```

Результаты будут записаны в папке `out`
