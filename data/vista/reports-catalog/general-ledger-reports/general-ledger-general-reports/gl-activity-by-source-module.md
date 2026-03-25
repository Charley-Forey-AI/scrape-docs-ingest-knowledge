---
title: "GL Activity by Source Module | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-activity-by-source-module"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/general-ledger-reports/general-ledger-general-reports/gl-activity-by-source-module"
---

# GL Activity by Source Module

You can use the GL Activity by Source Module report for GL
 activity by source module by selecting General Ledger > Reports > GL Activity by Source Module.
The GL Activity by Source Module is basically the same as the GL Trial balance. It has an added feature of source entry allowing the user to enter "AP" or "JC" to print only the General ledger entries coming from the selected modules. The source entry is actually using the source from the table that includes a longer description of source such as “AP Entry” or “AP Payment” but since there are many of these possible sources, we require the customer enter only the first 2 characters of this field. This report runs from a stored procedure, "brptGLFinDet".
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Format: (D)etail or (R)eference
Enter D or R.

Beginning Account
Click the Field Lookup
 button or press F4 to select beginning account or leave blank
 for all.

Ending Account
Click the Field Lookup
 button or press F4 to select ending account or leave blank for
 all.

Beginning Month
Enter or select the applicable beginning month.

Ending Month *Same Fiscal Year as Beg Mth
Enter or select the applicable ending month.

Sources to Include (AP, AR, etc.) Blank for
 All
Enter two letter module code (AP, AR, etc.) separated by commas for modules to include or leave blank for all.

Journal
Click the Field Lookup
 button or press F4to select journal to include or leave blank
 for all..

Include Year End Adjustments?
checkbox to include year end adjusting entries. Leave unchecked to exclude year end adjustments from the report.

Subtotals By Month?
Check this box to include subtotals by month.

Include Inactive?
Check this box to include inactive GL accounts.
