
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    # Find an index based on the letters in the name
    def hash_function(self, key):
        total = 0

        for letter in key:
            total += ord(letter)

        return total % self.size

    # Add a contact or update an existing one
    def insert(self, key, number):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                current.value.number = number
                return

            current = current.next

        contact = Contact(key, number)
        new_node = Node(key, contact)
        new_node.next = self.data[index]
        self.data[index] = new_node

    # Look for a contact using their name
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    # Show all the contacts stored in the table
    def print_table(self):
        for i in range(self.size):
            current = self.data[i]

            if current is None:
                print(f"Index {i}: Empty")
            else:
                print(f"Index {i}:", end=" ")

                while current is not None:
                    print(f"- {current.value}", end=" ")
                    current = current.next

                print()


# Test the contact management system
if __name__ == "__main__":
    table = HashTable(10)

    print("Empty Hash Table:")
    table.print_table()

    print("\nAdding Contacts:")
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\nSearching for John:")
    print("Search result:", table.search("John"))

    print("\nTesting Collisions:")
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()

    print("\nUpdating Rebecca's Number:")
    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    print("\nSearching for a Contact That Does Not Exist:")
    print("Search result:", table.search("Chris"))