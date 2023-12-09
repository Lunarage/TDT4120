#!/usr/bin/python3
# coding=utf-8


def resolve_and_install(package):
    if package.is_installed:
        return
    for dependency in package.dependencies:
        resolve_and_install(dependency)
    install(package)


class Package:
    def __init__(self, dependencies, is_installed_func):
        self.__is_installed_func = is_installed_func
        self.__dependencies = dependencies

    @property
    def dependencies(self):
        return self.__dependencies

    @property
    def is_installed(self):
        return self.__is_installed_func(self)

    def __str__(self):
        return str(
            {
                "is_installed": self.is_installed,
                "dependencies": self.dependencies,
            }
        )

    def __repr__(self):
        return str(self)