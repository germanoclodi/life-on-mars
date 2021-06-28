import sys
from field import Field
from probe import Probe

def run():
    with open(sys.argv[1], 'r') as input_file:
        step = ""
        for line in input_file:
            if step == "land":
                probe = land(field, line)
                step = "obey"
            elif step == "obey":
                field = obey(field, probe, line)
                step = "land"
            else:
                field = map_field(line)
                if not field.error == "":
                    break
                step = "land"

            if "str" in line:
                break

    for probe in field.probes:
        print(probe)

def map_field(line):
    field_matrix = list(filter(lambda x: x != " ", line.split(" ")))
    field_matrix[-1] = field_matrix[-1].strip()
    field = Field(field_matrix[0], field_matrix[1])
    return field

def land(field, line):
    landing_positions = list(filter(lambda x: x != " ", line.split(" ")))
    landing_positions[-1] = landing_positions[-1].strip()
    probe = Probe(field)
    probe.land((landing_positions[0], landing_positions[1]), landing_positions[2])
    return probe

def obey(field, probe, line):
    if probe.error == "":
        instructions = list(line.strip())
        probe.run_instructions(instructions)
    field.register_probe(probe)
    return field

if (__name__ == "__main__"):
    run()