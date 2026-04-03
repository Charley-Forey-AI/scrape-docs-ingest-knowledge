---
title: "Create a Test Company | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company"
---

# Create a Test Company

Create a set of company data whose purpose is to provide a way for testing without affecting data in the production company.
A set of company data which is separate from your live data can be useful for testing purposes. To obtain this separate set of data (a test company), you can make a copy of the data in your live company.

- Creating a test company is not a substitute for a backup. It excludes some data from and modifies some copied data in the destination company.Note: If your Spectrum environment is on premises, have your DBA or qualified IT obtain a backup by running the SQL job Spectrum – Full Backup, which is part of the SQL maintenance plan that was set up with Spectrum.

- Do not use this utility to change the company code.

- Make sure the drive that contains the Spectrum database and SQL transaction log files has enough free disk space for your live company and two additional copies of the database and transaction logs.Note: If your Spectrum environment is hosted by Trimble Viewpoint, you can check on your disk space by displaying the Drive Space Dashboard. This will show the total size of your Spectrum server and how much drive space remains available.

- The destination company may either be a new company or an existing company. If you want to reuse a company code, purge the data from it before using it again as the destination company.

- The user performing the Company Data Copy function must have full access (level 9) on all company tables and must have a SQL login with read/write access to the SQL database.Note: If your Spectrum application is hosted by Trimble Viewpoint, you can get read/ write access by requesting the SQL Credential Authorization form from Support.

- You must have access to the Viewpoint Customer Portal so you can [download required SQL scripts](https://support.viewpoint.com/s/knowledgedetail?c__urlname=How-can-I-use-Company-Copy-to-create-a-test-company).

The process of copying a company includes these main steps:

1. In SQL Server Management Studio (SSMS), and using a SQL script, temporarily [disable audit triggers](/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/disable-or-enable-audit-triggers).

1. Choose one, depending on whether the destination company already exists:

- [Create a new test company](/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/create-a-new-company).

- [Purge data from an existing test company](/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/purge-company-data).

1. [Copy company data](/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/copy-company-data) into the test company.

1. [Enable audit triggers](/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/disable-or-enable-audit-triggers) using a SQL script in SSMS.

1. In SSMS, and using a SQL script, [clean up copied data](/en/spectrum/spectrum/system-administration/administrator-utilities/create-a-test-company/clean-up-copied-data).

You can now use the newly created company for testing purposes. The data it contains is similar to the data in your live company as of the moment you made the copy.
