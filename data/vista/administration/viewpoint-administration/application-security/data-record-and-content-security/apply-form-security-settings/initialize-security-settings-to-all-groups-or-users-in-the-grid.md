---
title: "Initialize Security Settings to All Groups or Users in the Grid | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings/initialize-security-settings-to-all-groups-or-users-in-the-grid"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings/initialize-security-settings-to-all-groups-or-users-in-the-grid"
---

# Initialize Security Settings to All Groups or Users in the Grid

If you want to set the same security level for all groups or
 users in the grid at once, you can use the initialization feature.
If you re-initialize settings for all users, any
 modifications previously made to individual users will be changed to match that of all
 users.The following instructions
 detail how to initialize the same security settings to all items in the
 grid.

1. In VA Form Security,
 filter for the appropriate records. For more information, see [Filtering the VA Form Security Grid](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings/filtering-the-va-form-security-grid).  When you click the Refresh
 Grid button, the Initialize Access Level
 button becomes available.Important: Be very careful to filter
 information correctly before initializing. When you click the Initialize
 Access Level button, the system changes all records in the
 grid, not just the ones that are visible.

1. Click Initialize
 Access Level. The Initialize Security Access form opens

1. In the Initialize
 Security Access form, select an access level option from the Access
 Level section of the form.

1. In the Record
 Permissions section, check all appropriate permissions checkboxes (Add, Update, and/or Delete). When you select a box, users are able to perform that
 action on the forms in the grid.

1. In the Attachment
 Permissions section, select an option (View Only, Add, Add, Edit, or Add, Edit,
 Delete).

1. Click OK. The Initialize Security Access form closes, and all groups and
 users now display the specified access level and record permissions in the VA
 Form Security grid. Note: If you selected the Tab access level, only forms with multiple tabs are
 affected. The access level for all other forms does not change from its
 initial state. For more information on setting Tab security, see [Applying Tab Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-tab-security-settings).

1. Change the access level
 or permissions in the grid for specific users or groups as necessary. For more
 information, see [Manually Assign Security to Each Group or User](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/apply-form-security-settings/manually-assign-security-to-each-group-or-user).

1. Click the Apply button. The system updates group and user security
 settings.

1. If desired, click the
 Refresh Grid button again to clear the grid. Note: If you deny access to a form, its icon is grayed out in
 the associated module’s Programs folder and is inaccessible to the user. To
 hide or view inaccessible forms, users can select View > Display Accessible Items Only from the Main Menu toolbar.
