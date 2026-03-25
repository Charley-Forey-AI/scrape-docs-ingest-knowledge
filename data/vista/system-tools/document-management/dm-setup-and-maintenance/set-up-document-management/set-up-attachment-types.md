---
title: "Set Up Attachment Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types"
---

# Set Up Attachment Types

The following instructions detail how to create custom attachment types, but you can also use these instructions to modify existing, standard attachment types.
You can set up and maintain attachment types using the [DM Attachment Types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form) form.

1. From the DM Attachment
 Types form, enter New, N,
 or + in the Attachment Type
 ID field. The system creates a new attachment type and
 automatically assigns it the next available number.Note: Custom attachment types are assigned IDs
 that are greater than 50,000 to distinguish them from standard attachment
 types.

1. Enter a name for the attachment type in the Name field.

1. Enter a description for the attachment type in the Description field.

1. Enter the number of months that documents of this type should be retained in the Retention Time field. When you use the [DM Expired Documents Purge](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/dm-maintenance/about-the-dm-expired-documents-purge-form) form to purge documents, only documents older than the length of time set up here will be purged. For example enter 60 into this field if these attachments should be included in the DM Expired Documents Purge process once they are more than 60 months old. If you leave this field blank, documents will not be purged.

1. If you want to set security for the attachment type, check the Secured box.

1. Save the record. Once you save the record, the system sets the Status field to Custom.Note: There are three possible statuses: Standard (attachment type that came standard with the application), Override (a standard attachment type that has been customized), Custom (this is an attachment type that you have created).

1. Set security for the attachment type, if necessary. For more information, see [VA Attachment Type Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form).

1. Once you have created or modified an attachment type, you can set up default attachment types on the forms in the system. For more information, see [Setting Default Attachment Types for Forms](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/set-default-attachment-types-for-forms).
