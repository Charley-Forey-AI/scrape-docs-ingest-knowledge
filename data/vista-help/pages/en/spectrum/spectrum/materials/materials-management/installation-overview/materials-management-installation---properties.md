---
title: "Materials Management Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/installation-overview/materials-management-installation---properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/installation-overview/materials-management-installation---properties"
---

# Materials Management Installation - Properties

Use this tab to install properties information for the Materials Management module.
Fields
Descriptions

Post to invoice as one ticket per line?`
Invoice detail lines may be created in two ways. Select this checkbox to create an invoice detail line for each scale ticket.
If this checkbox is left clear, then the invoice detail lines will group scale tickets together by item code, creating fewer detail lines.
This affects the way customer scale tickets are posted to both Order Processing and Accounts Receivable invoices. Using either posting method, the source ticket number(s) will be recorded on the message line of invoice detail lines for audit purposes.

Integrate scale tickets to Inventory Control?
If you select this checkbox, the scale tickets with a job number will create job requisitions in the Job Requisition Entry screen.
This selection affects only job scale tickets; customer tickets will not create job requisitions.

Post to job requisition in detail?
Select this checkbox to post job requisitions in detail when the Scale Ticket Journal Update is performed. This will create one job requisition for every Batch Code, Job Number, Job Company and Order number combination that exists.
If this checkbox is not selected, the update will post job requisitions in summary. This will create one job requisition per scale ticket, regardless of whether it has the same Batch Code, Job Number, Job Company and Order Number combination or not.

Separate freight billing item on invoices?
If you select this checkbox, then any freight charges will be summarized as separate non-stock invoice lines from the material charges. The non-stock item code will default based on the hauler code file.
If you leave this the checkbox clear, then the freight charges will be summarized into the total billing for the material line item. Be aware that freight lines cannot be bundled on invoices from Materials Management if the tax flags or the G/L account codes on the lines are different.
This entry may be overridden for individual customers in the Materials Management Customer Material Contract Maintenance. This entry will default if no customer contract has been set up in that file. This entry applies only to customer scale tickets; job tickets will always assign freight charges to separate non-stock lines.
The Materials Management update to Order Processing automatically creates a separate line for "freight" when this checkbox is selected. If this checkbox is not selected, a separate "freight" line is only created if there is estimated cost set up in Hauler File Maintenance or Customer Material Contract Maintenance. In this case, the sales extension of this line is $0.00.
If the separate freight checkbox is not selected:

- if freight bill > $0.00, and the cost = $0.00, then 1 line will be created for the sale

- if freight bill = $0.00, and the cost > $0.00, then 2 lines will be created for the sale

- if freight bill = $0.00, and the cost = $0.00, then 1 line will be created for the sale

- if freight bill > $0.00, and the cost > $0.00, then 2 lines will be created for the sale
If the separate freight checkbox is selected:

- if freight bill > $0.00, and the cost = $0.00, then 2 lines will be created for the sale

- if freight bill = $0.00, and the cost > $0.00, then 2 lines will be created for the sale

- if freight bill = $0.00, and the cost = $0.00, then 1 line will be created for the sale

- if freight bill > $0.00, and the cost > $0.00, then 2 lines will be created for the sale

Two lines will also post to O/P if the Sales Tax Code
 Maintenance freight taxable field is not selected and the
 freight cost > $0.00 (with the billing amount on the freight bill set to
 $0.00 on the freight line).

Require quantity reconciliation?
the software is prompting you to decide whether the freight charges on scale tickets will require the hours to be adjusted or approved before they can be grouped to pay an invoice in Freight Cost Reconciliation.
If you select this checkbox, then tickets will first have to be adjusted or approved in [Freight Hours Reconciliation](/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/freight-cost-reconciliation/freight-hours-reconciliation). If this checkbox is not selected, then all selected tickets (regardless of whether they were adjusted/approved in the Freight Hourly Reconciliation) will display in Freight Cost Reconciliation and be ready for reconciliation.

Terms code for COD scale tickets
the software is prompting for a valid terms code to be used when updating customer scale tickets to the Accounts Receivable or Order Processing invoice. This entry may be left blank if no COD tickets are used. If a terms code is entered here, it must be set up in the Customer Terms Code File Maintenance screen.

Dollar limit for customer invoice generation
the software is prompting for the maximum dollar amount for any single customer invoice. This limit may be used to create several smaller invoices rather than one large one. This can be used for customers that are known to pay invoices of up to a certain amount sooner than invoices that go over that amount. If nothing is entered, then no limit will be used. This entry may be overridden in the Customer Material Contract Maintenance.

Company code for job cost
Enter the company code to be used for scale tickets associated with a job number. This field may be left blank if the Inventory Control multi-company job requisition feature is NOT being used, or if scale tickets will NOT be posting to Inventory Control. The code entered here will NOT affect scale tickets with a customer code.
The Job / Company File Maintenance screen may be set up to determine the company code in which a job is located. A selection is available on the Materials Management Utilities menu to automatically build this file from the job file. This file, however, does not allow the same job number to be used in more than one company.
This installation field will only be used if the Multi-company requisitions? checkbox is selected in the Inventory Control Installation screen. Here is the hierarchy information:

1. During the Import Scale Tickets update, or when adding tickets in the Scale Ticket Transactions screen, the job/company file will be used to determine the job company code.

1. If the job is not in this file, this Materials Management Installation field will be used for the default job company code.

1. If this field is left blank, the current company will be used for the job company code.
Note: When the multi-company code is set for Inventory Control, the job lookup
 windows in Materials Management will allow entry of a company code to
 look up jobs in other companies.

Update scale invoices to
Select the module where sales invoices will be created.

- Order Processing

- Account Receivable

This selection is used when running the Scale Ticket Update. Scale tickets with a customer code will create sales invoices in the selected module at that time. Updating to the Order Processing module will create sales invoices, not sales orders. This selection affects only customer scale tickets; job tickets will not create invoices. When tickets are updated to A/R, cost of good sold is not tracked. For operations wishing to track costs on customer tickets, this prompt should be set to Order Processing.

Default ticket type
Select the default ticket type:

- Job

- Customer
The software is prompting you to decide the default to use on reports and inquiry screens. Select Job if selection on these screens will usually be done by job. Select Customer if the selection on these screens will most often be done by customer. This entry may always be overridden at the time the report or inquiry is run.

Default period type
Select a default period type:

- Week-to-date

- Month-to-date

The software is prompting you to decide the period type to default on inquiries and reports. This entry may always be overridden at the time the inquiry or report is run.
