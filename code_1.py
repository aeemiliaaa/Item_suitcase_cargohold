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
        self.total = 0
        self.items = []

    def add_item(self, item:Item):
        if item.weight() + self.total  < self.maximum_weight:
            self.total += item.weight()
            self.items.append(item)
            
    def __str__(self):
        if len(self.items) == 1:
            return f"{len(self.items)} item ({self.total} kg)"

        else:
            return f"{len(self.items)} items ({self.total} kg)"



if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(5)
    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)