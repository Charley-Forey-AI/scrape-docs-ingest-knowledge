---
title: "About the Invoice Summary Level | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/about-the-invoice-summary-level"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/about-the-invoice-summary-level"
---

# About the Invoice Summary Level

You can define at what level work completed should be summarized on SM invoices using the Invoice Summary Level drop-down in the SM Customers form.
The Invoice Summary Level controls how work
 completed detail is summarized on invoices for the customer. Summary level options
 are:

- L-Line — This option summarizes invoice detail at the line level. For each scope
 on a work order, the system summarizes all work completed lines of the same type
 (Labor, Equip, Part, and Misc) and print the totals in their respective columns
 on the invoice (Labor, Equipment, Parts, and Other).

- C-Cost Type — This option summarizes invoice detail at the cost type level. For
 each scope on a work order, the system summarizes all work completed lines
 referencing the same cost type and print a single line for that cost type on the
 invoice. Totals for work completed lines with no cost type assigned are printed
 first, under the heading of "***NO COST TYPE***".Note: You will typically only
 use this option if you assign cost types to work completed
 lines.

- T-Transaction — This option will summarize invoice detail at the transaction
 level. For each scope on the work order, the system will print a separate line
 for each work completed line associated with the scope.

Note: You can override this setting by invoice in SM Invoice Review.
