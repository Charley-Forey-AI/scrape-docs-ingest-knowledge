---
title: "Expanding G/L Department Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-department-file-maintenance/expanding-gl-department-codes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-department-file-maintenance/expanding-gl-department-codes"
---

# Expanding G/L Department Codes

Learn how to expand the G/L Department Codes.
The department code length may be changed after the initial
 installation using the [Change G/L Account Codes](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes) screen. For example, the department length might be altered in
 conjunction with an expansion of the G/L account code from 4 digits to 6 digits. For more
 information, see the procedure, [Changing G/L Account Codes](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes/changing-gl-account-codes).After changing the account code length, it is
 necessary to add new departments in the [G/L Department File Maintenance](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-department-file-maintenance)
 screen using the procedure below before continuing operations.

1. On the
 Menu
 System screen, click General Ledger > Maintenance > Departments.

1. On the G/L Department File Maintenance screen,

1. Delete the old
 G/L departments and then click OK
 until you return to the Menu
 System screen.

1. Click Admin and then double-click
 General Ledger.

1. On the General Ledger Installation – Properties tab, modify the Account code mask field, if the mask will change. Also modify the Department code length and Retained earnings account number fields, as appropriate. Click OK to save your changes.

1. On the
 Menu
 System screen, click General Ledger  >
 Maintenance  > Departments.

1. In the Department code and Description fields, enter the new G/L department code(s) as needed. When all new G/L department codes have been entered, click OK to save your changes.

1. On the
 General Ledger Maintenance menu,
 double-click Master
 File. In Add mode (F5), enter the new account numbers,
 if applicable. For example, if you are changing
 from a four-digit account number with a mask of
 XXXX to an account number of XX-XXXX with a
 two-digit department code, you will probably have
 to enter several new account numbers.

Note: You may have to make a journal entry for some dollars from the new
 account number defined in step 2 to the other new
 department's account number. Click
 OK to save your changes.
Optional Steps:

- If the Validate job division with G/L department checkbox on the Job Cost Installation – Properties tab is selected, modify each job's division to match the new G/L department(s) before processing any Payroll transactions.

- If you are validating, verify the Payroll department setup. Note: You may need to add new Payroll departments.

- If the Validate equipment division to G/L department checkbox is selected on the Equipment Control Installation – G/L Codes tab, modify each piece of equipment's division to match the new G/L department(s) before processing any Equipment Control transactions.

Related information

- [G/L Department File Maintenance](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-department-file-maintenance)

- [General Ledger Installation - Properties](/en/spectrum/spectrum/accounting/general-ledger/general-ledger-installation-overview/general-ledger-installation---properties)

- [G/L Master File Maintenance](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-master-file-maintenance)
