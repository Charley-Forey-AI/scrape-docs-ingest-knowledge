---
title: "Imports Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/administration/imports-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r1/administration/imports-features"
---

# Imports Features

Vista 2021 R1 delivers on user-requested Imports enhancements, fixes, and other improvements.

## Added New Veteran Status to the HR Resource Master Import

In conjunction with changes made to the Veteran Status settings in HR Resource Master, a new ActiveDutyWartimeVetYN identifier (#466) was added to the HRResourceMaster (HR Resource Master) import. This new identifier defaults with the Overwrite Import Value, Use Viewpoint Default, and Update Column checkboxes set to No (unselected).
Note: Upon installation of this release, the new identifier and defaults will be added automatically to all existing templates referencing the HRResourceMaster import form.

## Added Ability to Export/Import IM Templates

To enable this functionality, a new Import/Export tab was added to the IM Templates form. A new field, Export\Import Template Directory, allows specifying the directory to use for exporting and importing templates. You will typically use a network shared directory so that others have access to the same location for importing and exporting templates. Once you define a location, it is saved and used by all templates.
When you export a template, the system saves the file to the specified directory. You can then access the file from another system using the Import option. New templates are automatically added to IM Templates. If the template already exists, you are given the option to overwrite the existing template.
For more information, see [Export / Import an IM Template](/en/vista/vista/administration/imports/setup-and-maintenance/export--import-an-im-template).

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
