# Project:          Module 8 - Example 1
# Description:      Class definition for Tennis Champions
# Demonstrates:     Sets
# Developed By:     LV
# Date:             October 2025

# Python Set - From Gemini

# A set is an unordered collection of unique, immutable elements. 
# Unordered: The elements in a set do not have a defined order, and you cannot access them by index.
# Unique: A set automatically discards duplicate elements; each element in a set must be distinct.
# Mutable (the set itself): You can add or remove elements from a set after it has been created.
# Immutable Elements: The individual elements within a set must be immutable data types (e.g., numbers, strings, tuples). Lists or dictionaries, which are mutable, cannot be directly stored as elements within a set.
# Creating Sets:
# Sets can be created using curly braces {} (for non-empty sets) or the set() constructor (for empty sets or from an iterable).

class Tennis_Champions:

    # initializer

    def __init__(self, wimbledon, us_open):
        
        self.wimbledon_champs = set(wimbledon)
        self.us_open_champs = set(us_open)
        
    # instance methods to demo set processing and functions

    def common_functions_methods(self):

        #print original sets
        
        print("Original sets")
        print()
        print(self.wimbledon_champs)
        print()
        print(self.us_open_champs)
        print()
        
        # copying a set
        
        wimbledon_copy = self.wimbledon_champs.copy()
        us_open_copy = set(self.us_open_champs)
        
        #print copied sets
        
        print("Copied sets")
        print()
        print(wimbledon_copy)
        print()
        print(us_open_copy)
        print()

        # adding elements to a set

        wimbledon_copy.add("Monica Seles")
        us_open_copy.update(["Simona Halep", "Caroline Wozniacki", "Jelena Jankovic"])
        
        # print after adding elements
        
        print("After adding elements")
        print()
        print(wimbledon_copy)
        print()
        print(us_open_copy)
        print()

        # removing/discarding elements from a set

        wimbledon_copy.remove("Monica Seles") # raises an exception if item is not found
        us_open_copy.discard("Simona Halep") # does not raise an exception if item is not found
                             
        us_open_copy.difference_update(["Caroline Wozniacki", "Jelena Jankovic"])
        
        # print after removing/discarding elements
        
        print("After removing elements")
        print()
        print(wimbledon_copy)
        print()
        print(us_open_copy)
        print()

        # clear all elements in a set

        wimbledon_copy.clear()

        # print after clearing elements

        print("After clearing elements")
        print()
        print(wimbledon_copy)
        print()
    
        # using for loop to iterate through a set

        for player in us_open_copy:
            print(player)

    # finding the union of two sets
    
    def find_union(self):

        all_champs = self.wimbledon_champs.union(self.us_open_champs)

        # all_champs = self.wimbledon_champs | self.us_open_champs  # alternatively, the | operator can be used  

        print("Players who have won Wimbledon or US Open")
        print()
        print(all_champs)
        print()
    
    # finding the intersection of two sets

    def find_intersection(self):

        champs_of_both = self.wimbledon_champs.intersection(self.us_open_champs)

        # champs_of_both = self.wimbledon_champs & self.us_open_champs  # alternatively, the & operator can be used  

        print("Players who have won Wimbledon and the US Open")
        print()
        print(champs_of_both)
        print()

    # finding the difference of two sets

    def find_difference(self):

        wimbledon_only = self.wimbledon_champs.difference(self.us_open_champs)

        # wimbledon_only = self.wimbledon_champs - self.us_open_champs  # alternatively, the - operator can be used  

        print("Players who have won only Wimbledon")
        print()
        print(wimbledon_only)
        print()

        us_open_only = self.us_open_champs.difference(self.wimbledon_champs)

        # us_open_only = self.us_open_champs - self.wimbledon_champs  # alternatively, the - operator can be used  

        print("Players who have won only the US Open")
        print()
        print(us_open_only)
        print()
    
    # finding the symmetric difference of two sets

    def find_symmetric_difference(self):

        wimbledon_or_us_open = self.wimbledon_champs.symmetric_difference(self.us_open_champs)

        # wimbledon_or_us_open = self.wimbledon_champs ^ self.us_open_champs  # alternatively, the ^ operator can be used  

        print("Players who have either won Wimbledon or the US Open but not both")
        print()
        print(wimbledon_or_us_open)
        print()

    # finding subsets and supersets
    
    def find_super_sub_sets(self):

        all_champs = self.wimbledon_champs.union(self.us_open_champs)

        print("Is all_champs (union of Wimbledon and US Open champs) a superset of Wimbledon Champs?")
        print()
        print(all_champs.issuperset(self.wimbledon_champs)) # alternatively, all_champs >= self.wimbledon_champs
        print()

        print("Is US Open Champs a subset of all_champs (union of Wimbledon and US Open champs)?")
        print()
        print(self.us_open_champs.issubset(all_champs)) # alternatively, self.us_open_champs <= all_champs
        print()

    # set comprehension
    
    def set_comprehension(self):

        williams = {item for item in self.wimbledon_champs if "Williams" in item}

        print("A set of players named Williams extracted from the Wimbledon Champs set")
        print()
        print(williams)