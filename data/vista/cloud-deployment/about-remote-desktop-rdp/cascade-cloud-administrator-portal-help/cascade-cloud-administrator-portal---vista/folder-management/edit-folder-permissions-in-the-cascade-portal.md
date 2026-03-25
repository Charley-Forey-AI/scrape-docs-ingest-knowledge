---
title: "Edit Folder Permissions in the Cascade Portal | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/cascade-cloud-administrator-portal-help/cascade-cloud-administrator-portal---vista/folder-management/edit-folder-permissions-in-the-cascade-portal"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/cascade-cloud-administrator-portal-help/cascade-cloud-administrator-portal---vista/folder-management/edit-folder-permissions-in-the-cascade-portal"
---

# Edit Folder Permissions in the Cascade Portal

You can edit which users or groups have access to a
 folder.
You can assign users or groups
 different folder permissions, depending on their roles.

- Full
 Permissions: Users are allowed to rename the folder, add
 subfolders or files, and delete folder contents.

- Read
 Permissions: Users are only allowed to open and view
 contents of the folder. These permissions do not allow changes to the folder
 or its contents.

The default permissions assigned
 for any user or group added to the folder are Read Permissions only.
Folders
 with disabled inheritance have an asterisk ( *
 ) next to the folder name on the Folder Management page. For more information, see the article on [Folder Permissions in the Cascade Portal](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/cascade-cloud-administrator-portal-help/cascade-cloud-administrator-portal---vista/folder-management/folder-permissions-in-the-cascade-portal).

1. Select
 the folder icon  to open the Folder
 Management page.

1. For the folder you want to edit, select the edit
 icon  to open the Permissions Management page.

1. In the Current Permissions section, enter the
 permissions for the user or group you want to edit.

1. Click into either a Modify Full
 Permissions or Modify Read
 Permissions cell.A dropdown arrow displays.

1. Select the dropdown and choose Yes or No, depending on the
 permissions you want to assign.

1. Click anywhere outside the cell to set the
 change.You will see the changed permissions labeled as
 Pending.
Note: If the Current
 Windows Permissions are highlighted in yellow text, you cannot
 modify in these permissions in the Cascade portal. You can only
 view, delete, or re-add these permissions.

1. To commit the changes, select Save Changes.You should see a confirmation message indicating that the
 permissions updated successfully. Notice that the Current Windows
 Permissions automatically update after you save changes.

1. If you attempt to change inherited permissions (not recommended), you will see
 a message that says Modify
 Inherited Permissions. If you want to disable inheritance, you
 must select Confirm to
 continue. For more information about permission inheritance, see the
 article on [Folder Permissions in the Cascade Portal](/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/cascade-cloud-administrator-portal-help/cascade-cloud-administrator-portal---vista/folder-management/folder-permissions-in-the-cascade-portal).

Note: Selecting Yes for Full Permissions
 automatically changes Read Permissions to Yes.Selecting No for
 either Full Permissions *or* Read
 Permissions automatically removes all permissions for that user or
 group.
