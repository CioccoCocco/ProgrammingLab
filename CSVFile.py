class CSVFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        data = []
        with open(self.name, "r") as file:
            for line in file:
                data.append(line.strip().split(','))
            