class Field:
    def __init__(self, x, y):
        try:    
            self.x = int(x)
            self.y = int(y)
            self.error = ""
        except:
            self.field_mapping_error()
        if not isinstance(self.x, int) or not isinstance(self.x, int):
            self.field_mapping_error()
        
        self.probes = []
    
    def register_probe(self, probe):
        self.probes.append(probe)

    def field_mapping_error(self):
        self.error = "Xerpay, we have a problem! I couldn't map this field!"
        print(self.error)