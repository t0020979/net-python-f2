HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = {
  'today': [],
  'tomorrow': [],
  'later': []
}

run = True

while run:
  command = input("Введите команду: ")
  if command == "help":
    print(HELP)
  elif command == "show":
    print(tasks)
  elif command == "add":
    task = input("Введите название задачи: ")
    date = input("Введите дату задачи: ")
    if date == "Сегодня":
      index = "today"
    elif date == "Завтра":
      index = "tomorrow"
    else:
      index = "later"
    tasks[index].append(task)
    print("Задача добавлена на", index)
  elif command == "exit":
    break
  else: 
    print("Неизвестная команда")

print("Спасибо за использование! До свидания!")