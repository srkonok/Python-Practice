class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        # self.tags[tag]=self.tags.get(tag,0)+1
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
# cloud.add("Python")
# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.__tags) #AttributeError: 'TagCloud' object has no attribute '__tags'

print(cloud.__dict__)
print(cloud._TagCloud__tags)
