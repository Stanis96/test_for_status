class TreeStore:
    def __init__(self, items):
        self.items = items

    @property
    def getAll(self):
        return self.items

    def getItem(self, id):
        for item in items:
            if item["id"] == id:
                return item

    def getChildren(self, parent):
        new_items = []
        for item in self.items:
            if item["parent"] == parent:
                new_items.append(item)
        return new_items

    def getAllParents(self, child):
        new_items1 = []

        def getParent(parent, new_items2):
            for item_ in new_items2:
                if item_["id"] == parent:
                    new_items1.append(item_)
                    getParent(item_["parent"], new_items2)
                    break

        for item in self.items:
            if item["id"] == child:
                getParent(item["parent"], self.items)
        return new_items1


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None},
]
ts = TreeStore(items)

if __name__ == "__main__":
    print(ts.getAll)
    print(ts.getItem(7))
    print(ts.getChildren(4))
    print(ts.getChildren(5))
    print(ts.getAllParents(7))
