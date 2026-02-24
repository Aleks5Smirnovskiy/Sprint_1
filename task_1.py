time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

parts = time_string.split(',')

total_minutes = 0

for part in parts:
    # Убираем лишние пробелы по краям
    chunk = part.strip()

    # Инициализируем значения
    hours = 0
    minutes = 0
    seconds = 0

    # Если есть часы
    if 'h' in chunk:
        # Берём подстроку до 'h'
        h_str = chunk.split('h')[0]
        hours = int(h_str)
        # Убираем этот фрагмент из строки
        chunk = chunk.replace(h_str + 'h', '').strip()

    # Если есть минуты
    if 'm' in chunk:
        # Берём подстроку до 'm'; она может начинаться после пробела
        # Например: ' 45m' или '25m'
        m_part = chunk.split('m')[0].strip()
        minutes = int(m_part)
        chunk = chunk.replace(m_part + 'm', '').strip()

    # Если есть секунды
    if 's' in chunk:
        s_part = chunk.split('s')[0].strip()
        seconds = int(s_part)

    # Переводим всё в минуты
    total_minutes += hours * 60 + minutes + seconds // 60

print(total_minutes)