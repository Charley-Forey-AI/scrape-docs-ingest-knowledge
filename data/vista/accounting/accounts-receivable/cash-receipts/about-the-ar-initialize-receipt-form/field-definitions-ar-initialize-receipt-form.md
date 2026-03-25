---
title: "Field Definitions: AR Initialize Receipt Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-initialize-receipt-form/field-definitions-ar-initialize-receipt-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-initialize-receipt-form/field-definitions-ar-initialize-receipt-form"
---

# Field Definitions: AR Initialize Receipt Form

The following is a list of field descriptions for the AR Initialize Receipt form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Apply Balance of Receipt To

- Oldest Invoices – Select this option to have the system automatically apply the payment to the oldest invoice. If the payment is greater than the invoice amount, the system applies the balance to each subsequent invoice until the applied amount matches the payment amount. If the system applied payment to any transaction that you did not want paid, override the automatic payment by selecting the desired transaction and entering zero amounts where applicable. Reapply the rejected amount to another invoice for that customer. If there are no remaining invoices, you may apply the payment on account until applying it to a specific invoice later.

- On Account – Select this option to have system apply payment to the account balance rather than specific invoices. Use this type of payment for customers with a Balance Forward account. However, you might also use this when the receiving a payment for an unknown application, or if the payment is a deposit against future invoices. In this case, change the payment transaction at a later date (assuming the month is still open. If the month is closed, add the transaction in a current month with a total check amount of zero, posting offsetting amounts to the on account payment. Discounts and taxes can also be taken/paid with this type of payment.

- By Invoice No - Start at First Open Invoice – Select this option to have the system apply payment beginning with the first open invoice and continuing until payment has been completely applied. This method applies payment by invoice number.

- By Invoice No - Start at Invoice – Select this option to have the system apply payment starting with a specified invoice (to the right) and continuing until payment is fully applied.

- By Customer Job (Material Sales invoices only) - Select this option to have the system apply payment to a selected customer job (specified to the right). When you click the Initialize button, the AR Initialize Receipts by Job form displays, showing all of the invoices that apply to the customer job. You can then indicate which invoices you want paid and the system applies payment accordingly.

Note: This feature is only available if you have set the
 Invoice Level for the specified customer to “One Invoice per Customer and Job” in AR
 Customers.

- Don’t Initialize - Select this option
 if you want to manually select and apply payment to invoices.

##  Start at Invoice

 Specify the invoice to start applying this payment to. The system applies payment to this invoice first and then to subsequent invoices (i.e. in order by invoice number) until fully applied.

##  Customer Job

 Used only for invoices interfaced from MS.
 Specify the customer job (defined on the MS ticket) to which this payment should be applied. When you click the Initialize button, the AR Initialize Receipt by Job form displays, showing a list of the invoices to which the customer job applies and allowing you to select which invoices to pay.

## Include Retainage

Check this box to have part or all of this payment applied to the invoice’s unpaid retainage. When checked, the system applies payment to the unpaid retainage, as long as the amount of the payment is enough to cover both the amount due and the unpaid retainage. (Note: If you are using the Distribute Tax to Retainage feature (AR Company Parameters), unpaid retainage includes retainage tax; therefore payment will be applied to the retainage tax portion as well.)
Note: Use of this option will reset the Options menu in AR Cash Receipts to ‘Show Open Invoices and Unpaid Retainage’ so that the grid will include those Retainage Only invoices on which cash was automatically applied. The option remains selected until changed by user.
Leave this box unchecked if you do not want the payment to be applied to the invoice’s unpaid retainage. You can still apply retainage manually.

##  Apply Discounts (if applicable)

 Check this box to apply discounts to this payment transaction. The system automatically takes the discount as long as the discount date is within the time frame specified by the payment terms for the selected customer.
 Leave this box unchecked if discounts will not be applied to this payment transaction. Discounts may still be applied manually.

##  Exclude Finance Charges

 Check this box to exclude payment from being applied to finance charges. When payments are applied to invoices, the amount applied to each invoice line will exclude the finance charge amount for that line. If a line's finance charge was previously paid, checking this box will cause a reverse entry for the amount of the finance charge on that line.
 Leave this box unchecked to apply payment to finance charges where applicable.
