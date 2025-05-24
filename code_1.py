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



if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    suitcase.heaviest_item()


