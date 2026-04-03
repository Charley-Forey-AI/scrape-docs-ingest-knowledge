---
title: "UDF Values Input | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/understanding-user-defined-fields/udf-values-input"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/understanding-user-defined-fields/udf-values-input"
---

# UDF Values Input

The table below shows examples of valid display codes for use when setting up user-defined field alignment masks. Alignment masks are only applicable for 'Numeric' fields.
When a report is initially created, the software suggests the display code, but the default may be overwritten. If the field length is changed after creating the report, the corresponding display code must also be changed.
This table shows sample display codes and how different numeric values would appear when that code is applied (# represents a placeholder).
Values Input

Display code
Example A
Example B
Example C
Example D

.12345
1234.56
12.3456
-123.456

$9,999.99-
$0,000.12#
1234.56#
$0,012.35#
$0,123.46-

ZZZZZ9
#####0
##1234
####12
******

ZZ9999.99
##0000.12#
##1234.56#
##0012.35#
##01234.46-

99
00
**
12
**

Z9-
#0#
***
12#
***

-$$,$$$.99
#####$.12
#$1234.56
####$12.35
-##$123.46

$ZZZZ.99
$####.12
$1234.56
$##12.35
********

ZZZZ+
####
12345+
##12+
#123-
