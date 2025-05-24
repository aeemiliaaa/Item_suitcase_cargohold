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
            
    def __str__(self):
        if len(self.items) == 1:
            return f"{len(self.items)} item ({self.combined_weight} kg)"

        else:
            return f"{len(self.items)} items ({self.combined_weight} kg)"



if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")