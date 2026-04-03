---
title: "Example #2: Employee File Including Add-Ons | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file/using-the-electronic-file-build-steps/example-2-employee-file-including-add-ons"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file/using-the-electronic-file-build-steps/example-2-employee-file-including-add-ons"
---

# Example #2: Employee File Including Add-Ons

This procedure is provided for more advanced users and
 assumes a certain level of familiarity with the Electronic File Build feature.
If you are a new user, please review Example #1 before
 proceeding to this procedure. When needed, it is possible to set up
 longer, more complicated text files. The same key principals apply: make sure you know
 what information you want to include, and try to set up any more complicated formulas in
 advance. The steps below are general directions on how you might structure a larger file
 that includes an add-on and category formula.

1. Draw up the information you want to include on the Add-ons report prior to setting it up in Spectrum®. For example, you might want to include the employee code, employees' names and addresses, their annual salaries, their hire dates, any add-ons or deductions, and so forth

1. Click Maintenance > Electronic File Table
 Maintenance.

1. Enter a Table code, (for example, ADDON).

1. Select a Data type from the drop-down list.Note: Most states require fixed width reports.

1. The Properties window displays automatically. Complete the Properties window. Including one or more sort variables (for example, you might select to sort by the employee code, PR.EMPCODE as taken from the Employee Master file) can be very helpful in organizing how the resulting data will be displayed. Click OK to proceed.

1. The File Name window displays automatically. Follow the directions provided in the dialog box for help in setting up the default file name for the electronic table file. If both checkboxes are selected, the file name path must include both the pound sign (#) and the dollar sign ($) in order to automatically insert the Payroll processing date and company ID information, (for example, C:\DATA\#$).

1. Press Enter to proceed to the line transactions. Sequence numbers are assigned by the software.

1. If you want a title or descriptive phrase to appear on each line of the report, select Constant from the Variable type drop-down list.

1. Enter the constant Descriptions (for example,
 Employee Add-ons 2014),
 or leave the description field blank if you want to include a placeholder on the
 report.Note: For readability purposes, when using fixed-width data
 types it can be helpful if you place a Constant placeholder between each variable.
 However, check with the intended recipient to see if this is the best way to set
 up your file before doing so.

1. Continue to complete the line transactions with the information you want to include on the report. For example, you may want to include such Single variable types as the employee's code, concatenated name, hire date, rehire date, annual pay rate, and so forth.

1. Select the Non-zero only checkbox if you want to deselect this record if a given variable (for example, the hire date, social security number, or state earnings amount) is blank or zero. This feature is especially helpful if you do not want a record to appear in the file.

1. If you want to include more complicated variables, such as a formula for an employee add-on that includes a category, first you would need to set up the formula.

1. Continue to compete the file table until all the information needed by the recipient is complete.
