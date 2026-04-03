---
title: "New/Edit G/L Account - Properties Tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/newedit-gl-account---properties-tab"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/newedit-gl-account---properties-tab"
---

# New/Edit G/L Account - Properties Tab

The Properties tab is used to select the account details, direct cost designation, and status of the G/L account code you are adding. As entries are completed in these windows, the data will display on the G/L Master File Maintenance starting screen.
Field
Description

G/L account code
Enter the General Ledger account code in the format defined in the Installation screen. Your account code must begin with the department codes you have defined. For example, if your department codes are 1, 2, and 3, you will be unable to start an account code with 4.

Department
 If department codes are part of the General Ledger account code, the department name associated with the account code displays.

Description
Enter the General Ledger account description, which can be either 18 or 30 characters long.

Abbreviated description
The first 18 characters of the entered account description display. When this account is printed,the text appears on certain financial reports. If this abbreviation describes the account, press Enter; otherwise enter a different description.

Account type
 Select the account type that you want to display on the [G/L Master File Maintenance](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-master-file-maintenance) screen.
Note: The 'Statistic' account type is used for financial reports to show $/unit or some other ratio on the income statement. When this option is selected, you enter the quantity for these accounts in a journal entry and update, and then they can be used in the financial statement design.

Direct cost
Select a direct cost method for this account:

- Non-direct cost: Typically anything that is considered an overhead cost.

- Job cost: This option forces the user to enter a job number if posting to the account.

- Equipment cost: This option forces the user to enter an equipment number if posting to the account.

- Work order cost: This option forces the user to enter a work order number if posting to the account.

During conversion, this field would be set to Non-direct cost. After the conversion journal entry has been made and updated, it should be changed to Job cost or Equipment cost.

Status
Select the status for this account:

- Active

- Inactive

- Not used

If the Not Used status is selected for an income or expense account and that same account's year-end balance is $0.00, the account will not roll forward to the next year when the G/L Opening Forward Balance Update is run. Likewise, if an asset, liability, or capital account's year end balance is $0.00 and the account's status is Not used, the account will not roll forward during the G/L Opening Forward Balance Update.
