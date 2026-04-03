---
title: "Vendor Defaults - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-defaults/vendor-defaults---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-defaults/vendor-defaults---field-descriptions"
---

# Vendor Defaults - Field Descriptions

A table reference for completing the fields on this screen.
Fields/ButtonsDescriptions
Vendor codeIf this screen is accessed from the info bar, the selected vendor code defaults in this field. [Info Bar FAQs](/en/spectrum/spectrum/getting-started/spectrum-interface-faqs/info-bar/info-bar-faqs)
Invoice approvalFields in this section are enabled only if the Use Invoice Approval Processing? checkbox is selected in Accounts Payable Installation.

Default routing codeServes as the default when routing invoices for approval.
Invoice dollar limit
Routing code over limit
The dollar limit which should trigger the use of the over-limit routing code, and the routing code to use when an invoice amount exceeds the dollar limit. If there is no established invoice dollar limit, leave this field blank.Note: You can opt to leave both fields blank and instead manage the approval routing by entering Approval Limits on the Routing Code. For additional information, see [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits).

Invoice defaults
Sales/use tax codeEnter the default tax code (up to 15 alpha-numeric characters) for this vendor. This code may be either a sales or a use tax code and will be used to set defaults where no job is entered in Purchase Order Entry or A/P Vendor Invoice Entry.In Invoice Entry and Unapproved Invoice Entry, when an invoice is added, Spectrum distributes the amount to the code entered here. However, if any additional codes are added using the G/L Distribution button, Spectrum adds tax to the invoice according to the tax codes and percentages defined in the Multiple G/L Distribution window.

Related-Party G/L AccountsIf the selected vendor is a related party, select this button to open the [Related-Party G/L Accounts](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-defaults/related-party-gl-accounts) window to manage override G/L accounts for related-party vendors.Note: This button is disabled if the Allow G/L account overrides by cost center checkbox is selected in the Enterprise Installation screen (Company tab).

G/L distributionEnter the General Ledger account code to which invoices for this vendor are usually charged, even if the General Ledger module is not part of the computer system. If G/L is not present, A/P amounts may be manually posted from the A/P Transaction Register produced before the invoice update. This is the debit G/L account to which invoices are posted, for example, Construction In Progress. G/L codes with a status of Not used may not be selected.When setting up a credit card issuer vendor, it is recommended that the same G/L code assigned to the Cash Management > Account code will be entered as the G/L distribution account code on the Financials tab or this screen. This will facilitate data entry of invoices to pay the credit card balance.
Cost Center Information
Spectrum allows entry of a G/L account code only if the operator entering the G/L account has permission to assign that code. The system compares the G/L account's list of shared cost centers to the list of cost centers in the operator's assigned cost center scheme and if there are no common cost centers, then this G/L account cannot be assigned.

Payment hold?To prevent payment of this vendor's invoices, select this checkbox. When invoices are entered into the software, this information will default to the invoice entry screen but may be overridden when necessary. Selecting or deselecting this checkbox will not affect any open invoices already entered. This field serves as a default when new invoices are entered.It is also possible to access the hold status of individual invoices even after they have been updated by using A/P Invoice Due Date Change.

G/L % AllocationThis button opens the Multiple G/L Distribution window. Use this window to set up non-direct cost G/L codes with a percent distribution. Then, in A/P Vendor Invoice Entry and Recurring Invoice Maintenance, the invoice amount is automatically distributed to these G/L codes based on the percent distribution set up for the vendor. This may be especially useful for departmentalized operations wishing to allocate certain general and administrative costs across departments (that is, telephone, office supplies or legal costs).
Payment due calculation
Based onSelect the payment due terms for this vendor.
Number of daysIf the payment due terms are figured from the invoice date, enter the number of days allowed (for example, "30" for net thirty days terms). If the payment due terms are figured from the first of the month, enter the date that payments are due (for example, "10" indicates that payment is due on the tenth).
Pay job invoices based on customer payment?This setting serves as the default for new invoices in Vendor Invoice Entry (in conjunction with the 'pay-when-paid' flag for subcontract invoices with override terms setting in the [Subcontract Defaults](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/subcontracts/subcontract-defaults)).Specifically, this setting applies to job invoices and credit memos when the job is flagged to Pay-when-paid.

Discount due calculation
Based onSelect the discount terms for this vendor.
Number of daysIf the discount terms are figured from the invoice date, enter the number of days allowed. If the discount terms are figured from the first of the month, enter the number of days allowed for a discount.
Discount %Enter the discount actual percentage; it is not necessary to convert the percentage to a decimal. For example, for a five percent discount, enter 5. For a ten and sixty-four one hundredths percent discount, enter 10.64.
Insurance
Certificate and Expiration dateUse the drop-down menu to select the insurance certificate option and enter the expiration date of the vendor's insurance certificate, if one exists.To use the expiration or lack of insurance as a flag and receive a warning during data entry, set up document tracking items in [Document Tracking Item Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/maintenance-overview/document-tracking-item-maintenance). This setting defaults when new subcontracts for this vendor are added to the software.

Purchase order default
Receiving methodSelect the default receiving method when a new purchase order for the vendor is added: Company default, One step (invoice), or Two-step (packing list + invoice).Note: This section is hidden if the Purchase Order module doesn't apply to the current company.
