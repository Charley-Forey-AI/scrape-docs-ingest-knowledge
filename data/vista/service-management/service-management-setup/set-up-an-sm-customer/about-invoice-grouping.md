---
title: "About Invoice Grouping | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/about-invoice-grouping"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/about-invoice-grouping"
---

# About Invoice Grouping

The Invoice Grouping feature in Service Management controls
 how the system generates invoices for customer work orders and agreement work orders using
 Time of Service billing.
Invoice grouping is defined at the customer
 level (in SM Customers) and/or the service site level (in SM Service Sites).
You can specify to create a separate invoice
 per customer (in SM Customers only), service site, work order, or work order scope. When
 generating invoices (via SM Work Order Billing), the system will group billable work
 orders on the same invoice based on the setting you selected. For example, if you
 specify to create a separate invoice per service site, the system will group all
 billable work orders posted to the same service site together on the same invoice.
Note: The option selected here determines the options
 available for selection in the Deliver To field. See the [F1](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form/field-definitions-sm-customer-form#ID-00042c5a--en) help for more information.
The following exceptions take precedence over the Invoice Grouping setting defined for
 a customer or service site:

- PO Override - This setting applies to work order
 scopes that reference a customer PO number. If you selected the PO
 Override checkbox in SM Customers, during invoice generation,
 the system groups all work order scopes with the same "bill to" customer and
 same customer PO number on the same invoice.
If you set up a PO Override by service site (that is, you selected Yes
 in the PO Override field in SM Service Sites), the system groups work
 order scopes for the service site that reference the same bill to customer and
 customer PO number, on the same invoice.

- Bill To Customer - Each work order
 scope is assigned a Bill To customer. If the bill to customer differs by work
 order scope, the system handles invoice generation as follows:

- C - One per customer — The system creates a separate invoice for each
 unique customer / bill to customer combination. All customer work order
 scopes that reference the same Bill To customer are grouped together on
 the same invoice.

- S - One per service site — The system creates a separate invoice for
 each unique customer / service site / bill to customer combination. All
 work order scopes sharing the same customer, service site, and bill to
 customer are grouped together on the same invoice.

- W - One per work order — The system creates a separate invoice for each
 unique customer / work order / bill to customer combination. All work
 order scopes sharing the same customer, work order, and bill to customer
 are grouped together on the same invoice.

- P-One per work order scope — The system creates a separate invoice for
 each work order scope.

- Custom Invoice Report - If a
 customer has multiple service sites, you have the option to assign a custom
 invoice report to each service site. If the custom invoice reports differ, the
 system will handle invoice generation as follows.

- C - One per customer — The
 system creates a separate invoice for each unique customer / custom
 invoice report combination. All work order scopes sharing the same
 customer and custom invoice report are grouped together on the same
 invoice.
If the bill to customer differs by work order scope, the system creates a
 separate invoice for each unique customer /custom invoice report /bill
 to customer combination. All work order scopes that share the customer,
 custom invoice report, and bill to customer are grouped together on the
 same invoice.

- S - One per service site — The system uses the custom invoice report for all
 scopes on a work order, since service site designation is at the work order
 level, not the work order scope level. The system creates a separate invoice
 for each service site and groups all work order scopes for the customer that
 share the same service site on the same invoice.If the bill to customer
 differs by work order scope, the system creates a separate invoice for
 each customer / service site / bill to customer combination. All work
 order scopes sharing the same customer, service site, and bill to
 customer are grouped together on the same invoice.

- W - One per work order — The system uses the custom invoice report for all
 scopes on a work order, since service site designation is at the work order
 level, not the work order scope level. The system creates a separate invoice
 for each work order; all scopes on the work order will be grouped together
 on the same invoice.If the bill to customer differs by work order scope,
 the system creates a separate invoice for each customer / work order /
 bill to customer combination. All work order scopes sharing the same
 customer, work order, and bill to customer are grouped together on the
 same invoice.

- P - One per work order scope — If you selected this option, the system will
 create a separate invoice for each work order scope.
