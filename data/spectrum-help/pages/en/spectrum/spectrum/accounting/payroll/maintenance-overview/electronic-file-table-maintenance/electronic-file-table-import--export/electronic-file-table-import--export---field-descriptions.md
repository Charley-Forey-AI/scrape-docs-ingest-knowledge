---
title: "Electronic File Table Import / Export - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-file-table-import--export/electronic-file-table-import--export---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-file-table-import--export/electronic-file-table-import--export---field-descriptions"
---

# Electronic File Table Import / Export - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Transfer type
Select the transfer type you wish to perform. Additional fields become accessible based on your selection here.

Export

Table
Enter a table code to import or export (based on the Transfer type specified above), use the SuperSelect options,or double-click on this field to select from a list of available table codes.
This field is enabled only if the Export transfer type is selected. Master table codes, as set up in Electronic Master File Maintenance, can be selected for transfer. If this field includes one or more master tables, then the update will include the master header and list of Payroll electronic file tables that comprise the master table, and all setup for the electronic files assigned within the master file.

File name
Enter a file name to export, or press Enter to accept the default (PRTABLES.OUT in the Spectrum data directory or, if the External file processing option is selected in the Company Installation screen, the default directory is the operator's local print directory, C:\SPECTRUM).

Import

Overwrite existing tables?
Select this checkbox if you want to overwrite existing tables during the import process.This field is enabled only if the Import transfer type is selected.

- When this checkbox is selected, all tables will be updated from the transfer file (including master tables and electronic data files).

- When this checkbox is clear, any tables included in the transfer file that do not yet exist will be imported (including master tables and electronic data files).

File name
Enter a file name to import, or press Enter to accept the default (PRTABLES.OUT in the Spectrum data directory or, if the External file processing option is selected in the Company Installation screen, the default directory is the operator's local print directory, C:\SPECTRUM).
