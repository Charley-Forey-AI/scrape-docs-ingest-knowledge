---
title: "Enable Attachment Type Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/enable-attachment-type-security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/enable-attachment-type-security"
---

# Enable Attachment Type Security

There are a number of steps to take to set up the system to
 enable attachment type security.
[Set up attachment types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types).
Use attachment type security to secure documents based on their associated attachment type. This allows you to restrict access to the HR Drug Test Results, HR Employment App, and other attachment types that are usually associated with documents that may contain sensitive information.To effectively secure an attachment type, you must apply security settings to it. This page covers the four components to making attachment type security work:

- Secure the attachment types

- Set up security groups

- Set up form security

- Grant access by attachment type to users and/or groupsYou or others in your organization may have already set up some of these components.

1. Secure the attachment
 types by selecting the Secured checkbox in the [DM Attachment Types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form) form.Note: By default, these attachment types are already secured:

- Audit reports attached using
 the HQ Batch Control form are assigned the HQ Sensitive attachment type.

- PR Ledger Update audit
 reports are assigned the PR Sensitive attachment type.

1. Set up security groups.Generally attachment type security isn't applied to specific users. Instead, we recommend that you set up security groups for attachment types and then apply security to those groups. For information on setting up security groups, see [VA Security Groups Form](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form).

1. Set up form security.Even though users may have access to an attachment type, to view documents
 associated with a data record, users must have permissions to the form which houses the data record. For
 example, a document may exist for a record in the AP Vendors form and have an associated
 attachment type named "AP". Any users which have access to the attachment type, but do
 not have access to the AP Vendors form, cannot view the document. For information on
 form security, see [VA Form Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form).

1. Set up attachment type security.For more information, see [VA Attachment Type Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form).

Related information

- [DM Attachment Types Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form)

- [Set Up Attachment Types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types)

- [About the HQ Batch Control Form](/en/vista/vista/administration/headquarters/batch-management/about-the-hq-batch-control-form)
