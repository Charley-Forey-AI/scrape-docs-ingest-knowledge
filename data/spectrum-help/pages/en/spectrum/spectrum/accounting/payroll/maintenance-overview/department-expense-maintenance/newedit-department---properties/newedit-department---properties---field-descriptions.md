---
title: "New/Edit Department - Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/department-expense-maintenance/newedit-department---properties/newedit-department---properties---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/department-expense-maintenance/newedit-department---properties/newedit-department---properties---field-descriptions"
---

# New/Edit Department - Properties - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/Buttons
Descriptions

Department code
Enter the G/L department code. The system will generate an error message if the entered General Ledger department has not yet been set up.
A Note About Using Numeric Coding: Because many users prefer alphabetic or combination alpha and numeric coding, this code is not a numeric-only field. Because of this, the code left-justifies when entered. Users preferring a strictly numeric coding scheme should be advised to use leading zeros when adding codes in order to produce desired sort results on screens and reports. Without leading zeros, 1, 10, and 100 will appear before 2, 20, and 200. Instead, codes should be set up 001, 002, and so forth.
 If the Job Cost Installation - Set add-on G/L account from Payroll department checkbox is selected, the new account number generated will use the appropriate number of characters for the department code, based on the division setup in General Ledger Installation screen. For example, if the Division = 2, and the Payroll department = 18, the G/L account 1799 becomes 1899.

Descriptions
Enter the department description.

Direct cost
From the drop-down menu, select the direct cost type that you want to assign to the department code: job cost, non-direct job cost, equipment cost or work order cost. Entry in this field is required.
During Time Card Entry, the G/L account associated with the pay type will be verified in the assigned company of the line to assure the account is valid and matches this direct cost flag.

Worker's compensation code
Enter a worker's compensation code. Entry in this field is optional. Please refer to the Worker's Compensation Code Maintenance section for default hierarchy information.

Salary/wages
Enter the General Ledger account code for each of the expenses.
The General Ledger account descriptions will display based on the department code entered, and no entry is allowed.
