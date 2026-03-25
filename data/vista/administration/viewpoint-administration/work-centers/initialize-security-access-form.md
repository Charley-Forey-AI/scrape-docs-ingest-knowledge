---
title: "Initialize Security Access Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/work-centers/initialize-security-access-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/work-centers/initialize-security-access-form"
---

# Initialize Security Access Form

Use this form to set access levels for all users/groups listed in a security form's grid.
 You can access this form by clicking the Initialize Access Level button from the following security forms in the VA module:

- VA Attachment Type Security

- VA Form Security

- VA Inquiry Security

- VA Report Security

- VA Security Administration

- VA Work Center Security

 Access Level settings are available for all security forms listed above, and determine what data users/group can access. Filter options control whether the selected access level is applied to items in the grid for a specific company or across all companies, and for a selected group or a specific user.
The following describes the access levels for each of the security forms.
VA Attachment Type SecuritySets access levels to determine what attachment types (defined in DM Attachment Types) users or groups can access. This in turn affects the documents the user or group can access. For example, if you allow access to attachment type "AP Invoice", the user or group will have access to all documents that are assigned that attachment type. However, the user or group must also have access to the associated data record. For example, if an attachment with an AP Invoice type is assigned to a vendor record (in AP Vendors), but the user or group does not have access to AP Vendors, they cannot view the attachment.VA Form SecuritySet access levels to determine what forms or specific tabs within a form users or groups can access. In addition, you can set attachment and record permissions for forms. Access levels and permission settings work together to establish form security for users or groups; form access levels determine whether a user can access a form, while record and attachment permissions determine how you can interact with the form's data or associated attachments.VA Inquiry SecuritySets access levels to determine what queries users or groups can access.VA Report SecuritySet access levels to determine what reports users or groups can access. This includes audit reports that are accessed during batch processing in a module. It is important to note that users who have access to batch processing forms do not automatically have access to the related audit reports. It is recommended that users who will be processing batches be given access to the related audit reports.VA Security AdministrationIf you are using this feature (that is, the Enable Security Administration checkbox is selected in VA Site Settings), you will use the access levels restrict a user's security administrator permissions to administering security in only specific company/module combinations in VA Form Security and VA Report Security.VA Work Center SecuritySet access levels to determine what work center templates users or groups can access.

Related information

- [About the VA Inquiry Security Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form)
