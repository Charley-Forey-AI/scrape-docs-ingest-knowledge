---
title: "Enter AP Invoice Lines: U.S. | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices/enter-ap-invoice-lines-u.s."
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices/enter-ap-invoice-lines-u.s."
---

# Enter AP Invoice Lines: U.S.

Once you've created the header portion of an invoice, enter the detail line items. This article applies if you're working in an AP Company whose HQ Country is United States.
 All invoices have a header portion and at least one line. This applies to invoices created using AP Transaction Entry, AP Recurring Invoices, or AP Unapproved Invoice Entry. Each line may be assigned to a different line type. For information about line types or any other fields on the invoice entry forms, see the F1 help.
To enter invoice detail lines:

1. In the Line field, enter a line number or N, New, or + and tab off to create a new line record.

1. In the Type field, [assign a line type to the line](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/about-accounts-payable-invoices/about-assigning-line-types-to-ap-invoice-lines).Note: If you have set the system to check compliance when entering purchase order or subcontract invoices (you selected the Don't add to Payments batch if "out of compliance" checkboxes in AP Company Parameters, Subcontracts or Purchase Orders sections), a warning displays when the purchase order or subcontract is not in compliance. To proceed, select OK and you can continue to enter the record.

1. Enter additional details specific to the line type as necessary. For example, if entering a job line, you will need to specify a JC Co, Job, Phase, and CT.

1.  For Job Lines only, if the costs associated with this line are related to a field ticket, enter the field ticket number in the Ticket field. Press F4 for a list of valid field tickets for the contract/job.For job PO lines, if the PO item is associated with a field ticket, the Ticket field defaults the ticket number from the PO item and is disabled.

1. In the Material field, enter a material for the line, if applicable.

1. In the Description field, enter a description for the detail line or accept the default.

1. If you are entering an Expense line (Type 3-Exp), enter a GL Co in the GL Co# field or accept the default. For all other line types, this field is disabled.

1. In the GL Account field, enter the GL account number or accept the default.Note: This field is enabled/disabled depending on how you set the Allow GL Account overrides checkbox in the company setup form related to the line type (that is, in the JC Company Parameters form if a Job line, IN Company Parameters form if an Inventory line, and so forth).

1. Enter information in the Amounts fields: UM, Units, UC, ECM, and Gross.Note: If you enter an invoice that includes a discount and you selected the Using tax discount checkbox in the AP Company Parameters form, the system automatically calculates the tax discount once the line's payable amount is entered. Tax discounts are calculated by subtracting the discount amount from the payable amount, then by applying taxes to the resulting amount (that is, the tax basis). The tax amount is then added to the payable amount and the discount subtracted from the total. Example: The following table shows what is calculated if you have an invoice payable amount of $1,000, a discount amount of $50.00, and a tax rate of 6.5%.
Payable AmountTax BasisTax AmountDiscountTotalNet Payable
$1,000.00$950.00$61.75$50.00$1,061.75$1,011.75

The system uses the following calculation: $1,000 - $50.00 = $950.00 x 6.5% = $61.75 + $1,000.00 = $1,061.75 - $50.00 = $1,011.75)

1. In the Misc Amt field, enter any freight or miscellaneous charges.

1. If you want to include the Misc Amt in the line's total, select the Included checkbox. However, the system does not include the miscellaneous amount when calculating taxes, discounts, or retainage for the line.

1. Enter any retainage or discount amounts in the Ret %, Ret Amt, Disc %, and/or Disc Amt fields.

1. If applicable, enter tax information in the Tax fields (Type, Code, Basis, and Amt).Note: For intercompany transactions, the tax type you select determines which company is responsible for paying tax, either the selling company or the purchasing company. The system determines the appropriate tax rate and tax code based on the responsible company’s associated tax group (HQ Tax Codes and Rates field, HQ Company Setup form, Add’l Info tab).For sales and value added tax, the system validates/defaults the tax code (in the Code field) based on the selling company’s tax group. For use tax, the system validates/defaults the tax code based on the purchasing company’s tax group.

1. If you are using payable categories (you selected the Using Payable Category checkbox in the AP Company Parameters form), enter a valid payable category in the Pay Category field or press F4 for a list of categories.The Pay Type field defaults from this line's pay category based on the line type (AP Pay Category form).

1. In the Pay Type field, enter the pay type for this item or accept the default. If you are using payable categories, this field defaults from the line's pay category base on line type. If not using payable categories, this field defaults the standard pay type defined in the AP Company Parameters form based on the line type.

1. (Optional) In the Supplier field, enter a supplier for this item or press F4 to select from a list.

1. Select Save. Note: When you save a PO or SL line, if the payment terms for the PO or SL differ from those assigned in the invoice header ( Discount Date and Due Date fields), a message displays and provides the option to update the header with the PO/SL payment terms. Select Yes to have the system automatically update the invoice header to reflect the payment terms for the PO/SL.Additionally, if you selected to have the system check compliance for purchase orders, subcontracts, and/or non-PO/SL invoices (options in the AP Company Parameters form), a warning displays when you enter non-compliant items. In all cases, the system still allows the entries.

1. Enter additional lines as necessary.Note: The sum total of all lines must match the total in the Invoice Total field (Header section) before you can post the batch.

Related information

- [AP Recurring Invoices Form](/en/vista/vista/accounting/accounts-payable/invoices/recurring-invoices/ap-recurring-invoice-forms/ap-recurring-invoices-form)

- [Enter Accounts Payable Invoices](/en/vista/vista/accounting/accounts-payable/invoices/ap-invoices/enter-accounts-payable-invoices)
