---
title: "Import Estimate Data | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/import-estimate-data"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/import-estimate-data"
---

# Import Estimate Data

You can import estimate data from a third-party application into Project Management using the PM Import Estimates Data form.
Before you import your data files, make sure that it is ready for import. Verify the following:

- That the file is comma separated

- That the leading number on each line is associated with a record type. Record types are maintained using [About the PM Import Estimates Detail Form](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-detail-form).

1. From the main menu, select Project Management > Programs > PM Import Estimates > Import Data.The PM Import Estimates Data form displays.

1. In the Template field, click Browse and then locate and select the import data file.

1. In the Import ID field, enter an ID for this import or press F4 to select an existing import ID.Important: If you select an existing import ID, the system replaces all data in the work files for that import with the new data. You should only use an existing import ID if the data is no longer valid or needed.

1. In the Enter Default Retainage Percent field, enter the retainage

 percent to assign to contract items and subcontract detail.

1. Click Import.

The system imports the data into a temporary work file. A message displays showing the

 total item, phase, cost type, material, and subcontract records imported, along with any errors found. If errors were found, you must correct the errors using the PM Import Edit form. Note: If no errors were found, you can upload your data without having to review the work files. However, it is recommended that you review your import data to ensure your data is correct.
