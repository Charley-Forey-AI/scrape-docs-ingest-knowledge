---
title: "Customer Recurring Invoices - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-recurring-invoices/customer-recurring-invoices---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/customer-recurring-invoices/customer-recurring-invoices---cost-center-information"
---

# Customer Recurring Invoices - Cost Center Information

If the cost center feature is enabled in the
 Enterprise Installation screen, Spectrum performs a series
 of cost center validations during Recurring Invoice Entry.
Spectrum will allow the operator to add a recurring invoice for a customer only
 if the operator has permission to access that customer's information.
 Spectrum compares the customer's list of shared cost centers with cost
 centers in the operator's assigned scheme; if there are no common cost
 centers, then invoice entry for that customer will be disallowed.
When the operator's scheme includes override settings for 'Job' entries in
 Cost Center Scheme Maintenance, this screen
 will validate the cost center assigned to the job based on these overrides.
 The override cost center(s) supersede the cost center list defined for the
 scheme in general. Spectrum will compare the cost center assigned to the job
 with 'Job' override cost centers in the operator's assigned scheme; if the
 cost center is not included, then entry for that job will not be
 allowed.
Spectrum will also verify that the operator has authorization for the contract. Spectrum compares the contract's cost center with cost centers in the operator's assigned scheme; if the cost center assigned to the contract is not present, then that entry for that contract will not be allowed.
When the operator's scheme includes override settings for 'Contract' entries
 in Cost Center Scheme Maintenance, this screen will
 validate the cost center assigned to the contract based on these overrides.
 The override cost center(s) supersede the cost center list defined for the
 scheme in general. Spectrum will compare the cost center assigned to the
 contract with 'Contract' override cost centers in the operator's assigned
 scheme; if the cost center is not included, then entry for that contract
 will not be allowed.
Spectrum will prompt for an invoice cost center on the main screen of
 Recurring Invoice Entry if the invoice is not
 for a job. This cost center will be used as a default during the entry, as
 well as for selection and reporting purposes following the update. As the
 cost center is recorded, Spectrum compares the customer's list of shared
 cost centers with cost centers in the operator's assigned scheme; if there
 are no common cost centers, then that cost center is not allowed. For job
 invoices, the cost center assigned to the job is displayed and no changes
 are allowed.

- At the A/R G/L account code field, Spectrum will allow entry of a G/L
 account code only if the operator entering the G/L account has permission to
 assign that code. Spectrum compares the G/L account's list of shared cost centers
 with cost centers in the operator's assigned scheme; if there are no common cost
 centers, then that G/L account cannot be assigned.

- At the Cost center field in the Recurring
 Invoice Detail portion of the screen, for job
 invoices, Spectrum will display the cost center of the job and
 no changes will be allowed. At the Cost
 center field in the Recurring
 Invoice Detail portion of the screen, for
 non-job invoices, Spectrum will default the cost center
 specified in the invoice header. The operator will be allowed to
 change the cost center to another authorized cost center when it
 defaults from the contract or equipment.

- At the G/L account field in the Invoice
 Detail portion of the screen, Spectrum will
 verify the cost center assigned to the G/L account coed by
 comparing the entry to the list of allowed cost centers for that
 G/L account. Spectrum compares the G/L account's list of shared
 cost centers with cost centers in the operator's assigned
 scheme; if there are no common cost centers, then that G/L
 account code is not allowed. Validation is also performed if the
 operator attempts to change or delete an existing distribution
 line. In addition, the cost center assigned to the detail line
 must be valid for the G/L account code assigned to that
 line.

- At the Equipment code field in the Invoice
 Detail portion of the screen, Spectrum will
 verify that the equipment code is permitted. Spectrum will
 automatically assign the cost center of the equipment to the
 detail line, provided that the operator has permission for that
 cost center. Spectrum also ensures that the cost center assigned
 to the line based on the equipment is valid for the G/L account
 code specified on that line. Entry of that equipment code will
 not be permitted if the cost center in the equipment file is
 disallowed.

When the operator's scheme includes override settings for 'Equipment' entries
 in Cost Center Scheme Maintenance, this screen will
 validate the cost center assigned to equipment detail lines based on these
 overrides. The override cost center(s) supersede the cost center list
 defined for the scheme in general. Spectrum will compare the cost center
 assigned in the entry screen detail with 'Equipment' override cost centers
 in the operator's assigned scheme; if the cost center is not included, then
 the invoice entry line will not be allowed.
When the Allow G/L account overrides by cost center
 checkbox is selected on the Enterprise Installation
 screen, Spectrum will assign Accounts Receivable trade General Ledger
 account, by cost center based on a list of override G/L accounts in the
 respective Accounts Receivable
 Installation > Override window.
