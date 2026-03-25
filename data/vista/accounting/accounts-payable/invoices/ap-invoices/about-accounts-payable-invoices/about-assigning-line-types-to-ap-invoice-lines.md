---
title: "About Assigning Line Types to AP Invoice Lines | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-assigning-line-types-to-ap-invoice-lines"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-assigning-line-types-to-ap-invoice-lines"
---

# About Assigning Line Types to AP Invoice Lines

You must assign a line type to each AP invoice line. The line
 type identifies where you want to post the expense, as well as the type of information
 required for that line type.

When you enter detail lines on an invoice (in
 AP Transaction Entry, AP Unapproved Invoice Entry, or AP Recurring Invoices), there are
 several different line types available for selection. Some of the
 data required is the same for all line types, but there may be additional data that is
 required for specific types. This topic discusses each of the types, as well as the fields
 that display based on that type.
Note: Because EM, PO, SL, and SM are optional modules you may not
 be able to use the Equipment, EM Work Order, Purchase Order, Subcontract, or
 SM Work Order line types.

## Job (Line type 1)

Use this line type for expenses related to a JC job. When you select this type, the
 system displays the JCCo, Job,
 Phase, CT, and Material
 fields. Job lines require that you enter data into the JCCo,
 Job, and Phase fields. Enter data into these
 fields or press F4 to find relevant information.

## Inventory (Line type 2)

Use this line type when you need to enter stock purchases that have not been set up on a
 purchase order. When you select this option, the system displays the IN Co,
 Loc, and Material fields, all of which are
 required.
When you post inventory invoices, the system updates the on-hand inventory quantity for
 the material. If you enter units in the Units field, the system will convert
 that quantity into the standard UM to update the on-hand quantity (using the conversion
 factor set up in HQ Materials)

## Expense (Line type 3)

Use this line type for all non-job purchases if you are not interfacing to SL, IN, or
 EM, or you are not using the PO module. If you are interfacing to other modules, use
 this invoice type for payables that do not fit any of the other categories. These
 invoices are not on a purchase order and do not update any modules other than GL. You
 can enter information in the Material field, but it is not
 required.

## Equipment (Line type 4)

Use this line type for equipment expenses that do not apply to a purchase order or EM
 work order. When you select this option, the system displays the EMCo,
 Equipment, Comp Type, Component,
 Cost
 Code, Cost Type, and Material
 fields.

## EM Work Order (Line type 5)

Use this line type for equipment expenses that apply to an EM work order. When you
 select this option, the system displays the EMCo, WO, Item#,
 Cost
 Code, Cost Type, and Material
 fields.

## Purchase Order (Line type 6)

Use this line
 type when the line applies to a purchase order. When you select this option, the system
 displays the PO, PO Item#, PO Item Line,
 Rec
 #, and Material fields.Purchase order invoices use the information set up in the PO module (or via SM Purchase
 Order Entry for SM-related purchase orders) and let you fill in the rest of the details
 from the vendor’s invoice. Once you enter (or [initialize](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-purchase-order-initialize-form)) a valid PO number, item, and item line, the
 screen displays the information from the PO based on the PO type (Job, Inventory,
 Expense, Equipment, EM Work Order, and SM Work Order). Fields that are grayed
 out cannot be changed. Notes associated with the PO appear on the PO Notes tab; line
 item notes display in the Item Notes field, while PO header
 notes display in the PO Notes field. The PO Notes tab does
 not display if you do not have the PO module installed.
Note: If you need to distribute a PO item into multiple lines,
 select the Tasks drop-down on the toolbar to open the PO Item Distribution form. This
 option is only available from AP Transaction Entry and AP Unapproved Invoice Entry.
 For more information, see [PO Item Distribution](/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-item-distribution-overview).

If the Receiving checkbox is selected for the purchase order in the PO Purchase Order Entry form,
 the Received minus Invoiced quantity defaults in the Units field. If you attempt to change it
 to a larger quantity the system display a warning, but you can proceed. If you did not
select the Receiving checkbox, the Original minus the Invoiced quantity defaults in the
 Units field.The system verifies the dollar amounts
 that you enter for each item to make sure that they do not exceed the total cost of the
 purchase order, purchase order item, or purchase order item line. If the items do exceed
 the total cost, the system displays a warning but you can proceed. However, to post the
 batch you must have selected the following checkboxes in the AP Company Parameters form
 (Audit Options tab, Purchase Orders section):

- Allow
 transactions to exceed item line's current total cost

- Allow
 transactions to exceed item's current total cost

- Allow
 transactions to exceed PO's current total cost

- Allow invoiced to exceed PO Item Line
 received

- Allow
 invoiced to exceed PO Item received

If any of the checkboxes are not selected, you will be unable
 to post the batch until you correct the invoiced amounts.Note:
 For unapproved invoices (AP Unapproved Invoice Entry), the validation procedure
 includes invoiced amounts in unposted AP batches as well as other unapproved invoice
 months/sequences. Additionally, if any of the checkboxes are not selected, the system will
 add approved invoices to the batch. However, you must correct the invoiced amounts
 before posting the batch.

When invoicing a purchase
 order, the GL
 Acct field defaults from the purchase order item. For PO items
 referencing an SM work order, this field is disabled.
If the PO
 item is for a job, the GL account defaults as follows:

- If you did not select the
 Allow GL Account override when posting costs checkbox in the
 JC Company Parameters form (GL Cost tab), and the Job’s status is open
 (Job
 Status field, JC Jobs form), the GL account defaults from the JC
 Departments form.

- If you selected the Allow GL
 Account override when posting costs checkbox in the JC Company
 Parameters form (GL Cost tab), and the Job’s status is open ( Job
 Status field, JC Jobs), the GL account defaults from the
 purchase order.

- If the Job’s status is soft-closed
 (Job
 Status field, JC Jobs form), the GL account defaults from the
 Open
 WIP Acct field in JC Departments form (Cost Types tab), assuming
 that you selected the Allow Posting to Soft-Closed
 Jobs checkbox in the JC Company Parameters form.

- If the Job’s status is hard-closed
 Job
 Status field, JC Jobs form), the GL account defaults from the
 Closed WIP Account field in the JC Departments form (Cost Types
 tab), assuming that you selected the Allow Posting to Hard-Closed
 Jobs checkbox in the JC Company Parameters form.

- If you did not specify a GL
 account in the JC Departments form, the system defaults the GL account
 specified for the purchase order.

## Subcontract (Line type 7)

Use this line type
 when the line applies to a subcontractor invoice. When you select this option, the system
 displays the SL, SL Item#, JCCo,
 Job, Phase, and CT fields.These invoices
 use the information set up in the SL module and let you fill in the rest of the details
 from the vendor's invoice. Keep in mind that if you have set up subcontractor purchase
 orders in the PO module, you must use the Job transaction type for that payable
 invoice.
When you create subcontract
 invoices, the system prompts for the subcontract item to be paid. The system then
 displays the item's assigned job, phase, cost type (as set up in SL), and the
 job/phase/cost type's UM (as set up in JC). You cannot change the Job,
 Phase, CT, or UM
 fields.
The system verifies the
 dollar amounts that you enter for each item to make sure that they do not exceed the
 total cost of the subcontract or subcontract item. If the items do exceed the total
 cost, the system displays a warning. If you selected the Allow transactions to
 exceed current total cost checkbox in the AP Company Parameters form
 (Audit options tab, Subcontracts section), the system allows line amounts to exceed the
 current total cost of a subcontract or subcontract item.Note: For
 unapproved invoices (AP Unapproved Invoice Entry), the validation procedure includes
 invoiced amounts in unposted AP batches, as well as other unapproved invoice
 months/sequences. Additionally, if you did not select the Allow transactions to
 exceed item's current total cost checkbox in the AP Company
 Parameters form, the system will add approved invoices to the batch. However, you
 must correct the invoiced amounts before posting the batch.

When invoicing a subcontract item, the GL Acct
 field defaults based on the following:

- If you did not select the
 Allow GL Account override when posting costs checkbox in the
 JC Company Parameters form (GL Cost tab), and the Job’s status is open
 (Job
 Status field, JC Jobs form), the GL account defaults from the JC
 Departments form.

- If you selected the Allow GL
 Account override when posting costs checkbox in the JC Company
 Parameters form (GL Cost tab), and the Job’s status is open (Job
 Status field, JC Jobs form), the GL account defaults from the
 subcontract item.

- If the Job’s status is soft-closed
 (Job
 Status field, JC Jobs form), the GL account defaults from the
 Open
 WIP Acct field in the JC Departments form (Cost Types tab),
 assuming that you selected the Allow Posting to Soft-Closed
 Jobs checkbox in the JC Company Parameters form.

- If the Job’s status is hard-closed
 (Job
 Status field, JC Jobs form), the GL account defaults from the
 Closed WIP Account field in the JC Departments form (Cost Types
 tab), assuming that you selected the Allow Posting to Hard-Closed
 Jobs checkbox in the JC Company Parameters form.

- If you did not specify a GL
 account in JC Departments, the system defaults the GL account specified for the
 subcontract item.

## SM Work Order (Line type 8)

Use this line type
 for expenses that apply to an SM work order. When you select
 this option, the system displays the SM Co, SM Work Order,
 SM
 Scope, and SM Cost Type fields. If the work order is
 for a job, the screen will also display a JC Cost Type field.Note: If you specify a work order scope that has not been assigned a
 call type, rate template, and/or phase (for job work orders), and you entered the line
 in:

- the AP Transaction Entry form, you will
 receive a warning that this information is required before work completed can
 be entered for the scope. You will be unable to save the record until the
 required information has been entered for the work order scope in SM Work
 Orders.

- the AP Unapproved Invoice Entry form, you
 will be able to save the record; however, you will be required to enter this
 information in SM Work Orders for the specified scope before you can post the
 invoice in the AP Unapproved Invoice Posting form.

If you specify a work order scope that is closed, and you
 entered the line in:

- the AP Transaction Entry form, you will
 receive a warning that the scope is closed. You will be unable to save the
 record until you either reopen the scope or change to a scope that is open.


- the AP Unapproved Invoice Entry form, you
 will be allowed to save the record; however, you will be unable to post the
 invoice in the AP Unapproved Invoice Posting form.

For job-related work orders, if you specify and
 job-related work order and the job has been soft or hard-closed, the system will handle
 the invoice line based on how you set the Allow Posting to Soft-Closed Jobs and
 Allow Posting
 to Hard-Closed Jobs checkboxes in the JC Company Parameters form):

- AP Transaction Entry - If you
 allow posting to hard and/or soft-closed jobs (appropriate checkbox is selected in
the JC Company Parameters form), you will be able to save the invoice line. If you
 do not allow posting to closed jobs (applicable checkbox is not selected), a message
 displays indicating the job is closed and you will be unable to save the
 record.

- AP Unapproved Invoice Entry - The
 system will allow you to save the invoice line regardless of whether or not you
 allow posting to closed jobs; however, if you do not allow posting to closed
 jobs, you will be unable to post the invoice in the AP Unapproved Invoice
 Posting form.

Once you process the invoice batch via AP Batch Process or AP Unapproved Invoice Posting (unapproved invoices only), the system auto-generates work completed Misc lines (in SM Work Orders) for each invoice line assigned this line type. The units, unit cost, gross, and tax values for the invoice line will become the cost values (Cost Qty, Cost Rate, Cost Subtotal, Cost Tax Type, Cost Tax Code, Cost Tax Basis, Cost Tax Amt, and Total Actual Cost) for the work completed line.
For Australian and Canadian Companies, if you specify a non-job SM
 work order, the system will automatically set the Tax Type to 3-VAT for the work
 completed miscellaneous line generated in SM Work Orders. The tax code for the work
 completed line will default from the Service Center or Service Site (depending on the
 Tax Source specified for the work order) and must be a VAT-type code.

- AP Transaction Entry - If you
 allow posting to hard and/or soft-closed jobs (appropriate checkbox is selected in JC
 Company Parameters), you will be able to save the invoice line. If you do not
 allow posting to closed jobs (applicable box is unchecked), a message displays
 indicating the job is closed and you will be unable to save the record.

- AP Unapproved Invoice Entry - The
 system will allow you to save the invoice line regardless of whether or not you
 allow posting to closed jobs; however, if you do not allow posting to closed
 jobs, you will be unable to post the invoice in AP Unapproved Invoice
 Posting.Note: This functionality will only apply if
 the SM company's AR company (defined in SM Company Parameters) is set up
 with a Default Country of AU or
 CA in HQ Company Setup.

Related information

- [AP Purchase Order Initialize Form](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/accounts-payable-invoice-forms/ap-purchase-order-initialize-form)

- [AP Unapproved Invoice Entry Form](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/ap-unapproved-invoice-forms/ap-unapproved-invoice-entry-form)

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)

- [JC Company Parameters Form](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/jc-company-parameters-form)

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
