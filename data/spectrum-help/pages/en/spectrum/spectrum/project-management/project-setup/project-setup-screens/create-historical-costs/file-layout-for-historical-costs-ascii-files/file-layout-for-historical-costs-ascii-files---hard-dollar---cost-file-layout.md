---
title: "File Layout for Historical Costs ASCII Files - Hard Dollar - Cost File Layout | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/create-historical-costs/file-layout-for-historical-costs-ascii-files/file-layout-for-historical-costs-ascii-files---hard-dollar---cost-file-layout"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/project-setup/project-setup-screens/create-historical-costs/file-layout-for-historical-costs-ascii-files/file-layout-for-historical-costs-ascii-files---hard-dollar---cost-file-layout"
---

# File Layout for Historical Costs ASCII Files - Hard Dollar - Cost File Layout

For the Hard Dollar version, the system creates an
 historical actual cost file that is formatted for direct import into the Hard Dollar system.
This download can be created based on the phase code or alternate phase code in the phase
 file. The historical cost file is used in their estimating system for historical unit cost
 analysis while doing take-offs. A separate update has been created to transfer costs for
 labor, burden, supplies and other.
The following is a description of which Spectrum fields will be transferred to the appropriate Hard Dollar EOS fields:
Field
Hard Dollar
Spectrum

1
Code
Phase

2
Project ID
Job - 1st 8 characters, discounting spaces

3
Project description
Job description

4
As-built quantity
Job-to-date quantity (total for all cost types)

5
Unit of measure
Unit of measure, qty cost type *

6
Year of work
Year of actual complete date

7
Labor code
blank

8
Labor rate
JTD amount / JTD hours, labor cost type(s) **

9
Area code
User-defined field

10
Labor description
Phase description for labor cost type(s) **

11
Unit cost - labor
JTD amount / JTD quantity, labor cost type(s) **

12
Labor burden
0

13
Unit cost - equipment
0

14
Equipment ownership
0

15
Unit cost - rentals
0

16
Unit cost - materials
0

17
Unit cost - supplies
0

18
Unit cost - subcontracts
0

19
Unit cost - other
0

20
Unit cost - tax
0

21
Total unit cost
JTD amount / JTD quantity, quantity cost type *

22
Shifts
0

23
Shift hours
0

24
Man hours
JTD hours, labor cost type(s) **

*The quantity cost type is defined in the Project Setup Installation
 screen. If it is blank, the quantity cost type will be taken from the Job Cost
 Installation, and if multiple, the labor quantity cost type will be used.
**The labor cost type matches what is defined in Job Cost Installation
 under "labor cost type(s)."

Related information

- [Hard Dollar Overview](/en/spectrum/spectrum/project-management/project-setup/estimating-systems/hard-dollar-overview)
