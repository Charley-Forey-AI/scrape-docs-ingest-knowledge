---
title: "Standard Transfer File Layout | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/standard-transfer-file-layout"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/standard-transfer-file-layout"
---

# Standard Transfer File Layout

The Standard file layout needs to be a comma-delimited file, with one line per record. There are three types of records: job, phase and revenue.

- Job records are indicated with a "*" as the first field in the
 record.

- Phase records are indicated with an uppercase "P" as the first
 field in the record.

- Revenue records are indicated with an uppercase "R" as the first
 field in the record. Each file should contain only one job. The
 three record formats are outlined below, including maximum field length.
Any blank or zero fields should still be included. For the phase,
 alternate phase, billing item, the user may want to put a quote (") in the
 spreadsheet column to indicate that these are alpha fields. The phase code will use
 zeroes to fill the mask.
Important: When
 entering record layouts, you must type the record lines directly into the text
 editor. If you attempt to cut and paste a line, any blank spaces preceding a field in
 the cut text will appear as blank data in the import.

Related information

- [Job Record File Layout Example](/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/standard-transfer-file-layout/job-record-file-layout-example)

- [Phase Record File Layout Example](/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/standard-transfer-file-layout/phase-record-file-layout-example)

- [Revenue Record File Layout Example](/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/import-standard-job/standard-transfer-file-layout/revenue-record-file-layout-example)
