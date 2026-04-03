---
title: "Change G/L Account Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes"
---

# Change G/L Account Codes

Use this screen to change and merge two or more existing General Ledger codes throughout the software, and retain all history files. If your company is migrating to cost centers, the merge feature is especially useful.
You can also use the code change utility to:

- Increase the length of your G/L code

- Move to a departmentalized chart of accounts

- Change the underlying account code logic

- Merge duplicate G/L codes together and retain their history

To merge two or more G/L codes, use the code change utility to convert them into a new code. The new code cannot exist in your Spectrum company.
Example: Merge an extra cash G/L code (0107) into the main one (0105)
0105 Main Cash Account
0107 Extra Cash Account

- Using this screen, map the old code of 0105 to 0106.

- Then, map the old code 0107 to 0106.

- Perform the update. The history for 0105 and 0107 have been merged into the new code of 0106.

- Change 0106 back to 0105. The history of 0107 has been merged successfully into 0105.

It is possible to change the overall length of the G/L code as part of the code-change process. For example, the G/L code structure can be transformed from three digits (XXX) to a longer configuration (such as five digits: X-XXXX).
Caution should be exercised when performing this type of code revision: be sure that there are no transactions in progress anywhere in the software at the time the G/L Code Change Update is performed. For example, there should not be any entered but unposted A/P invoices, and a payroll cycle should not be in progress. Be sure all other terminals are logged off when the update is performed.
The list box displays all codes that need to be changed but have not been updated.

Related information

- [Assign New G/L Code](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/assign-new-gl-code)

- [Change G/L Code Listing](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes/change-gl-code-listing)

- [Import G/L Account Codes](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/import-gl-account-codes)

- [Change G/L Account Codes Update](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes/changing-gl-account-codes/change-gl-account-codes-update)

- [Changing G/L Account Codes](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes/changing-gl-account-codes)
