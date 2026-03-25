---
title: "Set Default Attachment Types for Forms | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/set-default-attachment-types-for-forms"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/set-default-attachment-types-for-forms"
---

# Set Default Attachment Types for Forms

Once you have created attachment types using the DM Attachment Types form, you can set up default attachment types for forms in the system.
For example you can set up the PM Request For Information form so that attachments added using this form will automatically be assigned the PM RFI attachment type. This also adds an extra layer of security for sensitive documents in the event that a user forgets to assign an attachment type.
To set up a default attachment type on a form.

1. On a form that allows
 attached documents, select Tools >
 Form Properties. The Form Properties form displays.Note: You can also right-click the form and
 select Form Properties from the
 menu that displays.

1. If you are setting the default for your specific login, select the User tab and enter the attachment type in the User's Default Attachment Type field. You can press F4to select it from a list of attachment types.

1. If you are setting the default for the entire system, select the System Wide tab and enter the attachment type in the System Default Attachment Type field. Press F4 for a list of valid attachment types.

1. Click
 Close. Now when a document is added to
 this form, the system will automatically apply this attachment type to it.
 If you are attaching documents using the Attachment Detail form, the
 attachment type defaults in the
 Attachment Type
 field and you can change the setting. If you drag and drop a
 document to the form, the system automatically applies the attachment type
 to it.
Note: When adding a document that has a
 default attachment type, make sure that you have access to that attachment
 type or you will be unable to view the document. See [VA Attachment Type Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form) for more
 information.

Related information

- [Enable Attachment Type Security](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/enable-attachment-type-security)

- [Manage Attachment Types for Specific Documents](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/manage-attachment-types-for-specific-documents)

- [About Adding Documents](/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/about-adding-documents)

- [About the DM Attachment Detail Form](/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/about-the-dm-attachment-detail-form)

- [About the Form Properties form](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-form-properties-form)
