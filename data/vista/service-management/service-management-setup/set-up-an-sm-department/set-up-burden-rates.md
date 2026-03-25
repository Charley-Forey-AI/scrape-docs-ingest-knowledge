---
title: "Set up Burden Rates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-burden-rates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-department/set-up-burden-rates"
---

# Set up Burden Rates

You will set up labor burden rates using the Burden Rates tab in SM Departments.
Burden rates are defined by liability type and are used to determine the amounts debited to Cost and Cost WIP GL accounts for work completed labor lines when running PR Ledger Update.
Note: You must define burden rates for each liability type that you will use for tracking labor burden. If you do not set up burden rates for applicable liability types, no GL update will occur.
The following instructions detail how to set up burden rates in SM Departments.

1. In the Department field, enter the department for which to set up burden rates.

1. Click on the Burden Rates tab.

1.  In the Liability Type field, enter the liability type for which to define a labor burden rate. Press F4 for a list of valid liability types (as set up in HQ Liability Types).

1.  From the Rate Type drop-down, select E-Exactly as Payroll to use exact amounts from Payroll or R-Rate to enter an override calculation rate.

1. If you selected Rate in Step 4, in the Rate field, enter the rate to use when calculating burden for this liability type.

1. If you selected Exactly as Payroll in Step 4, skip to Step 6.

1. Save the record.

1. Repeat Steps 3-6 for each applicable burden liability type.

Related information

- [SM Departments Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-departments-form)
