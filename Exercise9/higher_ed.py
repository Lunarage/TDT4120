# !/usr/bin/python3
# coding=utf-8


class Institution:
    def __init__(self, name):
        self.name = name
        self.parent = self


class HigherEdSolver:

    def initialize(self, institutions):
        self.institutions = {}
        for institution in institutions:
            inst = Institution(institution)
            self.institutions[institution] = inst

    def parent_institution(self, institution):
        inst = self.institutions[institution]
        if inst.parent != inst:
            inst.parent = self.institutions[self.parent_institution(
                inst.parent.name)]
        return inst.parent.name

    def fuse(self, institution1, institution2, new_institution):
        inst1 = self.institutions[institution1]
        inst2 = self.institutions[institution2]
        new_inst = Institution(new_institution)
        inst1.parent = new_inst
        inst2.parent = new_inst
        self.institutions[new_institution] = new_inst
