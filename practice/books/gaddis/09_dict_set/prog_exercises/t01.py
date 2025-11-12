from datetime import time

auditories = {
    'CS101': 3004,
    'CS102': 4501,
    'CS103': 6755,
    'CS104': 1244,
    'CS105': 1411,
}
teachers = {
    'CS101': 'Хайнс',
    'CS102': 'Алъварадо',
    'CS103': 'Рич',
    'NТllO': 'Берк',
    'СМ241': 'Ли',
}

schedule = {
    'CS101': time(8),
    'CS102': time(9),
    'CS103': time(10),
    'NТllO': time(11),
    'СМ241': time(13),
}

info = auditories, teachers, schedule


def get_course_info(course_no: str) -> str:
    if not all(source.get(course_no, None) for source in info):
        return f'Данные по курсу "{course_no}" частично или полностью отсутствуют!'

    return (
        f'Номер курса:       {course_no}\n'
        f'Номер аудитории:   {auditories[course_no]}\n'
        f'Имя преподавателя: {teachers[course_no]}\n'
        f'Время проведения:  {schedule[course_no]}'
    )


print(get_course_info('CS101'), get_course_info('123'), sep='\n\n')
