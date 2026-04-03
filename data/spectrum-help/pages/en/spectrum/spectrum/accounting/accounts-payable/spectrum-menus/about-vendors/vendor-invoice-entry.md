---
title: "Vendor Invoice Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry"
---

# Vendor Invoice Entry

Use this screen to record invoices (including unapproved, unposted, standard, subcontract, etc.) and credit memos (including subcontract back charges).
For new transactions, the software determines whether the invoice is related to a purchase order or subcontract in the current company.

## Key Features

- One invoice may be distributed to multiple G/L accounts, jobs, phases, and cost types.

- Information about the current batch of unposted invoices continuously displays: including the number of invoices and credit memos, and the total dollar amount currently contained in the batch.

- A routing history record is created for every new invoice, including those that are added as unposted, in order to provide an audit trail.

- Unapproved items can be immediately confirmed by operators who have access to the unapproved list of other operators. Unposted items can also be sent back to the approval process, regardless of whether they were originally entered as an unapproved or not. To perform either of these options, the operator must have security to enter unposted invoices and unapproved invoices. Unapproved invoices are always included in the Week-to-Date column of the Job Cost reports. After you entered the Vendor, Invoice # and Entry type the software will determine whether you are authorized to access other reviewers' invoices based on the View unapproved invoices assigned to other operators checkbox setting in Operator Maintenance. If this checkbox is selected, you will be permitted to access the invoice. If this checkbox is not selected, the software will determine whether the you are the 'Current reviewer' assigned to the requested invoice. The software will permit limited access operators to view invoices when assigned to any reviewer. Once this screen has been completed, the [A/P Unapproved Invoice Detail](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/ap-unapproved-invoice-detail) window automatically displays.

- Subcontract progress billings, back charges, and standard invoices that reference a subcontract number can be entered directly in this screen. Subcontract progress billings can be routed for approval before locking in billing item quantities and amounts.

- Purchase order receiving by either one-step method (invoice) or two-step method (invoice + packing list). If the Update to packing list to jobs before invoicing option is selected in Purchase Order Installation, in the two-step method the invoice is matched up against the packing lists and the material cost is trued up on the job during the A/P Transaction Register Update. If the PO was accrued previously, additional items (freight or other charges) may be added, but they won't be accrued. Instead, they will be charged directly to the entered G/L charge line.

- Record adjustment invoices to reclassify costs on a posted invoice. During the [A/P Transaction Update](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/ap-transaction-update) the so-called zero-dollar invoice will be sent directly to Vendor History (rather than become an 'open item' for future payment).

- Print a [Subcontract Progress Billing Detail](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-progress-billing-detail) when saving a new progress billing.

- If an out-of-balance condition is detected, an interactive window displays and provides options for resolving the discrepancy.

More info on correction options:
ButtonsDescriptions
Set to Detail (on Total before tax)Click to change the amount in the heading to match the distributed amount (instead of requiring you to navigate to the 'Total before tax' field in the heading).
Set to Detail (on Sales tax)Click to change the amount in the heading to match the calculated tax amount (instead of requiring you to navigate to the 'Sales tax' field in the heading).
Allocated difference (on Sales tax)Use this button when the sales tax amount entered in the heading is the correct value, (that is, what is shown on the invoice and what needs to be paid). When clicked, the software allocates the difference between what the tax stated on the invoice and the sum of what calculated from all the detail lines with sales tax codes assigned.
Exception: Allocation is not permitted if a no tax amount has been entered in the heading but a sales tax code has been assigned to one or more distribution lines in the grid.

- Security settings determine if you can add, edit, or delete invoices (including unapproved and unposted invoices) in this screen. You cannot delete items that were generated from Purchase Order Receiving in this screen.

- Invoices and credit memos can only be changed before they have been posted using the [A/P Transaction Update](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/ap-transaction-update) that follows the [A/P Transaction Register](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register). Once invoices have been posted, any corrections that need to be made can be made only with additional transactions.

- Sub-tier vendor item tracking will place new invoices on hold whenever any of its sub-tier vendors are flagged for hold status (triggered by [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) action #3).Note: Vendor Invoice Entry warns you when [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance) include actions #2 and #3.

[Using Batch Scanning with Invoice Entry](http://www.screencast.com/t/rp18JrYF)
[Learn about Auto-Signature Checks](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/b96c5fa0-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiJiOTZjNWZhMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjg0MjgsImp0aSI6ImNmNTdhNWE5OGE0MTQ5MmNhN2YxNTllNGE3NjU0Yjk1IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.3nZLYEva-mn70ADSbOZbE9lV9GmdG4xbb_ImZGRU36s&response-content-disposition=filename%3D%22Auto-Signature_Procedures_v1422_1.pdf%22)
[Learn about Auto-Signature Cheques](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/b9b9e360-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiJiOWI5ZTM2MC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjg0MjgsImp0aSI6Ijc5MTA3MWYzNWI0NzRmYjY5Mjg4ZTZkMjU5NjIzMzgxIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.dWYNrZqkeDQqPvYa0Yd_yNNgD1OBMEafWqbBJHffesE&response-content-disposition=filename%3D%22Auto-Signature_Cheques_Procedures_v1422_1.pdf%22)
[View the Vendor Invoice Import manual](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9ad0ae20-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YWQwYWUyMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjg0MjgsImp0aSI6Ijk3MTQzOTI5YzE2ZjQ2OTU4ODRmZmZmMjZlZDlhNzY3IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.nF5OM5VN23LmfsOYRBH-advZaf840gOUqoSSklsGkZE&response-content-disposition=filename%3D%22Vendor_Invoice_Import_Manual_v1422.pdf%22)
[Accruing Job Purchase Orders](/en/spectrum/spectrum/accounting/purchase-order/spectrum-menus/data-entry-overview/purchase-order-entry/accruing-job-purchase-orders)

Related information

- [Vendor Invoice Entry - Field Descriptions: Invoice Header Fields](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-invoice-header-fields)

- [Vendor Invoice Entry - Pre-Paid Details](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/vendor-invoice-entry/vendor-invoice-entry---pre-paid-details)

- [Vendor Invoice Entry - Field Descriptions: Payment Plans Fields](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-payment-plans-fields)

- [Vendor Invoice Entry - Field Descriptions: Grid Entry Fields](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-grid-entry-fields)

- [Vendor Invoice Entry - Field Descriptions: Subcontract Fields](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-subcontract-fields)

- [Vendor Invoice Entry - Field Descriptions: Purchase Order Fields](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry/vendor-invoice-entry---field-descriptions-purchase-order-fields)

- [Enter a Vendor Invoice](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/enter-a-vendor-invoice)

- [A/P Transaction Register](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-transaction-register)

- [Reverse Vendor Invoice](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/reverse-vendor-invoice)

- [Subcontract Progress Billing Detail](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-progress-billing-detail)

- [Invoice and Credit Memo Procedures](/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/invoice-and-credit-memo-procedures)

- [Invoice Entry Flow Chart of Cost Center Defaults](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-hierarchies/invoice-entry-flow-chart-of-cost-center-defaults)
