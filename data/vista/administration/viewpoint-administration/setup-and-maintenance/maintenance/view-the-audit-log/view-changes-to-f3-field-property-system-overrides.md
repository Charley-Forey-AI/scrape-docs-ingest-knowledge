---
title: "View Changes to F3 Field Property System Overrides | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log/view-changes-to-f3-field-property-system-overrides"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log/view-changes-to-f3-field-property-system-overrides"
---

# View Changes to F3 Field Property System Overrides

Administrators can track system-wide changes to field property
 (F3) overrides and the users who made these changes. F3 changes are audited and recorded in
 the HQ Master Audit (HQMA) table. Admins can use this data to help determine why form or
 field behaviors changed.
Note: These are system-wide changes and
 are not company or user-specific.

View this data in the HQ Audit Detail report or by accessing the HQMA database using
 SQL Server Management Studio. To see the changes in the HQ Audit Detail report,
 complete the following steps:

1. From the Vista main menu, go to Headquarters > Reports > HQ Audit Detail.

1. In the HQ Audit Detail Report Launcher, enter the following values in the
 fields:

1. Company: 0

1. Beginning Table Name: DDFIc

1. Ending Table Name: DDFIc

1. Enter values in the remaining fields as
 desired, or leave blank to include all entries.

1. To see the report, select Preview,
 Print, or Export.

For the date range selected, you can see the changes in
 fields across all users and companies, along with the old value, new value, and date and
 time of each change.
