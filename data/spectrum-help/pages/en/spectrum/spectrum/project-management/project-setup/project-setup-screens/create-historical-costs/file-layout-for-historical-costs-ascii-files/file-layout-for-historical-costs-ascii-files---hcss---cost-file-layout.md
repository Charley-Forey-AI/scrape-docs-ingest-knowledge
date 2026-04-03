---
title: "File Layout for Historical Costs ASCII Files - HCSS - Cost File Layout | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/create-historical-costs/file-layout-for-historical-costs-ascii-files/file-layout-for-historical-costs-ascii-files---hcss---cost-file-layout"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/create-historical-costs/file-layout-for-historical-costs-ascii-files/file-layout-for-historical-costs-ascii-files---hcss---cost-file-layout"
---

# File Layout for Historical Costs ASCII Files - HCSS - Cost File Layout

For the HCSS version, the system creates an historical actual cost file that is formatted for direct import into the HCSS Heavy Bid system. Phases without a billing item will not be included.
The following is a description of which Spectrum fields will be transferred to the appropriate Heavy Bid fields:
Field
Field start/end position
HCSS
Spectrum

1
(1,20)
Activity
Phase

2
(21, 30)
Work item
Billing item

3
(31, 40)
Job
Job code

4
(41,41)
Type
A (A=actual vs. E=estimate)

5
(42, 49)
Rev date
Job completion date

6
(50, 74)
ACTV description
Phase description

7
(75, 104)
WI description
Billing item description from the A/R contract file

8
(105, 116)
Quantity
Job-to-date quantity

9
(117, 119)
Unit
Unit of measure (u/m)

10
(120, 133)
Units per hour
Calculation of quantity/hours

11
(134, 145)
Labor hours
Job-to-date hours for the labor cost type

12
(146, 157)
Labor dollars
Labor dollars

13
(158, 169)
MATL dollars
Material dollars

14
(170, 181)
EXP dollars
Construction expense dollars (overhead)

15
(182, 193)
EQP dollars
Equipment dollars

16
(194, 205)
SUB dollars
Subcontract dollars

17
(206, 280)
ACTV note
Extended phase description from the unlimited phase description

Related information

- [Project Setup Installation for HCSS](/en/spectrum/spectrum/project-management/project-setup/estimating-systems/project-setup-installation-for-hcss)
