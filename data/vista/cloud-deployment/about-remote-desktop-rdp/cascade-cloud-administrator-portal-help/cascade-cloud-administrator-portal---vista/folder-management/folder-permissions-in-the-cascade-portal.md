---
title: "Folder Permissions in the Cascade Portal | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/cascade-cloud-administrator-portal-help/cascade-cloud-administrator-portal---vista/folder-management/folder-permissions-in-the-cascade-portal"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/cloud-deployment/about-remote-desktop-rdp/cascade-cloud-administrator-portal-help/cascade-cloud-administrator-portal---vista/folder-management/folder-permissions-in-the-cascade-portal"
---

# Folder Permissions in the Cascade Portal

To better understand assigning folder permissions in the
 Cascade cloud admin portal, review defaults, types of permissions, and permission
 inheritance.

## Types of Permissions

You can assign users or groups
 different folder permissions, depending on their roles.

- Full
 Permissions: Users are allowed to rename the folder, add
 subfolders or files, and delete folder contents.

- Read
 Permissions: Users are only allowed to open and view
 contents of the folder. These permissions do not allow changes to the folder
 or its contents.

The Cascade portal also allows you to see the Current Windows Permissions that
 users or groups have for a particular folder. Updating the Full or Read permissions
 in Cascade updates these Windows permissions, unless they are highlighted in yellow
 text.
Windows permissions highlighted in yellow text cannot be
 modified in the Cascade portal. The Cascade portal allows you to view, delete, or re-add these permissions.

## Default Permissions

The default permissions assigned
 for any user or group added to the folder are Read Permissions only.
Each folder
 must have at least one user or group with permissions. If there is only one user
 or group for a particular folder, the delete icon will be disabled  (grayed out) and you will not be able to remove
 permissions for this user or group.

## Permission Inheritance

Folder permission is set at the highest folder level. Any
 subfolder inherits permissions from the folder above it.
It is *not* recommended that you change inherited
 permissions. However, if you do disable inheritance, you will see a
 Modify Inherited Permission popup with a confirmation
 message and must select Confirm to continue. Currently, disabling inherited permissions
 cannot be undone.
Folders
 with disabled inheritance have an asterisk ( *
 ) next to the folder name on the Folder Management page. You must set explicit permissions for these folders.
