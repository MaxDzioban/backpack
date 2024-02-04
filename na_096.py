#на 0.96
"""implement corresponding classes before the test_backpack_module function"""
class Item:
    '''class item'''
    def __init__(self,name,weight,value) -> None:
        '''init'''
        self.name=name
        self.weight=weight
        self.value=value
    def __repr__(self) -> str:
        '''repr name, weight, value'''
        return f"{self.name}"
    def __str__(self) -> str:
        '''str name, weight, value'''
        return f"{self.name} ({self.weight} kg, ${self.value})"

class Backpack:
    '''class Backpack'''
    _items=[]
    total_weight=0
    total_value=0
    __capacity = 10
    def __init__(self) -> None:
        pass
    def __str__(self) -> str:
        '''str about backpack'''
        if not self.items:
            return "Backpack contains 0 item with total weight 0 kg and total value $0"
        if len(self._items) == 1:
            return f"Backpack contains {len(self._items)} item wi\
th total weight {self.total_weight} kg and total value ${self.total_value}"
        return f"Backpack contains {len(self._items)} items wi\
th total weight {self.total_weight} kg and total value ${self.total_value}"

    @classmethod
    def add_item(cls, item):
        """add_item"""
        if isinstance(item, (str,int)):
            return 'Item is not valid'
        if cls.total_weight + item.weight <= cls.__capacity:
            cls._items.append(item)
            cls.total_weight += item.weight
            cls.total_value += item.value
            return "Object added!"
        return f"Item '{item.name}' is too heavy for the backpack."

    @classmethod
    def set_capacity(cls, new_value_for_setting):
        """set_capacity"""
        cls.__capacity = new_value_for_setting
        cls.total_weight = 0
        cls.total_value = 0

    @property
    def items(self):
        """return info about items"""
        return self._items
    @items.setter
    def items(self, new_items):
        """items_setter"""
        self._items = []
        self.total_value = 0
        self.total_weight = 0
        for elem in new_items:
            if isinstance(elem, Item):
                if self.total_weight + elem.weight <= self.__capacity:
                    self.total_weight += elem.weight
                    self._items.append(elem)
                    self.total_value += elem.value
    @items.deleter
    def items(self):
        """items deleter"""
        self._items = []

    @staticmethod
    def is_item_valid(item_name):
        '''is_item_valid'''
        return item_name in Backpack._items

    @classmethod
    def remove_item(cls, rem_elem):
        '''remove_item'''
        if rem_elem in cls._items:
            cls._items.remove(rem_elem)
            cls.total_weight -= rem_elem.weight
            cls.total_value -= rem_elem.value
            return "Object succesfully removed."
