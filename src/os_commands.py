from src.base_command import BaseCommand


class OsCommands(BaseCommand):
    @staticmethod
    def users():
        return BaseCommand.cmd_run(["awk", "-F:", "{print $1}", "/etc/passwd"])

    @staticmethod
    def total_procs():
        return len(BaseCommand.cmd_run(["ps", "aux"]))

    @staticmethod
    def user_processes(user):
        lines = BaseCommand.cmd_run(["ps", "-U", user])
        return lines

    @staticmethod
    def total_memory_used():
         lines = BaseCommand.cmd_run(["free", "-m"])
         return lines[1].split()[2]

    @staticmethod
    def total_cpu_used()-> float:
        lines = BaseCommand.cmd_run(["ps", "-eo", "%cpu", "--no-headers"])
        return round(sum([float(line) for line in lines]), 1)

    @staticmethod
    def get_max_mem_proc_name():
        lines = BaseCommand.cmd_run(["ps", "-eo", "command", "--sort=-%mem", "--no-headers"])
        return lines[0][:20]

    @staticmethod
    def get_max_cpu_proc_name():
        lines = BaseCommand.cmd_run(["ps", "-eo", "command", "--sort=-%cpu", "--no-headers"])
        return lines[0][:20]

