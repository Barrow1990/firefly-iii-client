# coding: utf-8

"""
    Firefly III API Client

    This is the Python client for Firefly III API

    The version of the OpenAPI document: 2.1.0
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class BillRepeatFrequency(str, Enum):
    """
    How often the bill must be paid.
    """

    """
    allowed enum values
    """
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    QUARTERLY = 'quarterly'
    HALF_MINUS_YEAR = 'half-year'
    YEARLY = 'yearly'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of BillRepeatFrequency from a JSON string"""
        return cls(json.loads(json_str))


