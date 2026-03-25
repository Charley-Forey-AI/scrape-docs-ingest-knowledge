---
title: "About Printing Overflow Vouchers | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/payments/checks/about-printing-overflow-vouchers"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/payments/checks/about-printing-overflow-vouchers"
---

# About Printing Overflow Vouchers

You must print overflow vouchers if remittance information exceeds the space available on the check stub.
When you generate computer checks with the AP Check Print form, the remittance information may exceed the available space on the check stub. If this occurs, the system displays a warning. Close the warning dialog box and the system enables the Print Overflows button. You must print the check overflow before posting the batch.
The space available on the check stub is determined by the Max# Lines Per Check Stub field in the AP Company Parameters form. If you are using Vista™ checks, the default value for this field is 29 and you should not change it. However, if you are not using Vista™ software checks, you may need to change this default to accommodate check space.
 The system prints overflow vouchers based on the Overflow Print Report Title field in the AP Company Parameters form. The standard report is the AP Check Overflow report; however, you can create a custom report in Crystal Reports and specify it in this field. If you do not specify a report in this field, the system automatically uses the AP Check Overflow report.
