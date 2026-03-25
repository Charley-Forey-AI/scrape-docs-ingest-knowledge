---
title: "Crystal Report Troubleshooting Tips | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/reports/crystal-reports-overview/crystal-report-troubleshooting-tips"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/reports/crystal-reports-overview/crystal-report-troubleshooting-tips"
---

# Crystal Report Troubleshooting Tips

Before using the following grid to troubleshoot a problem with a Crystal report, be sure to verify that you have placed group or key fields in the detail section.
Because the details ultimately make up subtotals in the group header or footer, seeing the individual detail records will help determine whether the report is returning too much or too little data.
Problem
Cause
Solution

Subtotals too high / Report returns too much data
Missing link between views, resulting in too many records getting returned.
Make sure index fields of views are linked.

Subtotal on field in summary view.
Use Running Total instead of Subtotal.

Subtotals too low / Report returns too little data
View linked to null field, resulting in too few records getting returned.
Use Left Outer Join.

Nullable fields used in record selection, resulting in too few records getting returned.
Use SQL Expression – See %ProjMgr expression in JC Cost Rev template.

Detail does not foot to subtotal
Suppression formula in group header is hiding some of the rows.
Use running total.

Ratio or PctFormula obviously incorrect
Not using the “Sum” function in formula.
See Pct Compl formula in JC Cost Rev template.

“Divide by Zero” error
Formula is missing check for 0 in denominator.
See Pct Compl formula in JC Cost Rev template.

Related information

- [Adding Reports to Module Menus](/en/vista/vista/system-tools/reports/report-setup-and-maintenance/adding-reports-to-module-menus)

- [Formatting Crystal Reports](/en/vista/vista/system-tools/reports/crystal-reports-overview/formatting-crystal-reports)

- [Crystal Report Settings for Vista™ Reports](/en/vista/vista/system-tools/reports/crystal-reports-overview/crystal-report-settings-for-vista-reports)
