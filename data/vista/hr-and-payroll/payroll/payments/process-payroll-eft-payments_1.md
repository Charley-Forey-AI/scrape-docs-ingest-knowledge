---
title: "Process Payroll EFT Payments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/process-payroll-eft-payments_1"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/process-payroll-eft-payments_1"
---

# Process Payroll EFT Payments

Use the PR EFT Payments form to process EFT payments for your pay period.
Note: The system updates the paid date to the CM module. You will need to ask your bank how many days in advance they will need the file before paying your employees.

Processing EFT payments consists of two steps:

1. Assign EFT payment information to eligible employee earnings within an open pay period.

1. Generate a data file to submit to your bank for payment.

To process EFTs:

1. In the PR EFT Payments form, select the Assign tab.

1. In the PR Group field, enter the payroll group for which you are processing EFT payments or press F4 to choose from a list.

1. In the Pay Period Ending Date field, enter the pay period ending date or press F4 to choose from a list of valid dates.

1. For the Payment Seq# field, and for the given payroll group and pay period ending date, choose one:

- If you want a single data file which includes all payment sequences, leave this field blank.

- If you want to create a data file for one particular payment sequence only, enter the payment sequence number.

1. If you want to restrict assigning EFT payment information by employee:

1. Select the Restrict by Employee SortName? checkbox.

1. In the Beginning Employee Sort Name and Ending Employee Sort Name fields, enter the employee or range of employees to process. You must enter a value in both fields.

1. In the Effective Date field, enter the date that you want the bank to use when depositing payments to your employees. The system defaults the same month and year in the Paid Month field.

1. In the CM Reference # field, enter a number that will be assigned to all of your EFT payments.Note: The number you enter here does not affect or interfere with any of your printed check numbers.

1. Click Update.The system displays a confirmation message and assigns the effective date, paid month, and CM reference number to all of your employees receiving EFT payments for this pay period.

1. Click Close.

1. Select the Download tab.

1. For U.S. companies only, select the Active radio button from the Export File Type section of the form.For Australian and Canadian companies, this field is set to Active and disabled.
Note: U.S. companies only:

- Select Prenote if an employee has just set up direct deposit and you want to check that their account information is accurate. The employee will receive a check.

- Select Test if you are initially testing that you have information set up correctly for your bank.

1. Enter the payroll group, pay period ending date, CM reference number, and description in their respective fields, as necessary.Note: Default values come from the Assign tab.

1. Canada only: in the File Creation Number field, enter a number that uniquely identifies this file for the bank.

1. (Optional) In the Download Filename field, change the default entry. Press F1 for more information.

1. Select File > Audit Report.The system displays an active audit report.

1. Review the report to ensure the EFT information is accurate. Print if required.Important: There is no other opportunity to print this report before you create the data file.

1. Click Continue to create the data file.What happens next depends on whether you are using the Secure File Path function. For more information, see [Secure File Path](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/secure-eft-data-files).

- If using a Secure File Path - Vista saves your file directly to the location specified in the PR Company Parameters form.

- If not using the Secure File Path - use the Save Export File As window to choose a location to save the file, changing the filename if you want.

The system completes this process in the background. During this time, the Background Jobs form displays the processing status. You may close the job queue while the system completes processing.Note: To open and view this and any other jobs in the queue, navigate to Main Menu > View > Display Job Queue.

1. Click Close.

1. Submit the downloaded file to your bank for processing.Note: You can also use the above instructions to recreate text files for closed pay periods. Just make sure to specify the closed pay period ending date, as well as the appropriate CM reference number.


 You now have a data file for the payment sequence(s) you chose. If needed, repeat for other payment sequences.
[Print direct deposit stubs](/en/vista/vista/hr-and-payroll/payroll/payments/print-direct-deposit-stubs) for your employees.Note: If you encountered any problems with your EFT or you have any other need to reprocess EFTs (for all employees) within the payroll group and pay, use the Clear tab in the PR EFT Payments form to clear existing EFT information. If instead you only want to clear payment information for certain employees, use the PR Employee Pay Sequence Control form. For more information, see [Clear EFT Payment Information](/en/vista/vista/hr-and-payroll/payroll/payments/clear-eft-payment-information).

Related information

- [About the PR EFT Payments Form](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-eft-payments-form)

- [PR Direct Deposit Print Form](/en/vista/vista/hr-and-payroll/payroll/payments/pr-direct-deposit-print-form)

- [Print Payroll Checks](/en/vista/vista/hr-and-payroll/payroll/payments/print-payroll-checks)

- [PR Check Print Form](/en/vista/vista/hr-and-payroll/payroll/payments/pr-check-print-form)

- [Processing Payroll](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/processing-payroll)
