from mygroup import groupmates


def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(12), "Экзамены".ljust(40), "Оценки".ljust(20))
    for s in students:
        # убедитесь, что обращаемся к полю словаря через s["name"], а не просто name
        print(s["name"].ljust(15), s["surname"].ljust(12), str(s["exams"]).ljust(40), str(s["marks"]).ljust(20))


def avg(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def filter_by_avg(students, threshold):
    return [s for s in students if avg(s["marks"]) > threshold]


def main():
    print("Все студенты:\n")
    print_students(groupmates)

    try:
        threshold = float(input("\nВведите порог среднего балла (например, 4.0): ").strip())
    except Exception:
        print("Некорректный ввод. Используется значение 4.0")
        threshold = 4.0

    passed = filter_by_avg(groupmates, threshold)

    print(f"\nСтуденты со средним баллом > {threshold}:\n")
    if passed:
        print_students(passed)
    else:
        print("Нет студентов, подходящих под условие.")


if __name__ == "__main__":
    main()