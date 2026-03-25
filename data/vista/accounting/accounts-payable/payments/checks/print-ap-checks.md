---
title: "Print AP Checks | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/checks/print-ap-checks"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/checks/print-ap-checks"
---

# Print AP Checks

Instructions for printing AP checks.
Load check stock in the appropriate printer.
When printing AP checks, you can select a specific group of checks to print from the current AP Payment Posting batch. You can print checks by vendor sort name, by sequence, or a combination of both. Regardless of the filter setting you select, the system prints checks in alphabetical order by vendor sort name, and then by sequence number order. This section explains how the system prints, depending on the filter settings you select.The following instructions detail how to print AP checks. You can also use the following instructions if you have voided and cleared checks and need to print them again.

1. In the CM Account field, enter the payment account.

1. In the Paid Date field, enter the payment date.

1. In the Beginning Check # and Ending Check # fields, enter the range of check numbers to print.Note: The Beginning Check # field defaults to the next available check number, while the Ending Check #  field defaults to the highest check number possible (9,999,999,999). When you click Print Checks, the Ending Check # field displays the last check number in the range.If you specify a previously used check number or check number range, the system displays a warning. Change the specified check number(s) or clear the checks from the payment batch and start over.

1. Click Print Checks.The Print window displays.

1. Configure printer settings as necessary and click OK.The checks print to the specified printer and the system returns to the AP Check Print form.Note: If the system requires the printing of one or more check overflow stubs, a warning displays. Close the warning and click Print Overflows. You must do this before posting the batch. For more information, see Printing Overflow Vouchers.

1. If applicable, click Print Copy to print a non-negotiable set of check copies.

1. Click Close.

1. (Optional) Use [AP Email Pay Info](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-email-pay-info-form) to send a non-negotiable copy (PDF format) to the vendor by email.Note: If you selected the Attach Vendor Payment Report to Pay History checkbox in the AP Company Parameters form, the system attaches a PDF copy of the report specified in the Check Print Report Title by Vendor field (also in the AP Company Parameters form) to the AP Payment Posting record. For more information, see [Setting Payment Information](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information).
