---
title: "CSV (Generic) Layout | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/csv-generic-layout"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/csv-generic-layout"
---

# CSV (Generic) Layout

The standard comma separated value import from a third-party package is made up of multiple record types within the file. There may be quotes around the alpha fields. The import program checks for quotes and, if found, removes them. Some fields may be cross-referenced to Viewpoint codes. All numeric fields should have no commas, and the decimal position is a floating decimal. The import will round the numeric to the precision defined in the data dictionary for each field. All fields will be formatted to the data dictionary specifications.
The record types will be as follows:
Record Type One (1)
= Item Record

Record Type Two (2)
= Phase Record

Record Type Three (3)
= Cost Type Record

Record Type Four (4)
= Subcontract Record (Optional)

Record Type Five (5)
= Material Record (Optional)

Record Type Six (6)
= Project Record (Optional)

Note: Record types must be listed numerically in the file.
 In other words, Record Type 1 (Items) must occur before Record Type 2 (Phases); Record Type
 2 must occur before Record Type 3 (Cost Types), and so on.
Each record type has a specific format for importing. To see a layout of each record type, click a link below.

- [Record Type 1 – Item Record](/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/record-type-one-1---item-record)

- [Record Type 2 – Phase Record](/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/record-type-two-2---phase-record)

- [Record Type 3 – Cost Type Record](/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/record-type-three-3---cost-type-record)

- [Record Type 4 – Subcontract Record](/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/record-type-four-4---subcontract-record)

- [Record Type 5 – Material Record](/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/record-type-five-5---material-record)

- [Record Type 6 – Project Record](/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/record-type-six-6---project-record)

- [Sample CSV Import](/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/sample-csv-import)
