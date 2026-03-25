---
title: "About the HQ Payment Terms Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form"
---

#  About the HQ Payment Terms Form

Use this form to set up the various payment terms used by your
 company.
Payment Terms are used to determine due dates, discount dates, and discount rates for customers and vendors when posting transactions in Accounts Payable, Accounts Receivable, Job Billing, and Material Sales.
 Once the payment terms are set up, each customer is
 assigned a default payment terms code in the AR Customers, and each vendor a default
 payment terms code in the AP Vendors.
 Payment terms are referenced in several programs
 throughout the system. For example, payment terms may be specified when setting up a
 contract in JC Contracts, or when entering a purchase order in PO Purchase Order Entry.
 Any transactions posted that reference payment terms, will use the information set up
 for the specified payment terms to calculate due dates, discount dates, and to implement
 discount calculations.
 Examples of Payment Terms Codes: CodePayment Terms Description
N30Net 30 Days. Payments are due in full 30 days past the invoice date.
2%2% 10th, Net 30th. If payment received by 10th day of the following month, a 2% discount can be taken. Otherwise, net amount is due 30 days past invoice date.

 The Check Date Defaults section allows you to test defaults based on a specific invoice date. Once you have selected an invoice date to test, click the Calc Dates button. The Discount Date and Due Date fields will default values based on the current pay terms setup.
The Sample Defaults tab uses the pay terms setup to provide a list of sample discount and due date defaults for invoices posted on each day of a month (in the current year). If either the Discount Date or Due Date is set to "None", that column will display as null in the grid.

Related information

- [Discounts](/en/vista/vista/administration/headquarters/payment-terms-setup/discounts)

- [Due Dates, Discount Dates, & Cutoff Dates](/en/vista/vista/administration/headquarters/payment-terms-setup/due-dates-discount-dates--cutoff-dates)

- [How the System Uses Payment Terms](/en/vista/vista/administration/headquarters/payment-terms-setup/how-the-system-uses-payment-terms)
