def run(program):
    # my eyes bleed at what I have wrought
    for key, value in program.items():
        if isinstance(value, dict):
            if value['op'] == 'add':
                s = 0
                for var in value['vars']:
                    s += program[var]
                program[key] = s

    return program
