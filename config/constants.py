#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/28 20:31
# @Author  : Tom

# 项目路径
import os

project_dir = os.path.abspath(os.path.join(__file__, "../.."))

class GlobalConfig:
    root_dir = os.path.abspath(os.path.join(project_dir, "../MMSA_datamodel"))
    data_root_dir = os.path.abspath(os.path.join(project_dir, "../MMSA_datamodel/Datasets"))
