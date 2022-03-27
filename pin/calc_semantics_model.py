#!/usr/bin/env python

# CAVEAT UTILITOR
#
# This file was automatically generated by TatSu.
#
#    https://pypi.python.org/pypi/tatsu/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.

from __future__ import annotations

from typing import Any
from dataclasses import dataclass

from tatsu.objectmodel import Node
from tatsu.semantics import ModelBuilderSemantics


@dataclass(eq=False)
class ModelBase(Node):
    pass


class CALCModelBuilderSemantics(ModelBuilderSemantics):
    def __init__(self, context=None, types=None):
        types = [
            t for t in globals().values()
            if type(t) is type and issubclass(t, ModelBase)
        ] + (types or [])
        super(CALCModelBuilderSemantics, self).__init__(context=context, types=types)


@dataclass(eq=False)
class Add(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None


@dataclass(eq=False)
class Subtract(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None


@dataclass(eq=False)
class Multiply(ModelBase):
    left: Any = None
    op: Any = None
    right: Any = None


@dataclass(eq=False)
class Divide(ModelBase):
    left: Any = None
    right: Any = None