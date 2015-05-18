from permission.logics import AuthorPermissionLogic, GroupInPermissionLogic
from permission.logics import CollaboratorsPermissionLogic


PERMISSION_LOGICS = (
	('cal.Event', AuthorPermissionLogic()),
	('cal.Event', GroupInPermissionLogic('Admin', 'Moderator', 'Member')),
	('cal.Entry', AuthorPermissionLogic()),
	('cal.Entry', GroupInPermissionLogic('Admin', 'Moderator', 'Member')),

)
