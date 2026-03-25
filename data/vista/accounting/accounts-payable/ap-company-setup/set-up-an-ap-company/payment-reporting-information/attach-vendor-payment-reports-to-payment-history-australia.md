---
title: "Attach Vendor Payment Reports to Payment History: Australia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information/attach-vendor-payment-reports-to-payment-history-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information/attach-vendor-payment-reports-to-payment-history-australia"
---

# Attach Vendor Payment Reports to Payment History: Australia

You can have the system automatically attach an electronic copy of payment information to payment history records when generating vendor payments in Accounts Payable.
The type of payment information attached to the payment history differs depending on the type of payment. For cheque payments, the system attaches a non-negotiable copy of the cheque to the payment history record. For EFT payments, the system attaches a copy of an EFT remittance report. For credit service payments, the system attaches a copy of the credit service remittance report. Attachments are in PDF format.
The system attaches reports to the payment record in AP Payment Posting once you print cheques or download EFTs and/or credit service files. When you post the AP Payment Posting batch, the system moves the attachment to the payment history record in AP Payment History.
Note: By attaching payment reports to payment history, you also enable the ability to send these payment reports to a vendor electronically once you make a payment. For more information, see [Sending Vendor Payment Information by Email](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-email-pay-info-form).

1. From the main menu, select Accounts Payable > Programs > AP Company Parameters.

1. In AP Company Parameters, click on the Payment Reports tab.

1. Select the Attach Creditor Payment Report to Pay History checkbox.The system enables the remaining fields on
 form.

1. In the Creditor Pay Attachment Type ID field, enter the attachment type ID or press F4 to select from a list of attachment types.Note: By adding an attachment type, you are able to apply
 security to attachments. For more information on
 attachment types, see [DM Attachment Types Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form). If you do not apply an attachment type and set
 security, all users with access to vendor pay
 history will be able to view these
 attachments.

1. In the Report title for Cheque Print by Creditor field, enter the report to use for creating the cheque print report that is attached to the payment history record or accept the default AP Cheque Print by Vendor - A/NZ report. Press F4 to select from a list of valid reports.If this field is blank, the system uses the AP Cheque Print by Vendor - A/NZ report.

1. In the Report title for EFT Remittance by Creditor field, enter the report to use for creating the remittance report that is attached to the payment history record or accept the default AP EFT Remittance by Vendor - A/NZ report. Press F4 to select from a list of valid reports.If this field is blank, the system uses the AP EFT Remittance by Vendor - A/NZ report.

1. In the Report title for Credit Service Remittance by Creditor field, enter the report to use for creating the remittance report that is attached to the payment history record. Press F4 to select from a list of valid reports.If this field is blank, the system uses the AP Credit Service Remittance by Vendor report.

 The uses the above settings when attaching reports to payment history.
