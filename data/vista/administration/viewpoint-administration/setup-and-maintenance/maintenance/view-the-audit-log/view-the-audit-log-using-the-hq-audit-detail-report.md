---
title: "View the Audit Log Using the HQ Audit Detail Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log/view-the-audit-log-using-the-hq-audit-detail-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log/view-the-audit-log-using-the-hq-audit-detail-report"
---

# View the Audit Log Using the HQ Audit Detail Report

Whenever a user edits a record in most Vista forms, the system creates an audit record in the HQ Master Audit (HQMA) table. This information is useful to audit or track changes made to tables, such as the old value, new value, date of change, and the user who made the change.
You may also view the Audit log [using the VA Audit Log Viewer](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log/view-the-audit-log-using-the-va-audit-log-viewer-form).
To view a list of audit records using the HQ Audit Detail report:

1. Open the HQ Audit Detail report from the Reports subfolders in the Headquarters or Reports modules on the main menu.

1. On the Inputs tab, press F4 in the Company field to select from a list of companies. Leave the field blank for Viewpoint Administration (VA) tables. You can also leave the field blank to run a report for all companies. Some tables, like the AP Vendors and the AR Customer tables, will need this input to be the group from HQ Groups as there is no company stored in those tables.

1. In the Beginning Table Name and Ending Table Name fields, press F4 to select from a list of tables. You can run a report for all tables by leaving these fields blank, but this will result in a very long report.

1. In the Beginning Date and Ending Date fields, enter or select a date from the Calendar control.

1. To filter for specific users, press F4 in the Beginning User Name and Ending User Name fields. To filter for all users, leave these fields blank.

1. Run the report:

- Click Preview to see the report before printing or exporting.

- Click Print to open the Print dialog box so you can print the report.

- Click Export to open the RP Report Export Options dialog box so you can export the report.
