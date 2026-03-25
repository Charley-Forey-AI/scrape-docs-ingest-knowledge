---
title: "Record Type Three (3) - Cost Type Record | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/record-type-three-3---cost-type-record"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/csv-generic-layout/record-type-three-3---cost-type-record"
---

# Record Type Three (3) - Cost Type Record

Column
Max. Size
Type
Sample Mask
Description
NOTES

1
1
Alpha Numeric

Record Type
Specifies the type of record (i.e. 1,2,3,4,5).

2
10
Alpha Numeric

Project Code
Estimate or project code imported from.

3
16
Alpha Numeric

Item
Item code to be imported as contract item.

4
30
Alpha Numeric

Phase code
May set up cross-reference to Viewpoint codes.

5
30
Alpha Numeric

Cost type
Cost type

6
16
Numeric
##########.##
Quantity
No commas, rounded to Viewpoint precision.

7
30
Alpha Numeric

Unit of measure
May be cross-referenced to Viewpoint codes.

8
16
Numeric
##########.##
Hours
No commas, rounded to Viewpoint precision.

9
16
Numeric
##########.##
Amount
No commas, rounded to Viewpoint precision.

10
1
Alpha

Bill Flag
(Y,N,C) Leave blank to use default for phase.

11
1
Alpha

ItemUnitFlag
(Y,N) Leave blank to use default for phase.

12
1
Alpha

PhaseUnitFlag
(Y,N) Leave blank to use default for phase.

13
8000
String

Notes
Cost Type notes
