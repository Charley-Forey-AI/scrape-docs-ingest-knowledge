---
title: "Add Multiple Invoices to a Payment Batch | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-multiple-invoices-to-a-payment-batch"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/add-multiple-invoices-to-a-payment-batch"
---

# Add Multiple Invoices to a Payment Batch

You can quickly add multiple invoices to a payment batch using the AP Initialize Payments form.

Payments in a batch may contain references to multiple bank accounts; specifically, invoices in the batch may all be assigned for payment from different CM accounts. (CM accounts are assigned to invoices when they are entered in the AP Transaction Entry or AP Recurring Invoices forms.) Although a payment batch can contain multiple transactions with different bank accounts, payments can only be processed for one CM account at a time.
If you want to pay only a small number of specific transactions, you can add them manually in the AP Payment Posting form rather than adding them with this form.
Note:

- It is highly recommended that you use separate payment batches to process invoices that have a different payment methods.

- The one exception to this is if you are using ePayments (U.S. only) because at the moment you generate the ePayments file, you can opt to change the different pay methods originally assigned on each invoice to N - ePayments. For details, see the field help for [Payment Methods](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form/field-definitions-ap-epayments-export-form#ID-000063380001--en) in the AP ePayments Export form.

1. Open the AP Payment Posting form.

1. Select File > Initialize Payments. The AP Initialize Payments form displays.

1. (Optional) In the CM Acct to be used if not assigned in the transaction field, enter a CM account. The system will assign this account number to all invoices that do not already have an account assigned.

1. Use the selection criteria options to restrict by CM account, vendor, job, payment control code, and/or payable type. See the F1 help on individual fields for more information.

1. In the Payment Methods section, you can use the invoices' payment method as criteria for adding the invoices to the batch:

- ePayments

- Check

- EFT

- Credit Service

1. In the Include transactions due as of field, enter a cutoff date. All transactions with a due date prior to or equal to this date will be added to the batch.

1. If you want to add transactions based on a discount date, select the If available, use Discount Date checkbox. If the invoice's discount date is equal to or prior to the cutoff date, the system will add the invoice to the batch.

1. If you only want to add discounted invoices to the batch, select the Include discounted transactions only checkbox.

1. In the Discounts section, set information in the fields as necessary. For more information, see [Adding Invoices with Discounts to a Payment Batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches).

1. If you want a separate check print for each subcontract, select the Create a separate payment per Subcontract checkbox.

1. If you want a separate check printed for each vendor/job combination, select the Create a separate payment per Job checkbox.Note: If there are multiple invoices with a Credit Service payment method for the same vendor, the system will group all of these credit service invoices into a single payment sequence, regardless of how you set the "separate payment" checkboxes mentioned above (steps 10 and 11).

1. If you do not want to add vendors with a credit balance to the batch, select the Exclude vendors with credit checkbox.

1. Select Update.

The system adds all invoices meeting the selection criteria to the batch. The system then clears all of the criteria on the form.Note: Keep the following in mind:

- If you have set up the system to prevent "out of compliance" invoices from being added to payment batches (AP Company Parameters form, Audit Options and Invoice Options tabs), the system will skip all invoices that are out of compliance.

- Any credit service invoices that have a different CM account than the one specified in the AP Company Parameters form (CM Acct field, Payment Services tab) will not be added to the payment batch.
