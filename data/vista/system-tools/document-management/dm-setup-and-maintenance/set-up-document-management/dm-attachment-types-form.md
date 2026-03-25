---
title: "DM Attachment Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form"
---

# DM Attachment Types Form

Use this form to create and maintain attachment types.
Attachment types allow you to group types of documents together, set security, and determine document retention settings. When storing documents in Vista, you may find it useful to assign attachment types to them.
 Vista comes with a number of standard attachment types that you can use. They have these functions:

- They are a high-level way of grouping and organizing related documents, for example AP invoices, payroll time cards, and project documents like RFIs, RFQs, and transmittals.

- They can be used to establish security. You can use attachment type security to set up security on documents based on the associated attachment type. For example, this allows you to restrict access to the HR Drug Test Results, HR Employment App, and other attachment types that are usually associated with documents that may contain sensitive information. For more information, see [Enable Attachment Type Security](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/enable-attachment-type-security).

- They can be used to set up expiration dates on certain kinds of documents. For example if your organization accumulates a lot of invoices, you can have the system purge invoices that are older than a certain date.

You can also create and maintain custom attachment types that meet your organization's needs.

## Status

The Status for each attachment type is assigned automatically and cannot be changed. The system assigns a status to each attachment type as follows:

- Standard - All attachment types provided by Vista are assigned this status.

- Custom - This type is assigned to all attachment types that you manually set up.

- Override - This type is only applied to Standard attachment types that you have modified. For example, if you update the retention time on a standard attachment type and then save the record, the system automatically changes the status from Standard to Override.

## Deleting Attachment Types

 You can only delete attachment types with a status of Custom or Override, as long as they are not currently associated with documents.
Note: If you delete an attachment type with a status of Override, the attachment type reverts back to the standard settings and the status changes back to Standard.

For information more about using this form, click the links below.
[Set Up Attachment Types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types)

Related information

- [Enable Attachment Type Security](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/enable-attachment-type-security)

- [Set Default Attachment Types for Forms](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/set-default-attachment-types-for-forms)

- [Manage Attachment Types for Specific Documents](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/manage-attachment-types-for-specific-documents)

- [Set Up Attachment Types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types)
