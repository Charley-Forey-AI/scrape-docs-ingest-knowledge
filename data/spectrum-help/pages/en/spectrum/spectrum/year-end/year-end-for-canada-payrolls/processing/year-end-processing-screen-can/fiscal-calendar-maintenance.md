---
title: "Fiscal Calendar Maintenance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/year-end-processing-screen-can/fiscal-calendar-maintenance"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/year-end-processing-screen-can/fiscal-calendar-maintenance"
---

# Fiscal Calendar Maintenance

The Fiscal Calendar Maintenance screen displays all fiscal years presently set up in the current company.
If this is part of your year-end processing, see [Open Forward Balance Update - G/L](/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/year-end-processing-screen-can/open-forward-balance-update---gl).
Entries made here control certain defaults and virtually every transaction updated to the General Ledger.
Normally, no changes are required in this screen. If changes are made, the dates on any historical transactions will not be changed.
Warning: Do not change the fiscal calendar once data has been entered into the software. Information in the General Ledger could become corrupted.
Note: Note regarding first-time users: If this screen is accessed before the fiscal calendar has been created in General Ledger Installation, the list box will be empty and only the New Year button will be enabled. This button can be used to open the Add New Fiscal Year window and you will be prompted for the first fiscal year, as you would be in the General Ledger Installation screen.
The Fiscal Calendar Change Log TableThe Fiscal Calendar change log table GL_FISCAL_CALENDAR_LOG (GL.FCL) may be accessed for review of by performing a query. This table logs any additions or changes to the following columns:

- Company – Key

- Year – Key

- Period – Key

- Sequence or Unique identifier – Key

- Entry type – 'C' = created, 'R' = reset, 'D' = deleted

- Entry date – System date

- Entry time – System time

- Entry operator – 3-digit operator code

- New start date

- New end date

- New period description

- Old start date

- Old end date

- Old period description

Other tables and views related to this screen include:

- GL_FISCAL_CALENDAR_DETAIL (GL.FYDET) (table)

- GL_FISCAL_CALENDAR_BY_PER_MC (view)

- GL_FISCAL_CALENDAR_BY_YEAR_MC (view)

Related information

- [Changing the Fiscal Calendar to a Long Year](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/reset-fiscal-calendar/changing-the-fiscal-calendar-to-a-long-year)

- [Changing the Fiscal Calendar to a Short Year](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/reset-fiscal-calendar/changing-the-fiscal-calendar-to-a-short-year)

- [Fiscal Calendar Changes - No Transactions Entered](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/period-end-overview/fiscal-calendar-maintenance/fiscal-calendar-changes---no-transactions-entered)

- [Fiscal Calendar Changes - Transactions Entered](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/period-end-overview/fiscal-calendar-maintenance/fiscal-calendar-changes---transactions-entered)

- [Reset Fiscal Calendar](/en/spectrum/spectrum/accounting/general-ledger/spectrum-menus/utilities-overview/reset-fiscal-calendar)

- [Year End Processing Screen (U.S.)](/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/year-end-processing-screen-u.s.)

- [Year End Processing Screen (CAN)](/en/spectrum/spectrum/year-end/year-end-for-canada-payrolls/processing/year-end-processing-screen-can)
