---
title: "Add-on Formula | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-file-formula-maintenance/add-on-formula"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-file-formula-maintenance/add-on-formula"
---

# Add-on Formula

Follow these steps to add an add-on formula in
 payroll.

1. From the Payroll  >  Maintenance  >  Electronic File Table Maintenance screen, click the Formulas button. The Electronic Formula File Maintenance screen displays.

1. Enter a formula code, description and select a type
 from the drop-down menu.Note: Records are used for the sum of each check or sum of checks. Totals are useful
 when the calculation involves categories.

1.  Press Enter to proceed to the line transactions. The Sequence number defaults automatically.

1. In the Result field, enter T1 (for temporary variable #1).

1. In the 1st factor field, press F4 or double-click on this field to display the Search Variables window and select the file that contains the employee's deduction and add-on history (in this example, file PR. EHVD).

1. Next, select the variable from the file, in this example, the employee's deduction amount (PR. HVDAMT). Click OK. The Details window displays.

1. In the Select by field, select Add-on / deduction code from the drop-down list.

1. In the Selection field, press F4 and select the add-on or deduction you want to include as the first factor in the formula (for example, MR = mileage reimbursement). Click OK.

1. In the Operator field, select the + sign for addition.

1. In the 2nd factor
 field, press F4
 or double-click in this field, and then select the same file and variable. This time,
 then the Detailsto the
 window displays, in the Select
 by field, select category from the drop-down list. For more information on setting up
 categories, refer to the [Electronic Category Group Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-category-group-maintenance) topic.

1. In the Selection field press F4 or double-click in this field to select the applicable category.

1. In the Result field in line 2, enter Answer.

1. In the 1st factor field, enter T1 to use the sum from line one.

1. In the Operator field, select the * sign for multiplication.

1. In the 2nd factor field, enter –1. This will take the sum of the add-ons and multiply it by negative one in order to yield the absolute value for the add-on. In this way, the add-ons will print as positive amounts on the final report.

1. In the Period field, select either Current or Year-to-date from the drop-down menu to assign the appropriate period to the factors and calculate the formula based on current or year-to-date amounts. If you leave this field blank for either factor, the Period information will default from the main screen.
