---
title: "Post and Process Payments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/post-and-process-payments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches/post-and-process-payments"
---

# Post and Process Payments

An overview of the payment posting process.

Before you can post/process payments, the invoices you wish to pay must be approved (if applicable), not on hold, not prepaid, and not in another batch.

Posting payments is a multiple-step process, all of which can be done using the AP Payment Posting form. The following instructions provide an overview of posting payments. Select the links to get more information on a particular step.

1. [Add invoices to a payment batch](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches).

1. [Print a report for review](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-preview-form).

1. [Edit invoices](/en/vista/vista/accounting/accounts-payable/payments/payment-posting/about-invoice-payment-batches) as needed.

1. [Print checks](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-check-print-form), [create AP EFT data files](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-eft-download-form) to send to your bank, and [generate credit service files](/en/vista/vista/accounting/accounts-payable/payments/credit-card-payments/generate-credit-service-files). ePayments (US only) can do all these, including the remittances, in a single process. See [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form#ID-000066a4--en__ID-000066a4).

1. If you created EFT data files:

- run the AP EFT Remittance report by selecting File > Tasks > EFT Remittance Report from this form or by running the report from the AP Reports folder in the Main Menu.Note: U.S only: the report is named AP EFT/ePayments Remittance Report. If you are not using ePayments, the report functions as the standard EFT Remittance Report.

- send a remittance report to the vendor using one of two methods:

- Email - use the [AP Email Pay Info](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-email-pay-info-form) form

- Mail - send a copy of the remittance report

Note: If you use ePayments (U.S. only), you do not need to send a remittance report to the vendor. The ePayments data file that you create and send to Corpay includes the invoice header and footer information for each payment. Corpay then supplies that data to the vendor when sending their payment..

1. If you generated credit service files, run the AP Credit Service Remittance report. You can run this report by selecting File > Tasks > Credit Service Remittance Report or by running the report from the AP Reports folder in the Main Menu.

1. If you have any prepaid transactions, process them using the AP Prepaid Process form. When prepaid transactions are updated, they are added to a payment batch that may already exist and include other types of payments. They will be processed as this batch is processed.

1. [Post the payment batch](/en/vista/vista/accounting/accounts-payable/ap-general-maintenance/ap-maintenance-forms/ap-batch-process-form) by selecting File >  Process Batch.

If the Attach Vendor Payment Report to Pay History checkbox in the AP Company Parameters form (Report Titles tab) is selected at the time you post the batch, the system attaches a PDF copy of the report specified in the EFT Remittance Title by Vendor field to the payment record. For more information, see [Payment Reporting Information](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information).For United States users: If you are using the Independent Contractor Reporting feature, the payment posting process includes a search for contractors (vendors) that qualify for contractor reporting. If the system identifies any contractors meeting reporting requirements when you process the batch, it displays a message asking if you want to run the AP Independent Contractor Report.
Tip: If you select No, you can run the report later from the AP Reports folder in the Main Menu.
 For more information, see [Reporting Independent Contractors](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/reporting-independent-contractors-united-states).
