---
title: "Example #1: Employee Raise | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file/using-the-electronic-file-build-steps/example-1-employee-raise"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/build-electronic-data-file/using-the-electronic-file-build-steps/example-1-employee-raise"
---

# Example #1: Employee Raise

Complete the following steps to learn how to use the
 Electronic File Table Maintenance
 screen to create a report that shows employee salary increase information.

1. Draw up the information you want to include on the Employee RaiseReport prior to setting it up in Spectrum. For example, you might want to include the employee code, employee name, the employees' current salaries, the salary increase formula (salary percentage), and the employees' hire date.

1. Click Maintenance  >  Electronic File Table Maintenance.

1. Enter a Table code, (for example, RAISE).

1. Enter a Descriptions for the table (for example, EMPLOYEE SALARY INCREASE).

1. Select a Data type from the drop-down list.

1. The Properties window displays automatically. Complete the Properties window. Including one or more sort variables (for example, you might select to sort by the employee code, PR.EMPCODE as taken from the Employee Master file) can be very helpful in organizing how the resulting data will be displayed. You can also select a checkbox to ensure that text will be stored in uppercase letters only. Click OK to proceed.

1. The File Name window displays automatically. Follow the directions provided in the dialog box for help in setting up the default file name for the electronic table file. If both checkboxes are selected, the file name path must include both the pound sign (#) and the dollar sign ($) in order to automatically insert the Payroll processing date and company ID information, (for example, C:\DATA\#$).

1. Click OK to proceed to the line transactions. Sequence numbers are assigned by the software.

1. If you want a title or descriptive phrase to appear on each line of the report, select Constant from the Variable type drop-down list.

1. Enter the constant Descriptions (for example, Salary Increases – First Quarter), or leave the description field blank if you want to include a space holder on the report.

1. Enter Alphanumeric for the file Type.Note: Key must be entered to display the sort variables; otherwise
 the report data will sort according to the setup in the Properties window.

1. Complete the remaining fields on this line and proceed to the second line of the report.Note: For more information on these fields see the [Electronic File Formula Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/electronic-file-formula-maintenance) screen.

1. Create a Constant space holder in line 2.

1. In the third line of the report, at the Variable type column, select Multiple. Multiple variables allow you to concatenate a number of fields, for example, you might include an employee's first, middle, and last name as one field in the report.

1. The Concatenate Multiple Variables window displays automatically. Complete the window as shown here. The variable types for the employee's first and last names can be found in the PR.EM1, or Employee Master, file. (Again, the file Type should be Alphanumeric.)

1. In line 4, create another Constant that with a description that reads Annual Pay.

1. In line 5 select a Single variable. The Search Files Variables window will display. From the drop-down list, select Employee Master. A list of variables displays. Scroll down and select the ANNUAL PAY RATE variable. Click OK to return to the main screen and complete the rest of the line. The file type for the annual pay rate will be Numeric.

1. In line 6 select a Formula variable. The Electronic File Formulas window will display. Select the RAISE formula and click OK to return to the main screen and complete the rest of the line. The file type for the annual pay rate will be Numeric.Note: For more information about setting up formulas,refer to the
 [Setting up Formulas](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/electronic-file-table-maintenance/using-the-electronic-file-build-steps/setting-up-formulas) topic.

1. In line 7 create another Constant space holder as you did in line 2.

1. In line 8 select a Single variable. The Search Files Variables window will display. From the drop-down list, select Employee Master. A list of variables displays. Scroll down and select the HIRE date variable. Click OK to return to the main screen and complete the rest of the line. The file type for the annual pay rate will be (D)ate and the Fill information will default.Note: You can set up the Display format anyway you like (for
 example, MM/YY, MM/DD/YY, and so forth) by typing in the format you want to
 use.

1. The Electronic File Table Maintenance screen should now look like this:

1. To view the RAISE 2001 listing, click the Listing screen and then select the RAISE 2001 table.

1. Click Preview to view your new report.
