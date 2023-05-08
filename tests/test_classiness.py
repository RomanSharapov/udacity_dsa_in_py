#!/usr/bin/env python3

from ..classy import Classy


def test_add_item():
    classy = Classy()
    classy.add_item("tophat")
    classy.add_item("bowtie")
    classy.add_item("monocle")
    classy.add_item("shoes")
    assert classy.items == ["tophat", "bowtie", "monocle", "shoes"]


def test_get_classiness():
    classy = Classy()
    classy.add_item("tophat")
    classy.add_item("bowtie")
    classy.add_item("monocle")
    classy.add_item("shoes")
    assert classy.get_classiness() == 11

    classy = Classy()
    classy.add_item("shoes")
    classy.add_item("shirt")
    assert classy.get_classiness() == 0

    classy = Classy()
    classy.add_item("tophat")
    classy.add_item("monocle")
    assert classy.get_classiness() == 7
