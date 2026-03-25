---
title: "Field Definitions: JB Interface Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-interface-form/field-definitions-jb-interface-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/jb-interface-form/field-definitions-jb-interface-form"
---

# Field Definitions: JB Interface Form

The following is a list of field descriptions for the JB
 Interface form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Bill Month

Specify the bill month for interfacing invoices or enter the current billing month for
 the billings you wish to move forward to the next month.
Note: If you are re-interfacing a
 closed-month billing, change the default to a month that is open in both JC and AR.
 Billings cannot be re-interfaced to a closed month. For more information, see [About Changing Interfaced or Closed-Month Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings).

## Created By

Enter the user by which to restrict billings
 displayed in the grid. Press F4 for a list of valid users. Only
 billings that were created by the selected user and meet all other selection criteria will
 display in the grid.
 If left blank, all billings meeting the selection criteria will display, regardless of who created them.

##  Restrict by Process Group

 Check this box to restrict invoices by a specific processing group. Only invoices assigned to the processing group specified in the Process Group field will display in the grid.
 Leave this box unchecked to have all invoices for the specified bill month display in the grid.

##  Process Group

 Enter the processing group (from JB Processing Group) to restrict invoice selection by. Only invoices assigned this processing group will display in the grid.

## Interface all bills

Check this box to have the Interface check
 box automatically selected for all invoices displayed in the grid. Invoices that should not
 interface can be deselected manually.
Leave this box unchecked to select invoices
 for interface manually. The Interface checkbox will default to
 unchecked for all invoices displayed in the grid.

##  Include Billings With Blank Invoice Numbers

 Check this box to view billings with blank invoice numbers. The Grid will display active billings without an invoice number and billings that are ready for interfacing. The system disables both the Interface checkbox for each item in the grid and the Post button. Uncheck this box to proceed with the interface.

##  Interface

 Check this box to interface this invoice when posting the batch.
