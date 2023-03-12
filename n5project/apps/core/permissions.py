from n5project.apps.utils.permissions import generate_group_permission


class Group:
    PERSON_GROUP_NAME = 'person'
    OFFICER_GROUP_NAME = 'officer'

    person = generate_group_permission(PERSON_GROUP_NAME)
    officer = generate_group_permission(OFFICER_GROUP_NAME)
