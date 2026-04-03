---
title: "Clean up Copied Data | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/clean-up-copied-data"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/clean-up-copied-data"
---

# Clean up Copied Data

Run a script in SSMS to easily prevent any potential issues arising from having copied data into a company.
Cleaning up copied data requires:

- access to Microsoft SQL Server Management Studio (SSMS)

- a SQL login that has read/write access to your database

- the contents of the *Company Copy
 Cleanup.sql* script, accessible by download from the [Viewpoint Customer Portal](https://support.viewpoint.com/s/)

- the company code of the company to which data was copied; this is the destination company, that is, the one being cleaned up

A consequence of copying data from a live/production company to a Test Company is that the dashboard and contacts may contain already contain some data. If this data is duplicated, issues with BI can arise in the Test Company.
To clean up your copied data and prevent these potential issues:

1. Using SQL Server Management Studio (SSMS), connect to the Spectrum database.

1. Select the Spectrum database and open a New Query window.

1. Copy the contents of the *Company Copy Cleanup.sql* script and paste it into the query window.

1. In the pasted text,

1. locate the `TST` placeholder,

1. delete it, and

1. replace it with the company code of the destination company.

1. Select Execute.
