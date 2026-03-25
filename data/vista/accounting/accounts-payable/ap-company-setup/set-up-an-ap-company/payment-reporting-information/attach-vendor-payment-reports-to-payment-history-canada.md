---
title: "Attach Vendor Payment Reports to Payment History: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information/attach-vendor-payment-reports-to-payment-history-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information/attach-vendor-payment-reports-to-payment-history-canada"
---

# Attach Vendor Payment Reports to Payment History: Canada

You can have the system automatically attach an electronic copy of payment information to payment history records when generating vendor payments in Accounts Payable.
The type of payment information attached to the payment history differs depending on the type of payment. For cheque payments, the system attaches a non-negotiable copy of the cheque to the payment history record. For EFT payments, the system attaches a copy of an EFT remittance report. For payment service payments, the system attaches a copy of a payment service remittance report. Attachments are in PDF format.
The system attaches reports to the payment record in the AP Payment Posting form once you print cheques or download EFTs and/or payment service files. When you post the AP Payment Posting batch, the system moves the attachment to the payment history record in the AP Payment History form.

1. From the main menu, select Accounts Payable > Programs > AP Company Parameters.

1. In the AP Company Parameters form, click on the Payment Reports tab.

1. Select the Attach Vendor Payment Report to Pay History checkbox.The system enables the remaining fields on
 form.

1. In the Vendor Pay Attachment Type ID field, enter the attachment ID or press
 F4 to select from a list of attachment types.Note: By adding an attachment type, you are able to
 apply security to attachments. For more information on attachment types, see [DM Attachment Types Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form). If you do not apply an attachment type and set security, all users with access
 to vendor pay history will be able to view these attachments.

1. In the Report title for Cheque Print by Vendor field, enter the report to
 use for creating the cheque print report that is attached to the payment history
 record or accept the default AP Cheque by Vendor - Canada report. Press F4 to
 select from a list of valid reports.If this field is blank, the system uses the
 AP Cheque by Vendor - Canada report.

1. In the Report title for EFT Remittance by Vendor field, enter the report to
 use for creating the remittance report that is attached to the payment history record
 or accept the default AP EFT Remittance Vendor - Canada report. Press F4 to
 select from a list of valid reports.If this field is blank, the system uses the
 AP EFT Remittance Vendor - Canada report.

1. In the Report title for Payment Service Remittance by Vendor field, enter
 the report to use for creating the remittance report that is attached to the payment
 history record. Press F4 to select from a list of valid
 reports.If this field is blank, the system uses the
 AP Credit Service Remittance by Vendor report.

The system uses the above settings when attaching reports to payment history.
