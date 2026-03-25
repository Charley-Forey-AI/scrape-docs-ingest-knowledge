---
title: "Field Definitions: Initialize Security Access Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/initialize-security-access-form/field-definitions-initialize-security-access-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/initialize-security-access-form/field-definitions-initialize-security-access-form"
---

# Field Definitions: Initialize Security Access Form

The following is a list of field descriptions for the
 Initialize Security Access form in the Viewpoint Administration module. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Access Level

The Access Level field on the Initialize Security Access form.
Select the access level to apply to all entries in the grid. Depending on the form from which you accessed the Initialize Security Access form, there may be up to three access levels available:

- Allowed – Groups or users are allowed access to all items in the grid.

- None – Groups or users are allowed access to all items in the grid unless some other security setting states otherwise. For example, users might have an individual setting of None, but the group they belong to has a setting of Denied. In this case, users would be denied access to the items in the grid.

- Denied – Groups or users are denied access to all items in the grid.

Note: In regards to attachment security, even if a user has access to an attachment type, to view documents associated with a data record they must have appropriate permissions. For example, a document may exist for a record in AP Vendors and have an associated attachment type named "AP". If users have access to the attachment type, but do not have access to AP Vendors, they cannot view the document.

### Form Security

For form security, the options are slightly different.

- Full - If setting security by Form, grants access to all groups/users for the specified form. If setting security by Group or User, grants access to all forms for the specified group or user.

- None - If setting security by Form, does not set any specific access to all groups/users for the specified form. If setting security by Group or User, does not set any specific access to all forms for the specified group or user. Users are unable to access the forms unless some other security setting states otherwise.

- Denied - If setting security by Form, this denies access to all groups/users for the specified form. If setting security by Group or User, denies access to all forms for the specified group or user.

- Tab - Select this option to set up security on each tab on the form. For more information, see [Set Tab Security Access](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-tab-security-settings/set-tab-security-access).

Related information

- [Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings)

## Attachment Permissions

The Attachment Permissions section on the Initialze Security Access form (for VA Form
 Security).
Select the attachment permissions to apply to
 groups (or users) that are in the grid in VA Form Security.

- View Only – Allows users to only view attachments.

- Add – Allows group/user to add attachments to the specified form.

- Add, Edit – Allows group/user to add and edit attachments for the specified form.

- Add, Edit, Delete – Allows group/user to add, edit, and delete attachments for the specified form.

## Record Permissions

The Record Permissions section on the Initialize Security Access form (for VA Form
 Security).
Select the record permissions to apply to
 groups (or users) that are in the grid on VA Form Security. This will allow the group/user
 to add, update, and/or delete records to the specified form.
The system disables these checkboxes if you
 selected the Denied option from the Access Level
 section of the Initialize Security Access form.
This section has three setting options:

- Add – Use this option to allow users to add records to a form.

- Update – Use this option to allow users to edit form records.

- Delete – Use this option to allow users to delete form records.
