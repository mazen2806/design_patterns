import copy


# Prototype pattern allows you to create new objects by cloning existing objects,
# without needing to know their specific classes.
class Computer:
    def __init__(self, hdd, ram):
        self.hdd = hdd
        self.ram = ram

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"HDD: {self.hdd}  RAM: {self.ram}"


if __name__ == "__main__":
    c1 = Computer("500 GB", "2 GB")
    c2 = c1.clone()
    c2.ram = "3 GB"
    print(c1)
    print(c2)

