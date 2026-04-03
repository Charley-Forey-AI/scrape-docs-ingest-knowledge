---
title: "Subcontract Defaults - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-defaults/subcontract-defaults---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-defaults/subcontract-defaults---field-descriptions"
---

# Subcontract Defaults - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields / ButtonsDescriptions
Header fields
VendorEnter a vendor code for this subcontract. The vendor code must already be set up in the vendor file. The vendor's full name will display.
Subcontract #It is recommended that the job number be used as the subcontract number for most vendors.
Invoice ApprovalFields in this section are enabled only if the Use Invoice
 Approval Processing? checkbox is selected in
 Accounts Payable Installation.

Default routing codeServes as the default when routing invoices for
 approval.
Invoice dollar limit
Routing code over limit
The dollar limit which should trigger the use of the over-limit routing code, and the routing code to use when an invoice amount exceeds the dollar limit. If there is no established invoice dollar limit, leave this field blank.Note: You can opt to leave both fields blank and instead manage the approval routing by entering Approval Limits on the Routing Code. For additional information, see [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits).

Invoice defaults
G/L accountEnter the code of the General Ledger account that should be charged for this
 subcontractor. If the Validate
 job division with G/L department and Auto default G/L
 department checkboxes are selected on the Job Cost Installation > Properties tab, then the G/L code will automatically be converted based
 on the job division. A search window is available for viewing valid General
 Ledger account codesNote: This must be a direct cost account. In addition, G/L codes with a status of
 Not used may not be selected.

Retention %The Default subcontract retention % defined in Accounts Payable Installation > Properties will default in this field once a new subcontract has been
 created.
Next paymentEnter the number of the next payment to this subcontractor. After initial
 conversion, as subcontracts are set up this should be set to
 1.
Cost centerIf cost centers are enabled for the current company and you have the
 appropriate security for the cost center code, enter it in this field. If
 this field is left blank, Spectrum will use the default cost center assigned
 on the Accounts Payable Installation screen.
EntityIf a cost center is entered above, the entity assigned to that cost center displays in this field. If entities are not being used, this field is hidden.
Payment due calculation
Override standard vendor payment terms?If this checkbox is selected, the same payment terms defined for the vendor associated with this subcontract will default and the Based on and Number of days fields will be enabled.
Based onSelect Invoice date if payment due terms with this vendor are figured from the invoice date. If payment due terms are figured from the first of the following month, select First of next month.
Number of daysIf the payment due terms are figured from the invoice date, enter the number of days allowed (for example, "30" for net thirty days terms). If the payment due terms are figured from the first of the month, enter the date that payments are due (for example, "10" indicates that payment is due on the tenth).
Pay invoices based on customer payment?When the Override standard vendor payment terms checkbox is selected, the 'pay-when-paid' flag will be available and new invoices for the current subcontract will default from this setting when the subcontract is for a job authorized for pay-when-paid processing in Job Setup.When the Override standard vendor payment terms checkbox is not selected, this pay-when-paid flag will display the current vendor setting, but will be disabled.

Discount due calculation
Override standard vendor discount terms?If this checkbox is clear, the remaining fields in this section are disabled and they will display the vendor's standard discount terms.
Based onChoose how the discount terms with this vendor are computed from the Invoice date or from the First of next month.
Number of daysEnter the number of days allowed for a discount.
Discount %Enter the discount actual percentage; it is not necessary to convert the
 percentage to a decimal. For example, for a five percent
 discount, enter 5. For a ten and sixty-four one
 hundredths percent discount, enter
 10.64.
