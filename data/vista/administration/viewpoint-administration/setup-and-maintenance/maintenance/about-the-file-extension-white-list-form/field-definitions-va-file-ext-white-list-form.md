---
title: "Field Definitions: VA File Ext White List Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-file-extension-white-list-form/field-definitions-va-file-ext-white-list-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/about-the-file-extension-white-list-form/field-definitions-va-file-ext-white-list-form"
---

# Field Definitions: VA File Ext White List Form

The following is a list of field descriptions for the VA File
 Ext White List form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Upload Type

Upload Type field on the VA File Extension Allow List form.

For each of the three types of upload, you can specify which types of file type extensions the system should allow when users attempt to upload. Press F4 to select one of these:

- Auto Import

- Document Templates

- Crystal Reports

## Allow No File Extension

Allow No File Extension checkbox on the VA File Extension
 Allow List form.
Consider the potential risk to your network if you select this checkbox. Only select it if you know of a specific need to upload files without an extension.

## FileExtension

FileExtension field on the VA File Extension Allow List form.

Displays the currently allowed extensions for what's shown in the Upload Type field.
If you need to allow upload of a file type not already in the list, add a new record and specify the extension.
If you need to modify an existing default record (those with IsStandard checkbox selected), delete the default record and create a new record reflecting the needed changes.
When you upgrade to a new version, the system:

- retains any records you have added or changed

- re-instates any default records you have delete

Note:

For network security reasons, best practice is to not augment this list except for when and if a file type that is not on the list needs to be uploaded.

## Description

Description field on the VA File Extension Allow List form.

Optionally add a description or note. Your entry appears here only.

## IsStandard

IsStandard field on the VA File Extension Allow List form.

This field is disabled and is informational only. It indicates whether records were added during the installation process (checkbox is selected) or were added by a user (checkbox is not selected).
You can delete records that appear by default, but the system will re-instate any deleted records each time you upgrade to a new version.
