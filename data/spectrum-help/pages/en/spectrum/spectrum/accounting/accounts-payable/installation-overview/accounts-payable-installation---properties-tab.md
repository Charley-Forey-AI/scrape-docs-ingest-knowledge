---
title: "Accounts Payable Installation - Properties tab | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---properties-tab"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---properties-tab"
---

# Accounts Payable Installation - Properties tab

Use this screen to define the default properties settings for the Accounts Payable module.
To apply or change these settings, go to System Administration > Installation > Accounts Payable.
Fields/ButtonsDescriptions
Post invoices to Job Cost?Select to cause invoice amounts to get applied to Job Cost.If not selected, invoices with job, phase, and cost type update to the subcontract detail system only, and not Job Cost or Time + Material files. Typically, this checkbox is selected at all times except during your initial conversion process.
Note: If you want to accrue the costs of materials that have been received on a purchase order, but not yet invoiced, this checkbox must be selected.

Stop entry if subcontract over revised amount?

- If this checkbox is selected, the software prevents entering the invoice until the subcontract is revised or a change order is recorded.

- If this checkbox is left clear, the software provides a warning that the revised contract amount has been exceeded, but entry of the invoice is permitted.

You may prefer to have the option to continue entry of the invoice even if, according to the subcontract records in the system, the revised contract amount is exceeded; the operator may know of change orders, for example, that have not yet been entered. Other users prefer to disallow any invoice entry that would exceed the revised contract; this is common in operations where subcontract management and Accounts Payable functions are handled by different staff members.
Default invoice detail dollar amount?

- Select this checkbox to default the invoice amount in the expense distribution during [Vendor Invoice Entry](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-invoice-entry). If this checkbox is selected, the software offers the balance of the invoice or credit memo when you enter the G/L distribution (in the lower half of the A/P Vendor Invoice Entry); if there are multiple lines of distribution, the software offers the remaining balance of the invoice on each successive line.

- If this checkbox is left clear, you must to enter the distribution amount on each line.

You may prefer to have the dollar amount default during entry of the invoice distribution because it decreases overall entry time and increases ease of operations. Other users prefer to enter the amount manually in order to actually slow down the operator; when the amount does not default, the operator must re-key the dollar amount. The system then validates the invoice amount equals the sum of the distribution.
Enter cleared amount in check reconciliation?Note: Applies only if you do not have the Cash Management module.

- If this checkbox is selected, the software prompts you for both check numbers and their amounts that cleared during the current statement cycle.

- If this checkbox is left clear, the software prompts you only for check numbers listed on the bank statement.

You can print a listing of checks that have not yet been presented to the bank. This list of "open items" is useful in reconciling the difference between the bank balance and your G/L account balance.
Recalculate terms discounts by line item?Select this checkbox to enter the terms discount percent by line item in Purchase Order Receiving, and in A/P Vendor Invoice Entry. When exiting the entry, Spectrum recalculates and displays the terms discount amount. If this checkbox is selected and a discount percent or amount is recorded in the heading portion of A/P Vendor Invoice Entry, the terms discount percent defaults to zero on the line items of the invoice.
If no entry is made in the heading, the detail lines default to the vendor terms discount percent. If you have entered detail level discount percentages and then later edit the discount amount in the header, the entered amount becomes the invoice discount and all detail line item discounts are reset to zero.
If this checkbox is left clear, the terms discount amount is determined from the terms discount percent in [Vendor Defaults](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-defaults). It cannot be entered for each line item.

Enter multi-company invoices?Select this checkbox to allow A/P invoices entered in this company to be distributed to other companies set up in Spectrum by specifying an alternate company code. When you do this, the software accepts G/L and Job Cost codes from the other company and updates accordingly. The invoice credits the Accounts Payable G/L account code in the current company and debits the multi-company G/L account specified on the Accounts Payable Installation > G/L Codes tab. The invoice distribution debits G/L (and job if applicable) in the other company, and credits the inter-company account code.
Stop entry if invoice date after maximum date?If this checkbox is left clear, invoice dates occurring after the maximum Accounts Payable processing date may be entered during invoice entry.
Select to prevent entry of an invoice whose date falls after the maximum Accounts Payable processing date. Enforced in these screens:

- Vendor Invoice Entry

- Unapproved Vendor Invoice Entry

- Subcontract Billing Entry

- Subcontract Below Line Billing

- Materials Management Freight Cost Reconciliation

- Material Purchase Reconciliation

- Purchase Order Receiving (both one-step and two-step)

Enable 'Phase over revised estimate' warning in invoice detail?Selected by default. When selected, a warning displays in the detail grid of these screens when a user enters a phase that is over budget.

- Vendor Invoice Entry

- Recurring Invoice Entry

- Purchase Order Entry

Include location in Comdata export file?Select this checkbox if you are a Comdata user and want to include the location field in the export file.
Use auto-sequenced vendor numbers?Select this checkbox if you want the system to automatically assign the next unused vendor code number when a new vendor is added to Spectrum and an alternate code has not already be specified.

Use automatic invoice processing?Note: Option appears only if your Spectrum
 subscription is through Trimble Construction One.
Select if
 you want to enable Automatic Invoicing for this AP company. For information
 about this feature, see [Automatic Invoicing (for Trimble Construction One Users)](/db/organizations/viewpoint/repositories/spectrum-production/content/documents/Global/Automatic_Invoicing/Topics/Shared/c_about_ai.dita).
Next vendor numberThe number which will be assigned to the next vendor you create, unless you change it.
Default subcontract retention percentEnter a standard subcontract retention percentage, if applicable to your company, to be applied by default to new subcontracts as they are added.
Cut-off day for 'First of next month' terms?Enter the day of the month (1-31) that is your "month-end" for purposes of prox terms A/P invoices. Prox terms invoices are ones carrying terms of "due 10th of following month" or "due 25th of following month".
For example:
If an invoice is due on the 10th of the month and is dated 01/12, it will be due 02/10; if the same invoice is dated 01/29, some offices may consider it due to be paid on 02/10 and others on 03/10. If the policy at your office is to hold invoices dated after the 25th of the month until the following 10th, enter 25 as the cut-off day. If all invoices dated within the current month are considered due on the following 10th, enter 31.
The system uses your entry in this field when the Payment due option group is set to First of next month in the [Vendor Defaults](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/about-vendors/vendor-main-properties/vendor-defaults), to determine the due date during A/P Vendor Invoice Entry. The operator may override the computed date.

Contract labor cost typesEnter up to five labor cost types to be used in tracking contract labor hours recorded through Accounts Payable.
Default T + M labor bill codeEnter the default Time + Materials labor billing code.

- This field displays only if one or more labor cost types are entered in the Contract labor cost types field.

- If you have a Time + Materials phase or job, the labor bill code entered here appears in the Accounts Payable Invoice / Credit Memo Entry > Contract Hours field.

Default invoice cost centerIf using cost centers, enter the standard cost center that should be assigned to the invoice header during Vendor Invoice Entry.
Sub billing entry defaultDetermines the default quantity entry method for the Subcontract Billing Entry. Choose a default method:

- This period – the software stops at the Current period quantity field for entry.

- Job-to-date – software stops at the Job-to-date field for entry.

Default invoice due date calculations
Payment due date based on

- Invoice date - due dates with this vendor are figured from the invoice date.

- First of next month - due dates are figured from the first of the following month.

Payment due - number of days

- If you selected Invoice date above, enter the number of days allowed. For example, enter "30" for net thirty days terms.

- If you selected First of next month above, enter the date that payments are due. For example, enter "10" if payment is due on the tenth of the month.

Discount due date based on

- Invoice date - discount terms with this vendor are figured from the invoice date.

- First of next month - discount terms are figured from the first of the following month.

Discount due - number of days

- If you selected Invoice date above, enter the number of days allowed for the discount.

- If you selected First of next month above, enter the number of days allowed for a discount.

Discount %Enter the discount percentage allowed. For example, a 2 percent discount should be entered as 2, not as 0.02.
