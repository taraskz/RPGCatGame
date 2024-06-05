class Inventory:
    def __init__(self):
        '''This function creates a backpack to store items'''
        self.backpack = {}
        self.inventory_file = 'inv.txt'

    def pickup_inventory(self, item):
        '''This function allows items to be picked up and stored'''
        self.backpack[item] = True

    def view_inventory(self):
        print("In backpack: ")
        for item in self.backpack:
            print(f"- {item}")
    
    def export_inventory(self):
        '''Creates the inventory'''
        try:
            with open(self.inventory_file, 'w') as f:
                for item in self.backpack:
                    f.write(item + '\n')
        except:
            print("Something went wrong :(")

    def read_inventory(self):
        '''This function prints out the inventory'''
        try:
            with open(self.inventory_file, 'r') as f:
                for line in f:
                    item = line.strip()
                    self.backpack[item] = True
        except:
            print("Something went wrong :(")
        
        
        