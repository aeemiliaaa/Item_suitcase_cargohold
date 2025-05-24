# Write your solution here:
class Item:
    def __init__(self, name:str, weight:int):
        self.__name = name 
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, maximum_weight:int):
        self.maximum_weight = maximum_weight
        self.combined_weight = 0
        self.items = []

    def add_item(self, item:Item):
        if item.weight() + self.combined_weight  < self.maximum_weight:
            self.combined_weight += item.weight()
            self.items.append(item)

    def print_items(self):
        for x in self.items:
            print (x)

    def weight(self):
        return self.combined_weight

    def heaviest_item(self):
        if len(self.items) == 0:
            return None 
        else:
            heaviest = self.items[0] 
            for x in self.items:
                if x.weight() > heaviest.weight():
                    heaviest = x
            return heaviest
            
    def __str__(self):
        if len(self.items) == 1:
            return f"{len(self.items)} item ({self.combined_weight} kg)"

        else:
            return f"{len(self.items)} items ({self.combined_weight} kg)"


class CargoHold:
    def __init__(self, maximum_weight:int):
        self.maximum_weight = maximum_weight
        self.suitcases = []
        self.total = 0


    def add_suitcase(self, suitcase:Suitcase): 
        if suitcase.weight() + self.total  < self.maximum_weight:
            self.total += suitcase.weight()
            self.suitcases.append(suitcase)
            self.maximum_weight -= suitcase.weight()
        
    def print_items(self):
        for x in self.suitcases:
            x.print_items()
    
    def __str__(self):
        if len(self.suitcases) == 1:
            return f"{len(self.suitcases)} suitcase, space for {self.maximum_weight} kg"
        else:
            return f"{len(self.suitcases)} suitcases, space for {self.maximum_weight} kg"



if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()



