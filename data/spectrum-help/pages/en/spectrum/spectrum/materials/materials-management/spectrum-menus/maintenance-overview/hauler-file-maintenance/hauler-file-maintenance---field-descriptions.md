---
title: "Hauler File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/hauler-file-maintenance/hauler-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/hauler-file-maintenance/hauler-file-maintenance---field-descriptions"
---

# Hauler File Maintenance - Field Descriptions

Use the table below for reference when completing the
 fields on this screen.
Fields
 Descriptions

Hauler code
 Enter a unique code or search for an existing one
 to identify the hauler.

Properties
Description
 Enter a full description for the hauler. For
 instance, the code might be "USATRU," and the full description
 "U.S.A. Trucking, Ltd."

Vendor code
 Enter the vendor code for this hauler (or if using the company's own
 truck, press Enter to leave blank). The
 vendor code entered here must have been previously set up in the
 Accounts Payable module.
 Note:
 If the vendor's status is Not used then
 entry is not allowed.


Freight G/L category
 The freight G/L category is used to set the
 freight liability G/L code (inventory G/L) and the freight expense
 G/L code (cost of sale) when creating the customer invoices in A/R
 or O/P. For job requisitions, the direct cost G/L is used for the
 freight line items.
Enter or search for the freight inventory category code for this
 hauler, and the corresponding category code displays. The inventory
 category codes are set up and maintained in Inventory Control > Category File Maintenance.
If this field is left blank, then the software will look to the Warehouse G/L Department Maintenance for the freight general ledger category.

Nonstock freight code
 Enter the non-stock freight code to use for this
 hauler.

Nonstock freight description
 The corresponding non-stock freight description
 displays; however, you may enter another description, if
 desired.

Nonstock freight u/m
 Enter the non-stock freight item unit of measure (UM); for example:
yd=yard,
ea=each,
pd=pound, and so forth.

Post freight to job cost?
 Select to post freight to
 Job Requisition Entry; otherwise, leave this checkbox clear if
 freight charges for this hauler should not be updated to the job.
 This is handy for companies who own their own trucks and use this
 freight amount for budget purposes.
Posting to Job Cost allows these users to
 accurately calculate hourly time cards for the trucks and drivers
 involved in the freight charges.

Freight cost
Freight cost per ton rate
 Enter the freight cost per ton for this hauler.


Freight cost per hour rate
 Enter the freight cost per hour rate for this
 hauler.

Minimum cost
 Enter the minimum cost for this hauler.

Freight billing
Freight bill per ton rate
 Enter the freight bill per ton rate for this
 hauler.

Freight bill per hour rate
 Enter the freight bill per hour rate for this
 hauler.

Minimum bill
 Enter the minimum billing rate for this
 hauler.

Default freight rate type
Default freight rate type
 Select Ton if the cost rate is based on load
 weight or Hour if the cost is based on
 time.
If you select Ton for your hauler calculation
 rate, the estimated freight will be fairly accurate and the variance
 between actual and estimated is small. However, if you select
 Hour for your hauler calculation rate,
 these estimates may not be as accurate. Because hourly freight
 charges are dependent on daily time logs from drivers, the variance
 between what is estimated from the tickets and what is actually
 charged by the haulers can be large.
To account for this, the software posts the variance to the job through
 Accounts Payable, causing an estimated freight going to the job on a
 daily basis. On a more periodic basis, the actual freight also will
 be reflected in Job Cost. For example, tickets are imported and
 posted daily. When the daily time sheets come in from the drivers,
 say weekly, the Freight Hours Reconciliation
 screen is used to adjust the tickets to reflect the correct elapsed
 time. When the invoice comes in from the vendor, the tickets are
 grouped together and an A/P invoice is created. This invoice
 contains adjustments for freight variance. These will post to job
 cost during the A/P invoice update, resulting in the actual freight
 cost being posted to job cost after the A/P invoices have been
 created and updated (not necessarily paid).

A/P invoice approval
Note: The following fields are unavailable if
 the Use Invoice Approval processing
 checkbox is clear in Accounts Payable Installation >  Invoice
 Approval.

Default routing code
 Enter the default routing code, or search for
 valid routing codes.

Invoice dollar limit
Routing code over limit
The dollar limit which should trigger the use of the over-limit routing code, and the routing code to use when an invoice amount exceeds the dollar limit. If there is no established invoice dollar limit, leave this field blank.Note: You can opt to leave both fields blank and instead manage the approval routing by entering Approval Limits on the Routing Code. For additional information, see [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits).
