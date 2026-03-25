---
title: "Field Definitions: DM Attachment Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/about-the-dm-attachment-detail-form/field-definitions-dm-attachment-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/document-management/dm-workflow/manage-documents/about-the-dm-attachment-detail-form/field-definitions-dm-attachment-detail-form"
---

# Field Definitions: DM Attachment Detail Form

The following is a list of field descriptions for the DM Attachment Detail form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## File Name

 Enter the network path of the file to attach. Optionally, click the browse button to search for the file. Once you select the file, the path displays in this field.

## Description

Enter a description of the document. The description can be up to 255 characters.

## Attachment Type

This field is used to associate the attachment with an attachment type.Enter an attachment type or press
 F4
 to select one from a list.
When
 F4
 is pressed, the Attachment Type Lookup opens. It displays only those attachment types that either are not secured or are types for which the user has security permissions assigned. See [VA Attachment Type Security ](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-attachment-type-security-form) for more information.
Note: This field will populate with a default attachment type if one was set up on the form that was used to access the Attachments Detail Form. Generally this is done to ensure that an attachment type is assigned and security is applied. For more information, see [Setting Default Attachment Types for Forms](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types/set-default-attachment-types-for-forms).
Attachment types are created and maintained using [DM Attachment Types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form).

## Create and Send Email Attachment

Check this box if the file that you are attaching should be included in the emails generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature in the PM module. If you do not check this box, the file will not display on the Attachments tab on the PM Send Documents form. Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for general information about the Create and Send feature.
This box is important because by default all attachments associated with a record are automatically included in any emails generated using the Create and Send feature. For example, you should not check this box if the attachment is an internal memo that contains confidential information.
Note: This checkbox is only enabled when accessing the DM Attachments form from a PM form with [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) functionality.

Related information

- [About the Create and Send Feature](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)
