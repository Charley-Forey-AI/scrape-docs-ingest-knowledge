---
title: "Copy Company Data | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/copy-company-data"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/copy-company-data"
---

# Copy Company Data

You can copy existing data from one company into a different company.
Copying company data is useful when setting up a test company based on your current 'live' setup or when a new company can make use of portions of data from an existing company, such as equipment files, fixed assets, company-specific user-defined fields, and so on.

- Proceed only when all users are logged out of all companies.

- To copy records, you need security level 9 on PA functions.

- Only fully posted transactions are eligible to be copied.

- The copy function copies all records in the files selected for the current company code, except those without an Info-Link name; these are files whose description doesn't start with //.

- During the time the copy process is running, do not perform any other activities in the application.

To copy the current company data to a new company:

1. Log in to the company you want to copy data from.

1. Go to System Administration > Utilities > Company Data Copy/Purge.

1. Select Copy data to another company.

1. Enter the Company code of the destination company.

1. Select files to copy:

- To copy files for a particular module, enter the Module name.

- To copy individual files, leave the module name blank and enter the File name.

- To copy ALL files, leave the Module and File name fields blank.

1. To also copy custom tables, select the Include custom files? checkbox.

1. To also copy all the installation settings to the new company code, select the Include installation settings checkbox.

1. Select Continue.The Edit Selection window opens. All the selected files to be copied appear in the grid.

1. Review the file list and edit it if needed. Remove any file from being copied by selecting it and selecting Delete.

1. To view the finalized list, select OK.

1. Confirm the warning messages to proceed with the copy process.

1. Select Continue.

1. Select OK.During the process, the number of files to be copied and which file is currently being copied display in the bottom left-hand corner of the page.

When the application has completed the process, it returns you to the Site Map page.
If you didn't opt to copy company settings in Step 7, log in to the destination company, go to System Administration > Installation > Properties, and complete the company information.
