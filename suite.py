#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/9 14:44
# @Author  : GXl
# @File    : suite
import unittest

suite = unittest.TestSuite()
suite = unittest.TestLoader().discover('.',pattern='homework*.py')
runner = unittest.TextTestRunner()
runner.run(suite)