---
title: "Generate Payments for Terminated Employees | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/generate-payments-for-terminated-employees"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/generate-payments-for-terminated-employees"
---

# Generate Payments for Terminated Employees

Use the PR Auto Termination Pay form to automatically generate payments for terminated employees.
Prior to generating payments, you must make sure that you have set up the system correctly. For more information, see [Process ETPs: Australia](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia).
The steps in this process include:

- determining which employees require a payment

- prompting the system to generate timecard records for each payment type that the employee is entitled to.

There are some payment types that require you to manually create timecard records to process them. For more information, see [Types of Automatic Payments for Terminated Employees](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees)
To generate payments for terminated employees:

1. Open the PR Auto Termination Pay form.

1. Set the selection criteria to determine which employees the system will display in the grid.

1. In the Begin and End fields, enter a separation date range. The system populates the grid with names of all employees who have a separation date in this range.

1. (Option) In the PR Group field, enter the payroll group to limit the employees to those of the specified group.

1. Click Fill Grid. If at any point you need to start over, select Clear Grid to remove all records from the grid.Note: This process doesn't bring employee records into the grid if any the following are true:

- A record for the employee exists in another user's workfile;

- The employee is inactive (the Activecheckbox in the PR Employees form is not selected);

- The employee has already been paid ETPs (the Employment Termination Payments Posted check box is selected in the PR Employees form)

- If PR Group security has been set up and you do not have permissions for an employee's group.

1. Manually add any employee records, as necessary.

1. Review each employee record:

1. If the Separation Reason field is set to R-Redundancy for the employee's record (PR Employees form), the Pay Redundancy and Pay Pre 1 Jan 2010 Redundancy check boxes are enabled and default as selected; clear the checkboxes as necessary.

1. The Pay Leave Loading check box defaults as selected; clear it if you do not need to pay leave loading for this employee. This checkbox is disabled if you have not set up an annual leave load type in the PR Auto Termination Pay Setup form. For more information, see [Set Up Automatic Annual Leave Payments](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-unused-annual-leave-payments/set-up-automatic-annual-leave-payments).

1. The Pay In Lieu of Notice check box defaults as checked; clear it if you do not need to pay the employee an "in lieu of notice" ETP. This checkbox is disabled if you have not set up an "in lieu of notice" type in the PR Auto Termination Pay Setup form. For more information, see [Set Up Automatic Standard ETPs](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/process-etps-australia/types-of-automatic-payments-for-terminated-employees/about-standard-employment-termination-payments-australia/set-up-automatic-standard-etps).

1. If the employee was hired on or before 18 August 1993, the system enables the Std Daily Hours field. For long service leave ETPs, you must enter the standard number of hours worked by the employee in a single day.

1. Select the Generate Payments checkbox for each employee record that you want to generate ETPs for. You can also select the Generate Batch Payments for all Employees to automatically select the Generate Payments checkbox for all records in the grid.

1. Click Generate Termination Payment Timecards.The system determines which ETP type (from the PR Auto Termination Pay Setup form) applies to each employee and displays the PR Timecard Entry batch selection form.

1. In the PR Timecard Entry batch selection form, specify the batch month, payroll group, payroll end date, and pay seq. Click OK.Note: If any records failed and were not added to the timecard batch, the system populates the Error Message field with the reason (PR Auto Termination Pay form).

1. Click Close to return to the PR Auto Termination Pay form. The system updates information in the Batch Month, Batch Number, and Error Message fields for each applicable record.Note: Once you generate timecards, you will be unable to delete the employee records from the PR Auto Termination Pay form. However, if you clear the timecard batch, the system will set the records in PR Auto Termination Pay back to a non-processed state and clear the Batch Month, Batch Number, and Error Message fields. At this point, you would be able to remove the records from the workfile.

1. Click Review & Post Timecards.The system display the PR Timecard Entry batch selection form.

1. Process and post the timecards as normal. For more information, see [Posting Timecards](/en/vista/vista/hr-and-payroll/payroll/time-entry/timecards/posting-timecards).

1. Close the PR Timecard Entry form. The system returns to the PR Auto Termination Pay form and clears the grid of all employee records that had termination payment timecards processed. Additionally, the Employment Termination Payments Posted check box is cleared for all processed employees (PR Employees form, Add'l Info tab).Note: You can delete posted timecards, but that alone will not clear the Employment Termination Payments Posted checkbox. If you delete an ETP timecard, you will need to clear the check the box in the PR Employees form and then follow the steps above to regenerate the timecard record.
Important: If you modify, add, or delete records on the PR Auto Termination Pay Setup form, and any users have records in their workfile, they must clear their workfiles and re-add employees to the workfile. If they do not, the two forms will be out of sync and errors will occur.
