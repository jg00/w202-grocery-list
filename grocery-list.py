
class ShoppingList:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.items = []

    def add_item_obj(self,item_obj):
        self.items.append(item_obj)


class Item:
    def __init__(self, title):
        self.title = title


def shopper_options():
    while True:
        
        option = input("Enter shopper option: c-create shopping list, q-exit, a-add to shopping list, v-view ")

        if option == "q":
            return option

        elif option == "c":
            list_name = input("Create shopping list: ")
            list_description = input("Shopping list description: ")
            shopping_list.append(ShoppingList(list_name, list_description))

        elif option == "a":
            list_name = input("Enter existing shopping list: ")

            shopping_list_id = -1
            for index in range(len(shopping_list)):
                if(shopping_list[index].title == list_name):
                    shopping_list_id = index

            if shopping_list_id >= 0:
                enterItems = True
                while enterItems:
                    item = input("Enter item (or x for other options): ")

                    if item != "x":
                        shopping_list[shopping_list_id].add_item_obj(Item(item))
                    else:
                        enterItems = False
            else:
                print("Shopping list does not exist")

        elif option == "v":
            for list in shopping_list:
                print(list.title)

                display_list = ""
                for index in range(len(list.items)):
                    display_list = display_list + list.items[index].title
                    if (index != len(list.items)-1):
                        display_list += ", "
                
                if display_list != "":
                    print(display_list)
                else:
                    print("no items in the list")
        else:
            print("Enter valid input")
        

shopping_list = []
while True:
    print("** Start grocery list app **")
    option = shopper_options()

    if (option == "q"):
        print("** End grocery list app **")
        break