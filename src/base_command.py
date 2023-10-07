from subprocess import run


class BaseCommand():
    def cmd_run(command: [str], capture_output=True, text=True)-> list[str]:
        result = run(command, capture_output=capture_output, text=text)
        return result.stdout.strip().split("\n")
