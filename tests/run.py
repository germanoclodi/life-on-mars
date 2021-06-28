import life_on_mars


def test_invalid_file_mapping_1():
    file_line_list = []
    with open("./tests/test_input_files/invalid_file_field_mapping_1.txt", "r") as input_file:
        for line in input_file:
            file_line_list.append(line)

    field = life_on_mars.map_field(file_line_list[0])

    assert field.error == "Xerpay, we have a problem! I couldn't map this field!"


def test_invalid_file_mapping_2():
    file_line_list = []
    with open("./tests/test_input_files/invalid_file_field_mapping_2.txt", "r") as input_file:
        for line in input_file:
            file_line_list.append(line)

    field = life_on_mars.map_field(file_line_list[0])

    assert field.error == "Xerpay, we have a problem! I couldn't map this field!"


def test_invalid_file_probe_direction():
    file_line_list = []
    with open("./tests/test_input_files/invalid_file_probe_direction.txt", "r") as input_file:
        for line in input_file:
            file_line_list.append(line)

    field = life_on_mars.map_field(file_line_list[0])
    probe = life_on_mars.land(field, file_line_list[1])

    assert probe.error == "Invalid landing direction."

def test_invalid_file_probe_position():
    file_line_list = []
    with open("./tests/test_input_files/invalid_file_probe_position.txt", "r") as input_file:
        for line in input_file:
            file_line_list.append(line)

    field = life_on_mars.map_field(file_line_list[0])
    probe = life_on_mars.land(field, file_line_list[1])

    assert probe.error == "Out of bounds landing."


def test_invalid_file_probe_movement():
    file_line_list = []
    with open("./tests/test_input_files/invalid_file_probe_movement.txt", "r") as input_file:
        for line in input_file:
            file_line_list.append(line)

    field = life_on_mars.map_field(file_line_list[0])
    probe = life_on_mars.land(field, file_line_list[1])
    life_on_mars.obey(field, probe, file_line_list[2])

    assert probe.error == "I couldn't understand you... what do you mean by X?"

def test_valid_file():
    file_line_list = []
    with open("./tests/test_input_files/valid_file.txt", "r") as input_file:
        for line in input_file:
            file_line_list.append(line)

    field = life_on_mars.map_field(file_line_list[0])
    probe = life_on_mars.land(field, file_line_list[1])
    life_on_mars.obey(field, probe, file_line_list[2])

    assert probe.__str__() == "1 3 N"