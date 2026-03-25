---
title: "About the IM Auto Import Profile Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-auto-import-profile-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-auto-import-profile-setup-form"
---

# About the IM Auto Import Profile Setup Form

Use this form to set up a profile that the system will refer to when automatically importing data files into the database from locations that you specify.
For information on how to set it up, see [About Importing Files Automatically](/en/vista/vista/administration/imports/setup-and-maintenance/about-importing-files-automatically).
When you place data files in the directories you have specified in the profile, the system performs the following actions:

1. Checks the directory, detects the file, and adds it to a queue for processing.

1. Processes your data files one at a time and inserts the data from those files into your Vista database.

1. If the import process succeeds, moves the original data file from the pickup directory and places it in the archive directory.

1. If the import process fails or encounters errors, preserves the original data file in the error directory.

1. Creates a record of the import process (success or failure) and stores it in the log directory you specified.
