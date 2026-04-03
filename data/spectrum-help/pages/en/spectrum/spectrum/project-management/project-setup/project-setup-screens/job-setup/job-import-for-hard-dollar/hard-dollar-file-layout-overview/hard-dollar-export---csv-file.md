---
title: "Hard Dollar Export - CSV file | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-hard-dollar/hard-dollar-file-layout-overview/hard-dollar-export---csv-file"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-hard-dollar/hard-dollar-file-layout-overview/hard-dollar-export---csv-file"
---

# Hard Dollar Export - CSV file

Find details on the Hard Dollar Export CSV
 window.
You can choose which records to generate in the export CSV, but you must map a Tag in the
 Job Properties Section.

## Mapping: Job Header

Address Line #1, Address Line #2, and Zip Code also have the ability to be mapped to
 Tags in the Job Properties Section, but these can be left blank.

## Mapping: Phase Record

Phase Number: You can use the Account Code, CBS Code, or Phase Code to populate the
 field.

- Non-alphanumeric characters are permitted in the Account Codes.

- Common customers are advised to alphanumeric codes.

- Account codes are not required in Hard Dollar.

- Phase code is another optional code which behaves the same as
 Account Codes. In Hard Dollar like Account Codes, Phase Codes can accept
 non-alphanumeric characters.

- CBS Position Code is an auto-generated code in Hard Dollar,
 which is used to determine any activities. These codes are dot-delimited to determine
 a hierarchy, for example, 14.1 would be considered the parent of activity 14.1.1 and 14.1.2.
 They emulate activity codes in software like Primavera. Because these codes are
 guaranteed, some customers choose to work with these codes to determine phases.

Cost Type: Cost Type is also mapped to Tags in Hard Dollar. There are built-in resource
 types, but by using a tag Hard Dollar gives the user a choice to use their own code
 system for a Cost Type. This gives you the flexibility to use a coding system that may
 be different from HardDollar's. For example, instead of forcing customers to use the
 alphabet "L" to denote labor, they could choose to use "R" if that made sense to them.
 These fields can be mapped to both Selected Tags or Text Entered Tags.
Alternate Phase: Similar options as Phase Number.
Workers Compensation Code: Uses a field called Worker's Comp. Override to enter some
 information regarding Worker Compensation. Some customers populate this field with a
 code and some do not. Either use this field in HardDollar or use an empty Tag to
 populate them.
Vendor Code: We the address book for vendors. Subcontractors and customers can use tags
 inside this address book to populate vendor codes.

## Mapping: Revenue Record

Taxable Flag: You may add a Tag, which would permit you to use a Yes (Y) or No (N).
 These fields can be mapped to both Selected Tags or Text Entered Tags.

## File Layouts

The Standard file layout needs to be a comma-delimited file, with one line per record.
 There are three types of records: job, phase and revenue.

- Job records are indicated with a "*" as the first field in the record.

- Phase records are indicated with a "P" as the first field in the record.

- Revenue records are indicated with the letter "R" as the first field in the
 record.
 Each file should contain only one job. The three record formats are outlined below,
 including maximum field length.
Any blank or zero fields should still be included. For the phase, alternate phase,
 billing item, the user may want to put a quote (") in the spreadsheet column to indicate
 that these are alpha fields. The phase code will use zeroes to fill the mask.Important: When entering record layouts, you must type
 the record lines directly into the text editor. If you attempt to cut and paste a line,
 any blank spaces preceding a field in the cut text will appear as blank data in the
 import.

Related information

- [Job Record File Layout Example](/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/standard-transfer-file-layout/job-record-file-layout-example)

- [Phase Record File Layout Example](/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/standard-transfer-file-layout/phase-record-file-layout-example)

- [Revenue Record File Layout Example](/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/standard-transfer-file-layout/revenue-record-file-layout-example)
