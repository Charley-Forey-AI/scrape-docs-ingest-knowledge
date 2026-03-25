---
title: "Set Security for Attachment Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/set-security-for-attachment-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/set-security-for-attachment-types"
---

# Set Security for Attachment Types

Use the VA Attachment Type Security form to set security for attachment types.
This is useful when certain documents are confidential, and you do not want all users to have access. For example, you could restrict access to the HR Drug Test Results, HR Employment App, and other attachment types that are usually associated with documents that may contain sensitive information.
Note: Even though users may have been given access to an attachment type, to view documents that are attached to a data record, those users must have permissions to view the record in the form. See [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form) for giving users access to forms.
Assign security for all users prior to allowing them access to the system. It is recommended that you assign security to groups of users. Then, if desired, you can customize individual user settings. These access levels are available for attachment type security access:

- Allowed – Use this option to grant access for the specified attachment type.

- None – This option does not set any specific access to the attachment type. It is most commonly used at the user level to defer security to the group level.

See [VA Security Groups](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form) and [About the Interaction Between Group and User Level Security Settings](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/interaction-between-group-and-user-level-security-settings) to learn more.
To set security for attachment types:

1. In the [DM Attachment Types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form) form, confirm that the Secured box is checked for the attachment types to which you want to apply security settings. You can set up security on only these secured attachment types.

1. Open the VA Attachment Type Security form.

1. In the Attachment Type field, either:

- Enter the attachment type for which to set up security, or press F4 for a list of attachment types

- Leave this field blank to set up security on all attachment types

1. In the Company section, select to filter by either a Select Company or Across All Companies.

- If you selected Select Company, enter the company number in the text box, or press F4 to select from a list of companies. If you do not see a company in this list, you may not have been granted form security permissions to administer attachment type security for that company.

- If you do not have security permissions for all companies, the all-companies option displays as Across Companies I have permissions for. For more information, see [Company](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form/field-definitions-va-attachment-type-security-form#ID-00047feb--en).

1. In the Group/User section, select to filter by either Security Group or User.

- If you selected Security Group, enter a specific group in the text box, or leave it blank to filter by all groups.

- If you selected User, enter a specific user in the text box, or leave it blank to filter by all users.

1. Click the Refresh button. The system displays all records matching the filter criteria in the grid.Note: The grid displays only secured attachment types (the
 Secured box in DM Attachment Types is checked).

1. Set access levels:

- To set access levels for individual records: In the grid , use the drop-down in the Access column to set the access level for each attachment type.

- To set the same access level for all records: Click Initialize Access Level. In the [Initialize Security Access](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/initialize-security-access-form) form, select an option in the [Access Level](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/initialize-security-access-form/field-definitions-initialize-security-access-form#ID-000490e9--en) section and click Apply. The Initialize Security Access form closes, and all records in the VA Attachment Type Security grid display the same access level.

Note: By default, attachment security is set up on the following:
Note:

- Audit reports attached using the HQ Batch Control form are assigned the HQ Sensitive attachment type.

- PR Ledger Update audit reports are assigned the PR Sensitive attachment type.

Note: Users needing access to these must be given access to the HQ Sensitive and PR Sensitive attachment types.

1. In the VA Attachment
 Type Security form, click the Apply button. A message
 displays stating that the system updated query security successfully. Note: If you set attachment type security for
 security groups, and then need to customize an individual user, repeat the
 above steps with filtering by that user and then changing the access level
 appropriately for individual attachment type.

Related information

- [Enable Attachment Type Security](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/enable-attachment-type-security)

- [VA Attachment Type Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form)

- [DM Attachment Types Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form)

- [Attachment Form/DM Stand Alone Documents](/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/attachment-formdm-stand-alone-documents)

- [DM Manage Attachments](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/dm-manage-attachments)

- [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form)

- [VA User Profile Form](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form)

- [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form)
