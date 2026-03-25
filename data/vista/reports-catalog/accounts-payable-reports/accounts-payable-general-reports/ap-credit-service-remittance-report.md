---
title: "AP Credit Service Remittance Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/accounts-payable-reports/accounts-payable-general-reports/ap-credit-service-remittance-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/accounts-payable-reports/accounts-payable-general-reports/ap-credit-service-remittance-report"
---

# AP Credit Service Remittance Report

Use the AP Credit Service Remittance report to print a remittance advice for a vendor. You can access this report by selecting Accounts Payable >  Reports  > AP Credit Service Remittance.
This report is designed to be a remittance advice for vendors and is intended for use with open payment batches. The report prints a new page per payment sequence, and includes the transaction number, AP reference number, invoice date, description, and gross, discount, deduction, and net amounts.
If you create a custom report and reference it in the Report Title for Credit Service
 Remittance field in AP Company Parameters (Payment Reports tab), the
 system will use it instead of this standard report when you select File >  Credit Service Remittance Report from the AP Payment Posting form.
Report ParametersDescription
Company
Accept the default, or press F4 to select a company.

Month
Enter or select the month.

BatchId
Press F4 to select the batch ID number.

Print All Remittance Reports?
Select the checkbox to print each credit service payment sequence in the batch for all vendors.
If you do not select this checkbox, the report will print remittances for every vendor if you did not check the Attach Vendor Payment Report to Pay History box in AP Company Parameters (Payment Reports tab). If you did check the Attach Vendor Payment Report to Pay History box, the system prints remittances only for vendors that are not set to receive remittance delivery by email (determined by the Method of Payment Info Delivery field in AP Vendor Master, Add'l Info tab).

Effective Date
Enter or select the applicable effective date.
