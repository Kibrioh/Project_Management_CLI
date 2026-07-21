"""
person.py

This module contains the Person class.

The Person class acts as the parent (base) class for the User class.
It stores common information that every user should have.

This follows the OOP principle of Inheritance.
"""


class Person:
    """
    Represents a generic person.

    Attributes
    ----------
    name : str
        The person's full name.

    email : str
        The person's email address.
    """

    def __init__(self, name: str, email: str):
        """
        Initialize a new Person object.

        Parameters
        ----------
        name : str
            The person's name.

        email : str
            The person's email.
        """

        # Store the name directly.
        self.name = name

        # Store email using the property setter.
        # This automatically validates the email before saving it.
        self.email = email

    # ----------------------------------------------------------
    # PROPERTY
    # ----------------------------------------------------------
    # A property allows us to control how an attribute is accessed.
    #
    # Instead of exposing _email directly,
    # users interact with "email".
    # ----------------------------------------------------------
    @property
    def email(self):
        """Return the person's email."""
        return self._email

    # ----------------------------------------------------------
    # SETTER
    # ----------------------------------------------------------
    # Every time someone assigns a value to email,
    #
    # person.email = "abc@gmail.com"
    #
    # this setter is executed automatically.
    #
    # It allows us to validate the email before storing it.
    # ----------------------------------------------------------
    @email.setter
    def email(self, value):
        """
        Validate the email before storing it.

        Raises
        ------
        ValueError
            If the email format is invalid.
        """

        # Very simple email validation.
        # Later we could improve this using regular expressions.
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address.")

        # Store the validated email.
        self._email = value

    # ----------------------------------------------------------
    # STRING REPRESENTATION
    # ----------------------------------------------------------
    # This method defines what gets printed when we do:
    #
    # print(person)
    #
    # instead of:
    #
    # <Person object at 0x....>
    #
    # we'll get something meaningful.
    # ----------------------------------------------------------
    def __str__(self):
        """Return a human-readable representation of the object."""
        return f"Name: {self.name} | Email: {self.email}"

    # ----------------------------------------------------------
    # SERIALIZATION
    # ----------------------------------------------------------
    # We first convert the object into a dictionary.
    #
    # Later:
    #
    # json.dump(person.to_dict())
    #
    # ----------------------------------------------------------
    def to_dict(self):
        """
        Convert the Person object into a dictionary.

        Returns
        -------
        dict
            Dictionary representation of the object.
        """

        return {
            "name": self.name,
            "email": self.email
        }

    # ----------------------------------------------------------
    # CLASS METHOD
    # ----------------------------------------------------------
    # A class method belongs to the class instead of an instance.
    # It allows us to recreate an object from a dictionary.
    # ----------------------------------------------------------
    @classmethod
    def from_dict(cls, data):
        """
        Create a Person object from a dictionary.

        Parameters
        ----------
        data : dict
            Dictionary containing person information.

        Returns
        -------
        Person
            A new Person object.
        """

        return cls(
            name=data["name"],
            email=data["email"]
        )