---
title: "AP Check Print Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form"
---

# AP Check Print Form

Use this form to print checks in the current payment-posting batch. Access this form from the AP Payment Posting form by selecting File > Print Checks.
With this form, you can process only transactions with a pay method of C-Check and a check type of C-Computer. If you are not sure of what checks will print during a check run, review the AP Payment Preview with Compliance report. The report displays checks in alphabetical order by vendor. For more information on running this report, see [AP Payment Preview](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-preview-form).
When you print checks, the system runs a Crystal report to perform the check print. The system uses the report that you specified in the Check Print Report Title field in the AP Company Parameters form. Prior to printing checks, make sure that you have specified the proper report. For more information, see [Setting Payment Information](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information).
The system does not update check information to the CM module or save it in the database (except for voids) until you post the payment batch. This allows you to reuse check numbers, which can be useful in the case of a printer malfunction. When reprinting checks, the system overwrites the old check information with the new information. Once you post the payment batch, the AP Check Print form does not allow you to reuse checks that exist in CM or in the database.
For more information, click the following links.
[Print AP Checks](/en/vista/vista/accounting/accounts-payable/payments/checks/print-ap-checks#task-6829--en__task-6829)
[Clear & Void AP Checks for Non-Posted Transactions](/en/vista/vista/accounting/accounts-payable/payments/voiding-payments/clear--void-ap-checks-for-non-posted-transactions)
[How the System Prints Checks](/en/vista/vista/accounting/accounts-payable/payments/checks/how-the-system-prints-checks#concept-8120--en__concept-8120)
[About Printing Overflow Vouchers](/en/vista/vista/accounting/accounts-payable/payments/checks/about-printing-overflow-vouchers#concept-6852--en__concept-6852)
