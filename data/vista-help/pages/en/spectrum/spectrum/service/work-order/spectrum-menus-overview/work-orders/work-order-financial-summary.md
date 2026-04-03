---
title: "Work Order Financial Summary | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-financial-summary"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-financial-summary"
---

# Work Order Financial Summary

Use the Work Order Financial Summary
 screen to view invoice financial information for a specific work order. To access this screen,
 select Work Order Info Bar > Financials > Summary.

- For 'job' work orders, invoice totals to be paid by the customer
 and profitability amounts will display on this tab. Billing and cost values and the
 listbox showing billing records will not be shown for 'job' work orders.

- For 'site' work orders this tab will show both unbilled and
 billing history, plus amounts available for billing. The top half of this tab will
 display view-only billing, revenue and profitability amounts. This section will not
 display cost information if the operator's 'WO security' level is lower than the
 level assigned to 'Labor Hours - Cost History tab'. The lower-half of this tab will
 display a listbox of billings-to-date, sorted by bill # in reverse order, so the most
 recent bill will show at the top of the list. The first columns of the listbox (Bill
 #, Customer, Invoice # and Type) are from the Billing History Table, and the
 remaining columns will show information from the associated records in A/R.

- When you are finished reviewing the financial summary and want to
 create the Accounts Receivable invoice, click the Bill Now
 button at the top of the screen.

Note: You can quickly navigate between Work
 Order screens via the Info Bar links, or use the
 hot-key equivalents on the command bar.

Field/Button
Description

Work order
The selected work order # and
 description display here. Any site alerts for the work order will display to
 the right of this field, if applicable.
Quote
The work order amount quoted to the
 customer will display in this field. If this amount is 0 or left blank, this
 field will display 'Not specified'.
Billings and cost

Unselected
This row will summarize transactions
 entered in Purchase Order Entry or Pre-Time
 Card Entry, but have not yet been selected for billing. It will
 also include transactions stored in the Work Order Cost History Table added
 during the A/P invoice Update, the Payroll Update or the G/L Journal Entry
 Update that have not yet been selected for billing. Unbilled time card entries,
 unapproved A/P invoices and unposted A/P invoices that are flagged as
 'Available for billing' will also be included.
Current billing
This row will summarize transactions
 currently recorded in the Labor Hours Entry, Material Entry, Other Charges
 Entry and the Task tab of Work Order Entry. These transactions represent the
 amount that will update to A/R when the Create A/R Invoice update is performed.
  In the Tax column, the Current billing total is the tax calculation
 for transaction records that have not yet been invoiced.

Total unbilled
This row is the summary of the
 Unselected and
 Current billing
 rows.
Billed-to-date
This row will summarize the total
 invoices-to-date on the work order. In the Tax column, the
 Billed-to-date total is the sum of all tax amounts for credit memos.


Total sale
This row is the sum of the Total unbilled and Billed-to-date rows.
Standard Cost
Click this button to open the [Standard Cost Inquiry](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-financial-summary/standard-cost-inquiry) screen to view
 profitability figures.
Estimated cost
This row will summarize the cost of
 open purchase orders written for a specific work order and all material entered
 via the Material Entry and New Material
 Entry screens. These costs are separated from the unposted
 costs, because it is unreasonable for these costs to change by the time the
 actual costs are booked. The open purchase order cost
 basis will be calculated as the sum of the outstanding balance due all open
 P.O. detail lines referencing the current work order. The cost basis will
 exclude any closed purchase orders, or purchase orders where the quantity
 received is equal to or greater than the quantity ordered. Use tax will be
 added if the purchase order detail line or A/P invoice detail line
 references a use tax code.
The entered material
 calculations cost basis will be calculated as the cost of all applicable
 material billing transaction entries referencing an inventory item using
 standard cost. The cost basis will exclude material entries that have
 already been invoiced, and material entries originally created by selecting
 from purchase orders or cost history. For material items subject to use tax,
 include the cost of use tax based on the estimated cost amount.

Unposted cost
This row will summarize costs for
 transactions (excluding estimated costs) that have been entered but not yet
 updated to General Ledger and Work Order Cost modules.

- The Labor amount will include the cost basis of entered labor
 billing transactions and pre-time card transactions. The labor cost basis
 will be calculated by including the cost of certain unbilled work order
 labor transactions currently present in Labor Hours Entry, excluding
 labor that has already been invoiced and labor entries originally created
 by selecting from Pre-Time Card Entry or Cost History. Otherwise, the
 labor cost basis with burden will be calculated either by summing
 estimated pay extension plus burden from setup in Technician
 File Maintenance and other Work Order
 Maintenance screens, or from Work Order
 Installation setup:

- Standard Cost: When the percentage is set to
 0.00 (or blank) for 'Unposted time card burden percent' or 'Payroll
 burden percent', the burden calculation for unposted cost
 calculation will be determined based on either hourly or percent
 settings in Work Order > Technician Maintenance.

- Actual Cost: When the percentage is set to
 non-zero, the burden calculation will use the installation
 percentage.

- If the 'Payroll overhead' option is selected
 for the work order, unposted costs from Pre-Time Card Entry will be
 calculated and then increased by the specified overhead percentage
 or rate/hour amount.

- The Material amount will include material costs from
 Accounts PayableInvoice
 Approval and unposted transactions in AP
 Invoice/Credit Memo Entry. For material items subject to
 use tax, include the cost of use tax based on the unposted cost amount.

- The Other amount will use the cost basis currently stored in
 the unbilled transaction by summing the cost of all applicable other
 charge billing transaction entries with a Source = Entry, excluding other
 charges that have already been invoiced and other charge entries
 originally created by selecting from cost history. The labor cost basis
 is comprised of two amounts: labor cost extension and burden. The burden
 calculation will vary depending upon whether the option selected on the Work Order Installation > Labor tab:

- Standard Cost: When the percentage is set to
 0.00 (or blank) for 'Unposted time card burden percent' or 'Payroll
 burden percent', the burden calculation for unposted cost
 calculation will be determined based on either hourly or percent
 settings in Work Order > Technician Maintenance.

- Actual Cost: When the percentage is set to
 non-zero, the burden calculation will use the installation
 percentage.

- The Total amount will include additional unposted amounts
 added to Unposted labor cost, Unposted material cost and Unposted other
 charge cost.

Actual cost
This row will summarize "accounting
 costs" that have been entered and posted to direct work order cost General
 Ledger codes. For material items subject to use tax, include the cost of use
 tax based on the posted cost amount. The Net profit total
 is the difference between Total sale and Actual cost. The associated percentage is calculated as
 [Total sale - Actual cost] divided by Total sale times 100.

Total cost
This row is the sum of the Unposted cost and Actual cost.

- The Labor amount will include additional unposted amounts
 added to Unposted labor cost. If labor costs from Labor Hours Entry were
 not included in the unposted labor cost amount, they will not be included
 in this amount either.

- The Material amount will include Estimated material cost. If
 material costs from Purchase Order Entry and Material Entry were not
 included in the estimated material cost, they will not be included here
 either.

- The Other amount will include additional unposted amounts
 added for Unposted other charge cost.

- The Total cost amount will include additional estimated
 material cost and unposted amounts conditionally added to Unposted labor
 cost and Unposted other charge cost in the calculations.

- The Net profit amount will include additional estimated
 material cost and unposted amounts conditionally added to unposted labor
 cost and unposted other charge cost. The profit calculation is the
 difference between Total sale and Total cost. The associated percentage
 is computed as [Total sale - total cost] divided by Total sale times 100.


A/R Invoice
Click this button to open the [Accounts Receivable Invoice Inquiry](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/inquiries-overview/accounts-receivable-invoice-inquiry) window to view general financial information about the invoice.
Billing Detail
Click this button to open the [Work Order Billing History Inquiry](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-financial-summary/work-order-billing-history-inquiry) window to
 display billing summary information and a history of transactions associated
 with the specified bill #.

Related information

- [Create A/R Invoice](/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/work-orders/work-order-financial-summary/create-ar-invoice)
