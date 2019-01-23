#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostTupleConan(base.BoostBaseConan):
    name = "boost_tuple"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_tuple"
    lib_short_names = ["tuple"]
    header_only_libs = ["tuple"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_static_assert",
        "boost_type_traits"
    ]


