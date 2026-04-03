---
title: "Changing G/L Account Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes/changing-gl-account-codes"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes/changing-gl-account-codes"
---

# Changing G/L Account Codes

Learn how to change or merge existing G/L account codes.

1. On the Menu System screen, click General Ledger  >  Utilities  >  G/L Code Change >  >  New. The [Assign New G/L Code](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/assign-new-gl-code) window displays.

1. In the Old code field, enter the old G/L code. If you do not know the old G/L code, click the arrow or press F4 to search available G/L codes.

1. In the New code field, enter the new G/L code. To merge existing codes into a single new code, enter an existing code that has not been updated. For further information on merging and assigning new G/L codes, see the Assign New G/L Code topic.Note: Note regarding Department/Division logic: If you are adding
 Department/Division logic, you can change account code 4000 to 10-4000. It will be
 necessary to add accounts 20-4000, 30-4000, and so forth manually after updating
 the change G/L codes. First, modify the G/L Installation screen to the new mask
 XX-XXXX. Then, add the new department codes in G/L Department Maintenance. Keep in
 mind that after entering the new mask, you will not need to enter the dash symbol
 (-) during data entry because the software will do this for you automatically. For
 example, typing account 204000 would display as 20-4000.

1. Click OK to save and exit, or click Cancel to exit the window without changes. The [Change G/L Account Codes](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes) screen displays.

1. Click Listing to access the [Change G/L Code Listing](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes/change-gl-code-listing)screen, and then click Preview to verify your code change. Review the listing carefully to make sure that all account codes are assigned properly and the same length. You cannot cancel the update after it has been performed.

1. After previewing the report, the software returns to the G/L Code Change screen. The Preview Report window displays first. Click OK.

1. In the G/L Code Change Maintenance screen, click Update. After reading the Code Change Warning window, click OK. The [Change G/L Account Codes Update](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/change-gl-account-codes/changing-gl-account-codes/change-gl-account-codes-update) screen displays.

1. Select Yes, proceed with update, and then click OK.Note: Regarding the G/L Code Change update: This update may take some time.
 The function looks at every file in the software that has account numbers (General
 Ledger, Payroll, Accounts Payable, Payroll, and so forth) and changes them
 accordingly. It is recommended that all other users be logged out of Spectrum at
 the time of the update to speed up the process and avoid any problems.

1. Click OK until you return to the Menu System screen.Maintenance screens are usually updated as part of the G/L Code Change Update. Nevertheless, it is a good idea to review the affected codes in the G/L Master File Maintenance screen after the update to ensure they were properly updated.

Related information

- [Expanding G/L Department Codes](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/maintenance-overview/gl-department-file-maintenance/expanding-gl-department-codes)

- [Changing General Ledger Maintenance Settings](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/changing-general-ledger-maintenance-settings)

- [Updating General Ledger Installation Settings](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/updating-general-ledger-installation-settings)
