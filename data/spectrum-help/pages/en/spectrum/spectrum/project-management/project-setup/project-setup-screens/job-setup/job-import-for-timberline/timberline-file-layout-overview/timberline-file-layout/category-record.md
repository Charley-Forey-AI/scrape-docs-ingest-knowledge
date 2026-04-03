---
title: "Category Record | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-timberline/timberline-file-layout-overview/timberline-file-layout/category-record"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/job-setup/job-import-for-timberline/timberline-file-layout-overview/timberline-file-layout/category-record"
---

# Category Record

Note regarding Category Codes:
Category codes for Equipment, Labor, Materials, Subcontract and Other must be entered as three characters as follows:

- EQU = Equipment

- LAB = Labor

- MAT = Materials

- SUB = Subcontract

- OTH = Other

When imported into Spectrum, these three-digit codes will be converted into single-digit cost types (E, L, M, S, O). Any unrecognized character codes will automatically be converted to O.
Field Name
Type
Description
Length

RECTYPE
A
C to indicate category record type
1

PHASEID
A
Job phase code in which item is included
15

DESCRIPTION
A
30 characters filled with spaces
25

CATEGORY
A
Job cost category for item
3

TRANDATE
N
Date file generated (mmddyyyy format)
8

QUANTITY
N
Quantity of item used in this phase
8.2

UM
A
Unit of measure
4

AMOUNT
N
Dollar amount of item
8.2

LOCATION or USER1
A
Location of item from estimate -or- Location or WBS code for item (PE Ext)
20

USER2
A
Location or WBS code for item (PE Ext)
20
