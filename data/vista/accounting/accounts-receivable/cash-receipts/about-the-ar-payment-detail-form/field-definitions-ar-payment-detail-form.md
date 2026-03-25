---
title: "Field Definitions: AR Payment Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-payment-detail-form/field-definitions-ar-payment-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-payment-detail-form/field-definitions-ar-payment-detail-form"
---

# Field Definitions: AR Payment Detail Form

The following is a list of field descriptions for the AR Payment Detail form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Remove Input Restrictions

 Check this box to override input restrictions in the line detail grid. If checked, you can apply amounts that exceed the unpaid tax, retainage, and finance charge amounts or 'Apply' amount. However, it is highly recommended that you DO NOT use this option unless you have a complete understanding of how the detail and distribution tables track data.

## Apply Amount

This field automatically defaults an amount based on the total amount applied to this invoice on the AR Cash Receipts form, and the amount applied to other items on this invoice.
Accept the default amount, or enter the appropriate amount to apply to this invoice item.
If a discount is to be taken, do not subtract that amount from the amount entered here. The system automatically adjusts the total payment (displays in the Total field)
Tip: After entering the payment amount, and while the cursor is still in this field, use the 'shortcut' options for applying payment discounts (Ctrl + D) and tax discounts (Ctrl + E).

##  Disc Taken

 This field is available when the one of the “Allow Discounts” options are selected in AR Company Parameters.
 If you initialized payments and selected the Apply Discounts checkbox on AR Initialize Receipt, this field defaults the 'offered' discount for the invoice line. The system allows overrides as long as the amount does not exceed the discount available.
 You can override this restriction by checking the "Remove Input Restrictions" option above the grid.
Important: It is not recommended that you override input restrictions unless you have a complete understanding of how data is tracked within the detail and distribution tables.
Tip: To set the Disc Taken automatically for this line, place focus in the Apply Amount column and press Ctrl + W.

##  Apply Tax

 This field is available when the one of the “Allow Discounts” options are selected in AR Company Parameters.
 Initially defaults the amount of payment that was applied to this line's tax amount. The system allows overrides; however, you cannot apply an amount that exceeds the unpaid tax or 'Apply' amount. You can override this restriction by checking the "Remove Input Restrictions" option above the grid.
Important: It is not recommended that you override input restrictions unless you have a complete understanding of how data is tracked within the detail and distribution tables.
Tip: To set the Apply Tax automatically for this line, place focus in the Apply Amount column and press Ctrl + Q.

##  Apply Retg

 This field defaults the amount of payment that was applied to this line's retainage amount. The system allows overrides; however, you cannot apply an amount that exceeds the unpaid retainage or 'Apply' amount. You can override this restriction by checking the "Remove Input Restrictions" option above the grid.
Important: It is not recommended that you override input restrictions unless you have a complete understanding of how data is tracked within the detail and distribution tables.
 If you elected to automatically apply the payment to retainage (by selecting the Include Retainage checkbox on AR Initialize Receipt), the system will apply the payment to both the Amount Due and Unpaid Retg for each item until payment is satisfied. If the amount of the check is not sufficient to cover both the Amount Due and the Unpaid Retg for an item, the payment will be applied to the Amount Due only. Adjust applied amounts manually for any item.
Note: If you do not check the Include Retainage box in the Apply Payment window, you can still apply payment to retainage by entering the amount manually.
Tip: To set the Apply Retg automatically for this line, place focus in the Apply Amount column and press Ctrl + G. (Note: Sets both the Apply Retg and Apply RetgTax amounts as applicable.)

##  Apply RetgTax

 This field only displays if you have checked the Include Apply RetgTax in Grid option (Options menu).
 If you are using the ‘Distribute Tax to Retainage’ feature (AR Company Parameters), defaults a retainage tax amount based on the amount of payment applied to the line’s retainage amount. For example, if the UnPaid Retainage is $115.00 ($100 retainage, $15 retainage tax), and you apply 50% of that ($57.75), this field would default as 7.75 (50% of the retainage tax). You may override as necessary; however, you cannot apply an amount that exceeds the unpaid retainage tax or the ‘Apply Amount’.
Important: Although you can override the input restriction by checking the ‘Remove Input Restrictions’ option above the grid, it is not recommended unless you have a complete understanding of how data is tracked within the detail and distribution tables.
 If you elected to automatically apply the payment to retainage (Include Retainage option, AR Initialize Receipt), the system will apply the payment to both the Amount Due and UnPaid Retainage/UnPaid Retg Tax for each item until payment is satisfied. If the amount of the check is not sufficient to cover these amounts, the payment will be applied to the Amount Due only. Adjust applied amounts manually for any item.
Tip: To set the Apply RetgTax automatically for this line, place focus in the Apply Amount column and press Ctrl + G. (Note: Sets both the Apply Retg and Apply RetgTax amounts as applicable.)

## Apply FC

Initially defaults the amount of payment that was applied to this line's finance charges. The system allows overrides; however, you cannot apply an amount that exceeds the unpaid finance charge or 'Apply' amount. You can override this restriction by checking the "Remove Input Restrictions" option above the grid.
Important: It is not recommended that you override input restrictions unless you have a complete understanding of how data is tracked within the detail and distribution tables.
Note: Although finance charges may be assessed and paid on
 contract invoices, the system does not update the finance charge portion of the invoice to
 JC; only the invoice amount updates to JC.
Tip: To set the Apply FC automatically for this line, place focus in the Apply Amount column and press Ctrl + F.

##  Apply TaxDisc

 This field is available when the Allow TaxDisc on Invoices & Receipts checkbox is selected in AR Company Parameters.
 If you initialized payments and selected the 'Apply Discounts (if applicable)' option, this field will default the offered tax discount (i.e., 'TaxDisc Avail') for the invoice line, if applicable. The system allows overrides as long as the amount does not exceed the tax discount available. You can override this restriction by checking the "Remove Input Restrictions" option above the grid.
Important: It is not recommended that you override input restrictions unless you have a complete understanding of how data is tracked within the detail and distribution tables.
Tip: To set the Apply TaxDisc automatically for this line, place focus in the Apply Amount column and press Ctrl + E.
