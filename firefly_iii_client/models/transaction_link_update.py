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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TransactionLinkUpdate(BaseModel):
    """
    TransactionLinkUpdate
    """ # noqa: E501
    inward_id: Optional[StrictStr] = Field(default=None, description="The inward transaction transaction_journal_id for the link. This becomes the 'is paid by' transaction of the set.")
    link_type_id: Optional[StrictStr] = Field(default=None, description="The link type ID to use. Use this field OR use the link_type_name field.")
    link_type_name: Optional[StrictStr] = Field(default=None, description="The link type name to use. Use this field OR use the link_type_id field.")
    notes: Optional[StrictStr] = Field(default=None, description="Optional. Some notes. If you submit an empty string the current notes will be removed")
    outward_id: Optional[StrictStr] = Field(default=None, description="The outward transaction transaction_journal_id for the link. This becomes the 'pays for' transaction of the set.")
    __properties: ClassVar[List[str]] = ["inward_id", "link_type_id", "link_type_name", "notes", "outward_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TransactionLinkUpdate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionLinkUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inward_id": obj.get("inward_id"),
            "link_type_id": obj.get("link_type_id"),
            "link_type_name": obj.get("link_type_name"),
            "notes": obj.get("notes"),
            "outward_id": obj.get("outward_id")
        })
        return _obj


