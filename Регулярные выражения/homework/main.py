import re
import csv

PHONE_PATTERN = r'(\+7|8)\s*\(?(\d{3})\)?[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})\s*(\(?(доб\.?)\s*(\d+)\)?)?'
PHONE_SUB = r'+7(\2)\3-\4-\5 \7\8'


def format_phone(phone):
    """Приводит телефон к стандартному формату"""
    if not phone:
        return ""
    phone = re.sub(PHONE_PATTERN, PHONE_SUB, phone).strip()
    # Убираем лишние пробелы вокруг "доб."
    phone = re.sub(r'\s*доб\.?\s*', ' доб.', phone)
    return phone


def process_contacts(contacts):
    """Обрабатывает и объединяет контакты"""
    unique = {}
    for contact in contacts:
        # Разбиваем ФИО на отдельные компоненты
        parts = " ".join(contact[:3]).split()
        last, first = parts[0], parts[1]
        patronymic = parts[2] if len(parts) > 2 else ""

        key = (last, first)
        if key not in unique:
            unique[key] = [last, first, patronymic] + contact[3:]
        else:
            # Объединяем недостающие данные
            for i in range(2, 7):
                if not unique[key][i] and contact[i]:
                    unique[key][i] = contact[i]

        # Форматируем телефон
        unique[key][5] = format_phone(unique[key][5])

    return list(unique.values())


# Чтение и обработка данных
with open("phonebook_raw.csv", encoding="utf-8") as f:
    contacts = list(csv.reader(f))

processed = process_contacts(contacts)

# Запись результатов
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(processed)