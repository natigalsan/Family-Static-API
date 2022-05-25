
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": last_name,
            "age": "33 Years Old",
            "Lucky_numbers": [7, 13, 22]
        }, {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": last_name,
            "age": "35 Years Old",
            "Lucky_numbers": [10, 14, 3]
            
        }, {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": "5 Years Old",
            "Lucky_numbers": [1]
        }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return


        pass

    def delete_member(self, id):
        # fill this method and update the return
        
        one_members = FamilyStructure.query.get(id).self._members()
        pass

    def get_member(self, id):
        # fill this method and update the return
        members = jackson_family.get_all_members()
        one_members = FamilyStructure.query.get(id).self._members()

        return jsonify({"resultado": one_members})

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        # esta función ME devuelve todos los miembros iniciales de la familia Jackson
        return self._members
