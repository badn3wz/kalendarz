from permission.logics import AuthorPermissionLogic, GroupInPermissionLogic
from permission.logics import CollaboratorsPermissionLogic


PERMISSION_LOGICS = (
	('playerprofile.UserProfile', AuthorPermissionLogic()),
)
