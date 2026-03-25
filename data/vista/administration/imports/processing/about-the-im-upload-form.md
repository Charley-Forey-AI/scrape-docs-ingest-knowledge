---
title: "About the IM Upload Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/processing/about-the-im-upload-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/processing/about-the-im-upload-form"
---

# About the IM Upload Form

This form is used to upload work file data into the appropriate system data files.
Files updated by the upload will be the same as those updated when posting transaction detail directly in the corresponding forms.
To start the upload process, specify the Import ID of the work file to upload and click the Update button. For direct imports, the work file is uploaded directly to the associated database table. For batch imports, the work file data is uploaded to the appropriate batch file (e.g. CMCE, EMBF, JCCB, MSTB, PRTB, etc). Access the batch in the appropriate form after the upload is complete and make any necessary adjustments before processing.
Note: Minimal validation is done during the upload process; however, any errors not caught during the upload will be caught during the normal batch validation process. If errors exist, either correct them or remove the record(s) from the batch.
Note: When uploading imported bank reconciliation data, you must initialize cleared entries from the import file (in CM Clear Initialize) before reviewing the data. For more information, see CM Clear Initialize in Related Topics below.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [About the IM Import Form](/en/vista/vista/administration/imports/processing/about-the-im-import-form)

- [About the IM Work Edit Form](/en/vista/vista/administration/imports/processing/about-the-im-work-edit-form)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

- [About the CM Clear Initialize Form](/en/vista/vista/accounting/cash-management/processing/reconciliation/about-the-cm-clear-initialize-form)

- [Import Types](/en/vista/vista/administration/imports/setup-and-maintenance/import-types)
