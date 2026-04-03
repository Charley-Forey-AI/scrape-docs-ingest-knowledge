---
title: "Purge Company Data | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/purge-company-data"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/purge-company-data"
---

# Purge Company Data

Purge records from a given test company in preparation for copying a new set of records to the same test company.
You can also purge records outside the context of a test company, such as records you don't need to retain anymore in your live company. Follow these same steps.

- Proceed only when all users are logged out of all companies.

- To purge records, you need security level 9 on PA functions.

- Only fully posted transactions are eligible to be purged.

- The purge function purges all records in the files selected for the current company code, except those without an Info-Link name; these are files whose description doesn't start with //.

- During the time the purge process is running, do not perform any other activities in the application.

- There is no undo function to retrieve purged records. If this function is accidentally run on your live data, the only recourse is to restore the files from backup.Note: If your Spectrum environment is on premises, have your DBA or qualified IT obtain a backup by running the SQL job Spectrum – Full Backup, which is part of the SQL maintenance plan that was set up with Spectrum.

 To purge Test Company records:

1. In the Test Company, go to System Administration > Utilities > Company Data Copy/Purge.

1. Select Purge data from this company.

1. Select files to purge:

- To purge files for a particular module, enter the Module name.

- To purge individual files, leave the module name blank and enter the File name.

- To purge *all* files, leave the Module and File name fields blank.

1. To also purge custom tables, select the Include custom files? checkbox.

1. Select Continue.The Edit Selection window opens. All the selected files to be purged appear in the grid.

1. Review the file list and edit it if needed.

1. To view the finalized list, select OK.

1. Confirm the warning messages to proceed with the purge process:

1. Select Continue.

1. Select OK.

During the process, the number of files to be purged and which file is currently being purged display in the bottom left-hand corner of the page.

When the application has completed the process, it returns you to the Site Map page.
If you're purging this company's data in preparation for copying new data into it, proceed with [Copy Company Data](/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/copy-company-data).
