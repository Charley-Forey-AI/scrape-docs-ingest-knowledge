---
title: "About the AR Purge Paid Invoices Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-purge-paid-invoices-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/about-the-ar-purge-paid-invoices-form"
---

# About the AR Purge Paid Invoices Form

You can use the AR Purge Paid Invoices form to purge paid invoices from the Accounts Receivable system for customers with Open Item accounts. You also have the option to purge temporary and inactive customers.
When purging paid invoices, the following applies:

- All batches (for all users) that have posted transactions in any of the AR posting programs (Invoice Entry, Cash Receipts, Finance Charge, and Release Retainage) must be closed. If there are any open batches, you must run The AR Batch Update program before you can proceed here.

- You can only purge invoices for closed months.

- You can only purge invoices by customer or by contract. If purging invoices by customer, you have the option to exclude invoices that have contracts.

- The system purges all fully applied (paid) invoices through the specified month.

- The system purges On-account payment detail that nets to zero.

- If a customer’s Selective Purge option (AR Customers) is selected, the customer will be skipped.

## When is an invoice available for purging?

In order to purge an invoice, the transaction and each line item, if applicable, must have been fully paid. The month in which the final payment was applied to the invoice is the month that the invoice is available for purging and must be included when the Purge Through Month is specified.

## How often do you need to purge?

Keep paid transactions as long as they are needed. It is suggested that you determine how long to store paid transactions and create a purge cycle that will accommodate your needs.

## What gets purged and how does it affect other modules?

When an invoice is purged, all detail related to the invoice is deleted. This includes any adjustments, credit memos, or write-offs applied to the invoice. The system only purges the information from the AR files, ARTH (Transaction Header) and ARTL (Transaction Lines). Purging in this program does not affect information that has already been interfaced to other modules (CM, JC, and GL) during the posting process. Note: If there are Miscellaneous Distributions associated with purged invoices, they must be purged separately in AP Miscellaneous Purges.

## Purging Temporary and Inactive Customers

These options allow you to purge temporary and/or inactive customers from the AR files. Temporary customers are those customers whose Temporary Customer option is checked in AR Customers (Info tab). Inactive customers are those customers whose Status in AR Customers (Add'l Info) is set to Inactive.
When either of these options are selected, all information related to the selected customer (static information, invoices, and payments) is deleted. In addition, monthly totals for the AR company and customer will be cleared, as long as no transactions exist for the customer and AR company. If no other companies have monthly totals for the customer, the customer will then be purged from the AR files.
If you are purging a customer from a Customer Master that is shared by multiple companies, you will need to purge the invoices and monthly totals for the customer in all of the companies sharing the master file. Only then will the 'temporary' and/or 'inactive' customer be deleted from the Customer Master.
