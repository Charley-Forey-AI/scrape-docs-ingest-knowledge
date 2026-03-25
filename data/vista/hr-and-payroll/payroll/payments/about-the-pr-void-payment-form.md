---
title: "About the PR Void Payment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-void-payment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-void-payment-form"
---

# About the PR Void Payment Form

Use this form to void computer checks, EFTs, and previously processed manual checks.
You can access this form by clicking the Void Pmt button on PR Employee Pay Seq Control.
If you select the Void Check # radio button the system enables the Void Memo field. This records the check as void in Check History and Cash Management. If you already updated the check to Cash Management, the system deletes it in the next CM interface. When voiding, you cannot reuse the check number.
If voiding an EFT payment, a message displays. Click OK and the next CM interface subtracts the paid amount from the existing entry, as long as you previously updated the current EFT information to Cash Management.
For all voids, the CM Reference, CM Ref Seq #, EFT Seq# (if applicable), Paid Date, and Paid Month are cleared; the Total Hrs, Total Amount, and Total Deductions in the Payment Amounts box are set to zero; and the record now accepts new payment information.
If you select the Clear Check # radio button, the system allows you to reuse the check number.
Note: Whether you are clearing or voiding a payment, the system records a record in the system’s master audit table (HQMA). To review the audit table, run the HQ Audit Detail report.
