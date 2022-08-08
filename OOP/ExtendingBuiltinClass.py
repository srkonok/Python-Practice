class Text(str):
    def duplicate(self):
        return self+self
class TrackableList(list):
    def append(self,called):
        print("Append Called!")
        super().append(object)


# text=Text("Python!")
# print(text.duplicate())#Python!Python!

list1= TrackableList()  
list1.append("1")

