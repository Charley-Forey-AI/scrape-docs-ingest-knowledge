---
title: "How Finance Charge Types Are Used | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/invoices/how-finance-charge-types-are-used"
---

# How Finance Charge Types Are Used

When using the AR Finance Charge form to automatically calculate finance/service charges, the system bases calculations on either the customer's account balance or individual invoices. Assign a Finance Charge Type to each customer to determine the calculation level.
The following is a description of each type:
Account Type:The system calculates the finance/service charges based on the customer’s account balance. The system accumulates all transactions due on or before due date cutoff (less retainage), subtracts all cash received and credit memos posted before the paid cutoff date, and calculates the finance/service charge on any remaining overdue balance.
 Use this type for customers with either Balance Forward or Open Item statement accounts.

Invoices:The system calculates finance/service charges on individual invoices. The system calculates charges based on the unpaid portion of each invoice (less retainage), with a separate line for each line of the invoice. The system creates a new invoice, indicating the original invoice, JC company, and applicable contract. For each line on the original invoice, a separate line exists on the finance charge invoice, indicating the applicable contract item. The system calculates finance charge invoice due dates using the Payment Terms for the contract or customer.
 If you set the Interface Level in AR Company Parameters (Finance Charges tab) to Calculate Finance Charge, the generated finance charges interface to Job Cost as individual revenue records.
Only use this type for customers with Open Item statement accounts.

Rec Type:When you select this type, the system assesses finance/service charges against all outstanding invoice transactions and groups them according to invoice receivable type. The system generates a separate invoice for each receivable type.
 When using this option, the system calculates finance charges against invoices using the dates in the Due Date Cutoff and Paid Date Cutoff fields in the AR Calculate Finance Charge form.
 When restricting by Rec Type on the AR Calculate Finance Charge form, the system only assesses finance charges for unpaid invoices that are due on or before the due date cut off, and payment has not occurred on or before the paid cut off date.
Only use this type for Open Item statement accounts.

No Finance Charges:The system skips over any customer assigned this finance/service charge type. No charges are assessed.

Note: Use the Statements section in AR Customers to specify an account as requiring either Balance Forward or Open Item statements.
[ About the AR Customers Form](/en/vista/vista/accounting/accounts-receivable/customers/about-the-ar-customers-form)
