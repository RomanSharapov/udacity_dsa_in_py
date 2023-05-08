#!/usr/bin/env python3


class Classy:
    """You can use this class to represent how classy someone
    or something is.
    "Classy" is interchangable with "fancy".
    If you add fancy-looking items, you will increase
    your "classiness".
    The following items have classiness points associated
    with them:
    "tophat" = 2
    "bowtie" = 4
    "monocle" = 5
    Everything else has 0 points.
    Use the test cases to guide you!"""

    def __init__(self):
        self.items = []

    def add_item(self, item: str) -> None:
        """This method adds items to the list"""
        self.items.append(item)

    def get_classiness(self) -> int:
        """This method calculates the "classiness"
        value based on the items."""
        classiness = 0
        classy_map = {
            "tophat": 2,
            "bowtie": 4,
            "monocle": 5,
        }
        for item in self.items:
            if item in classy_map:
                classiness += classy_map[item]

        return classiness
