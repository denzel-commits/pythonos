from src.os_commands import OsCommands
from src.utilities import save_log


if __name__ == "__main__":
    commands = OsCommands()
    contents = ""

    total_procs = commands.total_procs()
    data = f"Процессов запущено: {total_procs}"

    memory_used = commands.total_memory_used()
    data += "\n" + f"Всего памяти используется: {memory_used} Mb"

    cpu_used = commands.total_cpu_used()
    data += "\n" + f"Всего CPU используется: {cpu_used}%"

    max_mem_process = commands.get_max_mem_proc_name()
    data += "\n" + f"Больше всего памяти использует: {max_mem_process}"

    max_cpu_process = commands.get_max_cpu_proc_name()
    data += "\n" + f"Больше всего CPU использует: {max_cpu_process}"

    users = commands.users()
    data += "\n" + f"Пользователи системы: {','.join(users)}"

    data += "\n" + "Пользовательских процессов:"
    for user in users:
        procs_count = len(commands.user_processes(user))
        data += "\n" + f"{user}: {procs_count}"

    print(data)
    save_log(data)
