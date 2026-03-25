---
title: "About the AR Initialize Receipt Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-initialize-receipt-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-initialize-receipt-form"
---

# About the AR Initialize Receipt Form

You can use the AR Initialize Receipt form to to apply customer payments to invoices.
You can access this form by clicking the Save/Update button () in AR Cash Receipts.
When initializing payments, you must specify how to apply the payment and whether to include retainage, discounts, and/or finance charges. The following is a brief description of each option available in this form

- Oldest Invoices – Use this option to have the system apply payment to the oldest invoices. If the payment covers more than one invoice amount, the system will automatically apply the payment beginning with the oldest invoice and continuing until the payment has been fully distributed. If the payment was applied to any transaction that you did not wish to have paid, you can override the automatic payment by selecting the desired transaction (in AR Cash Receipts) and entering zero amounts where applicable. You will have to reapply the amount you rejected to another invoice for that customer. If there are no remaining invoices to pay, you may apply the payment on account until you can apply it to a specific invoice later.

- On Account – This payment option allows you to apply the payment to the customer's account balance rather than specific invoices. This type of payment is generally used for customers with a Balance Forward account, but you can use it for customers with Open Item accounts. For instance, you might use this type to apply a payment 'on account' temporarily when you do not know the specific application or the payment is a deposit against invoices to be processed in the future. The payment transaction could be changed later (assuming the month is still open) to apply to the specific invoices. If the month is closed, you may add a transaction in a current month with a total check amount of zero, posting offsetting amounts to the 'on account' payment and to other transactions to which you are applying the payment. You can apply discounts and taxes with this type of payment.

- By Invoice No - Start at First Open Invoice – This payment option works similar to the Oldest Invoices option, except that the system automatically applies the payment to the first open invoice and continues on to the next invoice until payment has been completely applied. For example, invoice #100 would be paid before invoice #200. Retainage and discounts are handled in the same manner.

- By Invoice No - Start at Invoice – Use this option to apply payment to invoices beginning with a specific invoice number (indicated to the right). The system will apply payment in the same manner as the previous option.

- By Customer Job (Material Sales invoices only) – With this option, payment is applied to a specific job for the customer (indicated to the right). Once you specify the job and click the OK button, the AR Initialize Receipt by Job form displays showing all of the invoices to which that customer job applies. You can then indicate which invoices you want paid and the payment is applied accordingly. Note: You can only use this feature if you have set the Invoice Level to 'One Invoice per Customer and Job' for the specified customer in AR Customers.

- Don't Initialize - Select this option if you want to manually select and apply payment to invoices.

- Include Retainage - This option allows you to apply payment to an invoice's unpaid retainage, as long as the amount of the payment is enough to cover both the amount due and unpaid retainage. If unchecked, payment is not applied to the retainage portion of invoices. However, you can manually override the payment application and apply any amount of the payment to retainage as necessary. (Note: If you are using the Distribute Tax to Retainage feature (AR Company Parameters), the unpaid retainage amount will include retainage tax.) Note: Use of this option will reset the Options menu in AR Cash Receipts to 'Show Open Invoices and Unpaid Retainage' so that the grid will include those Retainage Only invoices on which cash was automatically applied. Option will remain selected until changed by user.

- Apply Discounts (if applicable) - This option allows discounts to be applied to the payment transaction. System will automatically take discounts as long as the discount date is within the time frame specified by the payment terms for the selected customer and the amount of the payment covers the entire invoice balance. (Discounts may be taken manually. If unchecked, discounts will not be applied to invoices. However, you can manually apply a discount to an invoice/invoice line as necessary.

- Exclude Finance Charges – This option allows for excluding finance charges when applying payment. If checked, the payment applied to each invoice line will exclude the finance charge amount for that line. If unchecked, payment will be applied to finance charges as allowable (i.e. whatever portion of the payment is left after paying tax will be applied to the finance charges, then to the invoice total until fully applied). However, you can manually override the payment application and apply any amount of the payment to finance charges as necessary.

Once you have set the options as desired, click OK to begin initialization. The system will apply payments as specified and return you to the AR Cash Receipts form.
