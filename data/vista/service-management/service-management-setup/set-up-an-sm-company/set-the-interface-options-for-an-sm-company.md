---
title: "Set the Interface Options for an SM Company | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/set-the-interface-options-for-an-sm-company"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/set-the-interface-options-for-an-sm-company"
---

# Set the Interface Options for an SM
 Company

You can define how data is handled when capturing work completed on a work order.
You can define how the General Ledger is updated when processing work completed, as well as whether work completed data is interfaced to the respective modules.
If you are using the Equipment Management, Inventory, Purchase Order, and/or Payroll modules, you can have the related data from work completed lines interfaced to the respective modules. For example, if you select to interface to Equipment Management (EM), equipment usage captured on a work order will generate equipment usage entries in EM.
Service Management > Programs > SM Company Parameters

1. From the main menu, select
 Service
 Management > Programs > SM Company
 Parameters.

1. In the
 SM Co
 field, enter the SM company, and then click on the Interfaces tab.

1. In the GL Usage
 Interface section, select No Update, Summary,
 or Detail to identify the level at which data will be updated to General
 Ledger when posting miscellaneous work completed entries (using SM Batches and SM
 Batch Process).

1. If you selected Summary as the GL interface level, enter the summary description in the
 Summary GL Description
 field. This description will be used when interfacing summarized miscellaneous work completed entries to GL.

1. If you selected Detail as the GL interface level, use the selection box to select each of the items to include in the detail GL description. The
 Detail GL Description
 field (display only) will include each item as it is selected.

1.  In the
 Journal
 field, enter the GL journal to update when posting miscellaneous work completed lines or press
 F4
 to select from a list of valid GL journals.

1. In the Other Interfaces section, select the checkbox for each module (EM, IN, PO, PR, and JC) to which data will be interfaced when capturing work completed on an SM work order.Note: You will typically only leave these unchecked during implementation. For more detailed information, see the F1 help for each option.

Related information

- [Set Up an SM Company](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company)

- [SM Company Parameters Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form)
