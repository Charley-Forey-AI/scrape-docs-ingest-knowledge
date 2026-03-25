---
title: "Export / Import an IM Template | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/export--import-an-im-template"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/export--import-an-im-template"
---

# Export / Import an IM Template

You can export and import templates in IM Templates to enable
 copying templates between systems.
Exporting a template from one system and importing
 from another eliminates the need to "recreate" a template from scratch in the
 destination system. You can also use this feature to update an existing template on one
 system that was modified on another system.The following details
 how to export and import a template in IM Templates.

Set up the Export/Import directory

1. In IM Templates, enter any template in the
 Template field.


1. Click the Import/Export tab.

1. In the Export\Import Template Directory field, enter the directory to use for exporting and importing templates. This will typically be a network share directory to
 enable others to access the file for importing. The system saves the specified
 directory and defaults it for all templates.

Export a
 template

1. In the Template field,
 enter the template to export.

1. Click the Import/Export tab.

1. Click Export.The system saves the file to the specified directory as "template
 name.xml" (for example, if the value in the Template field is "AP
 Invoice", the file name will be "AP Invoice.xml").

Import a Template

1. In the Template field,
 enter a template.You can enter any template here. The system automatically
 recognizes whether the imported template is new or existing, and will import the
 template appropriately (that is, either add it or provide a prompt to overwrite
 the existing template).

1. Click the Import/Export tab.

1. Click Import.The Open window displays, defaulting the directory indicated in the
 Export\Import Template
 Directory field.

1. Select the template to import and click Open.If the template is new, the system adds it automatically. If the
 template already exists, you are prompted to overwrite the file. If you select
 Yes, the system overwrites the existing template. If
 you select No, you are returned to Import/Export
 tab.

1. Review and edit the template as needed.
