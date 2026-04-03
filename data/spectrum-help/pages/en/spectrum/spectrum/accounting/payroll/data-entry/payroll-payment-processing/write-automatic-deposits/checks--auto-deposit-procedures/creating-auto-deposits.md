---
title: "Creating Auto Deposits | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/checks--auto-deposit-procedures/creating-auto-deposits"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/checks--auto-deposit-procedures/creating-auto-deposits"
---

# Creating Auto Deposits

Spectrum supports the NACHA export file format and allows you to create an auto deposit file at the end of your payroll cycle to forward to your bank electronically or via disk.
Check with your bank to determine which documents are required from your employees (for example, voided checks, voided deposit slips, or merely their bank # and account #).

## Creating Auto Deposits

- On the Site Map screen, click Admin  >  Installation  >  Payroll Installation, enter your automatic deposit liability G/L account code number.

- Select or do not select the Use Nacha service class code 200 and balanced file format checkbox depending upon your bank's recommendation. Click OK or press F4 to review how your bank needs you to answer this question.

- As employee information comes in, you can modify or record their auto deposit information. Click Payroll  >  Maintenance  >  Employee, and select an employee in order to open the Properties  >  Auto Deposit window.

- In the Status field of the Auto Deposit window, select the Pre-notification type. As you process your payroll cycle, employees whose files are set to Pre-notification will get a payroll check, and the software will produce a test record for your bank to verify data.

- The bank will notify you when it has approved the Pre-notification records. Then
 you can modify the Payroll > Maintenance > Employee > Properties > Auto Deposit > Status field from Pre-notification to Yes and in the Allocation method field designate either Percentage or Fixed amount allocation method.
Note: Your employees can distribute their paychecks to a maximum
 of 5 different savings and/or checking accounts. The full amount of their net pay
 goes into auto deposit (in other words, they cannot receive a partial amount in
 check form).

- For the first payroll cycle (and all cycles thereafter) after changing the Status field from Pre-notification to Yes, the employee will receive a "void" check that provides them with the standard check stub information they've received before. The Auto Deposit function now creates a real record for the bank to transact.
Note: The first time you perform the auto deposit function in
 Spectrum, the software prompts for a series of questions to be answered. The
 terminology of these fields/questions is taken directly from the NACHA guideline
 manual, so you can ask your bank how they should be answered. Viewpoint Support
 staff members are unable to provide these answers. Support staff can assist you if
 you have trouble creating the file.

Related information

- [Processing Auto Deposits](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/write-automatic-deposits/checks--auto-deposit-procedures/processing-auto-deposits)
