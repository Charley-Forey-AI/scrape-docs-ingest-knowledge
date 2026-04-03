---
title: "View Locked Database Tables | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/system-administration/administrator-utilities/view-locked-database-tables"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/system-administration/administrator-utilities/view-locked-database-tables"
---

# View Locked Database Tables

Use this screen to view the list of database tables that are currently locked.
Note: This page is applicable only if you have Enterprise Management security access (security category EM).
With each table listed, the application displays

- operator name, user id, and phone number

- logon time

- company name

If you encounter a record locked message, it's because another operator is using the record.
For example, if you were to attempt to access job 650 in Job File Maintenance while another operator was working in job 650, the application would block you from accessing the record.
If needed, and with the appropriate security access, you can determine the name of the operator currently using the record.
To view the information, select Block Info.
