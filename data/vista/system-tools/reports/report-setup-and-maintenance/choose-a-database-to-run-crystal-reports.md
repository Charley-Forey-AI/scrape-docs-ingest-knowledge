---
title: "Choose a Database to Run Crystal Reports | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/report-setup-and-maintenance/choose-a-database-to-run-crystal-reports"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/report-setup-and-maintenance/choose-a-database-to-run-crystal-reports"
---

# Choose a Database to Run Crystal Reports

For cloud-hosted Vista customers running Crystal Reports, use
 the RP Report Titles form to choose which database your reporting data comes from: the main
 transactional database or the replica Vista Enterprise Database.
In order for this
 feature to work, your organization must have successfully set up the secondary Vista
 Enterprise Database. Note: The Vista
 Enterprise Database is a secondary reporting database only available to cloud-hosted
 customers who have purchased the setup. To learn more about this offering, contact
 your account representative.

1. From the Vista main menu, go to Reports > Programs > RP Report Titles.

1. Choose a Crystal report from the grid or enter the Report
 ID.If you don't make any selections, this report will run against the reporting
 database. In most scenarios, this is what you want. Running reports against
 the reporting database allows you to continue using Vista to complete other
 processes, as generating the report does not interfere with the main
 transactional Vista database.

1. To do real-time reporting on the most up-to-date data, you need to run the
 report against the primary transactional Vista database. On the Info tab, select
 the Transactional Report checkbox.This checkbox is selected by default for payroll batch or
 check printing process reports and batch reporting process reports. For
 non-Crystal reports, this checkbox is grayed out and disabled. For more
 information, see the Field Definition Help for this checkbox: [Transactional Report](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/about-the-rp-report-titles-form/field-definitions-rp-report-titles-form#concept-c081cb86-ee46-43ee-bf5f-6380451d0827--en).

1. Save the record.
