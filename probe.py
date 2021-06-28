import operator

class Probe:
    def __init__(self, current_field):
        self.current_field = current_field
        self.w_r = ["E", "S", "W", "N"]
        self.modifiers = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.current_position = (0, 0)
        self.d = "N"
        self.error = ""

    def land(self, landing_point, direction):
        if (int(landing_point[0]) >= 0 and int(landing_point[0]) <= self.current_field.x) and (int(landing_point[1]) >= 0 and int(landing_point[1]) <= self.current_field.y):
            self.x = landing_point[0]
            self.y = landing_point[1]
            self.current_position = (int(landing_point[0]), int(landing_point[1]))
            if direction in self.w_r:
                self.d = direction
            else:
                self.error = "Invalid landing direction."
        else:
            self.error = "Out of bounds landing."

    def run_instructions(self, instruction):
        current_index = self.w_r.index(self.d)
        current_modifier = self.modifiers[current_index]
        agg_position = (0, 0)
        for i in instruction:
            current_index = self.w_r.index(self.d)
            if i == "M":
                agg_position = tuple(map(operator.add, agg_position, current_modifier))
            elif i == "L":
                if current_index > 0:
                    self.d = self.w_r[current_index - 1]
                    current_modifier = self.modifiers[current_index - 1]
                else:
                    self.d = self.w_r[-1]
                    current_modifier = self.modifiers[-1]
            elif i == "R":
                if current_index < 3:
                    self.d = self.w_r[current_index + 1]
                    current_modifier = self.modifiers[current_index + 1]
                else:
                    self.d = self.w_r[0]
                    current_modifier = self.modifiers[0]
            else:
                self.error = f"I couldn't understand you... what do you mean by {i}?"
                break;
        
        self.current_position = tuple(map(operator.add, agg_position, self.current_position))
    
    def read(self):
        if self.error == "":
            print((self.current_position[0], self.current_position[1], self.d))
        else:
            print(self.error)

    def __str__(self):
        if self.error == "":
            return f"{self.current_position[0]} {self.current_position[1]} {self.d}"
        return f"Xerpay, we have a problem! {self.error}"
        