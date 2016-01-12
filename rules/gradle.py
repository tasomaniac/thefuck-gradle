import re


def match(command):
    return re.search(r'Task \'(.+)\' not found in root project \'(?:.+)\'. Some candidates are: \'(.+)\'\.', command.stderr)


def get_new_command(command):
    p = re.search(r'Task \'(.+)\' not found in root project \'(?:.+)\'. Some candidates are: \'(.+)\'\.', command.stderr)
    original = p.group(1)
    canditate = p.group(2)
    return re.sub(original, canditate, command.script)

# Optional:
enabled_by_default = True

priority = 1000  # Lower first, default is 1000

requires_output = True
