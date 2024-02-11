#!/usr/bin/python3
"""Defines the CoreModel class."""
import models
from uuid import uuid4
from datetime import datetime


class CoreModel:
    """Represents the CoreModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new CoreModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the CoreModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy

    def __str__(self):
        """Return the print/str representation of the CoreModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
