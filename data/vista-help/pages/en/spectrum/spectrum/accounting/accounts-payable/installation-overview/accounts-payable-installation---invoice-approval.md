---
title: "Accounts Payable Installation - Invoice Approval | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---invoice-approval"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---invoice-approval"
---

# Accounts Payable Installation - Invoice Approval

The Invoice Approval Routing process allows you to optionally track invoices by routing them through reviewers for approval.
To activate, set up, and use the invoice approval process:

- Activate the approval process.

- Set up one or more Routing Codes, each with its own sequence of
 reviewers, using the [Invoice Approval Routing Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/invoice-approval-routing-maintenance) screen.

- Use
 the Invoice Approval screen to view and to approve, edit, or reject invoices that have been
 entered and routed.

Fields/ButtonsDescriptions
Use Invoice Approval Processing?Select this checkbox if you want to use the Invoice Approval process.If this checkbox is not selected, the A/P invoice approval section in Job Cost > Job Setup is shaded and disabled.
Selecting this checkbox enables the option for invoices to be added to the unapproved invoice processing files, even when created outside the AP module, for example, Materials Management freight and material purchases, Payroll amounts, and Purchase order receiving. Otherwise, all invoices are added to Invoice / Credit Memo Entry.

Set invoice to unposted when no routing code defaults?Select this checkbox if you want invoices automatically sent to an A/P batch in A/P Vendor Invoice Entry when there is no routing code default. When this checkbox is selected, the system determines whether the imported AP invoice will be routed or not.
Standard default routing codeRouting codes are used to determine the order in which invoices are reviewed.
Invoice dollar limit
Routing code over limit
The dollar limit which should trigger the use of the over-limit routing code, and the routing code to use when an invoice amount exceeds the dollar limit. If there is no established invoice dollar limit, leave this field blank.Note: You can opt to leave both fields blank and instead manage the approval routing by entering Approval Limits on the Routing Code. For additional information, see [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits).

Default security for new operatorsEnter the default security level assigned to new employees.
Operator Security
Code NameThe reviewer code and name.
Security levelLists invoice approval security levels for users. This column shows only those operators who have
 security for the Invoice Approval screen.Use the drop-down menu at the Security level field to
 select the level of editing permitted in the Invoice
 Approval Distribution window (located in Invoice
 Approval).
In Function Security
 Maintenance separate security settings are available for the
 Vendor Invoices screen for the New
 Invoice and Delete Invoice features,
 and to restrict users from editing the header fields of an existing invoice
 (including the sub-windows).
Note: Security for Invoice Approval can also be set up in Operator
 Maintenance.

Access all lists?Select the Access all lists checkbox for those operators who will be
 permitted to access the unapproved invoices of other reviewers in the
 Invoice Approval screen (located on the
 Accounts Payable Data Entry menu).Note: Security for Invoice Approval can also be set up in Operator
 Maintenance.
