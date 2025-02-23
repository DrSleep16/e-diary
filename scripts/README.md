# Скрипты для работы с данными школьной системы

Файл scripts.py содержит скрипты для работы с данными школьной системы. Скрипты предназначены для исправления оценок, удаления замечаний и создания похвал для учеников.

## Использование

### Исправление оценок

Скрипт `fix_marks` предназначен для исправления оценок учеников, заменяя низкие оценки на 5. Для запуска скрипта выполните:

```bash
fix_marks --student "Фамилия Имя" 
```

Где `"Фамилия Имя"` - имя и фамилия ученика, которому требуется исправить оценки.

### Удаление замечаний

Скрипт `remove_chastisements` позволяет удалить все замечания для указанного ученика. Для запуска скрипта выполните:

```bash
remove_chastisements --student "Фамилия Имя" 
```

Где `"Фамилия Имя"` - имя и фамилия ученика, для которого нужно удалить замечания.

### Создание похвалы

Скрипт `create_commendation` создает похвалу для ученика за указанный предмет. Для запуска скрипта выполните:

```bash
create_commendation --student "Фамилия Имя" --subject "Название предмета" --text "Текст похвалы"
```

Где `"Фамилия Имя"` - имя и фамилия ученика, `"Название предмета"` - название предмета, а `"Текст похвалы"` - текст похвалы.

## Замечания

- Перед использованием убедитесь, что у вас есть доступ к базе данных и указанные ученики, предметы и учителя существуют.
- В случае возникновения ошибок, проверьте правильность введенных данных и доступ к базе данных.
- Внесите необходимые изменения в скрипты в соответствии с вашими данными и требованиями.

**Обратите внимание:** Эти скрипты могут вносить изменения в базу данных. Пожалуйста, будьте осторожны при их использовании.