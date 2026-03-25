---
title: "About Determining Pay Rates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payments/about-determining-pay-rates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payments/about-determining-pay-rates"
---

# About Determining Pay Rates

In the Payroll module, wages are categorized by earnings codes, but specific pay rates are stored in PR Employees, PR Craft Classes, PR Craft Class Templates, and PR Automatic Earnings.
The pay rates are pulled into the Posting
 form or calculated during payroll processing.

- PR Employees - In the PR Employees you may enter an Hourly
 Rate for the employee. The Timecard Entry form compares this rate to the posted
 Craft Class rate and defaults to the higher of the two. Typically, the amount in
 the employee file should be the lowest pay rate for that employee. Therefore, the
 employee will never be paid less than the rate specified in his master file.
 Conversely, if you have a foreman that always gets a certain rate that is
 generally higher than the craft class rate, enter his standard rate and it will
 always be used because it is higher. If the employee should always be paid based
 on the Craft Class rates, it is recommended that the Hourly Rate be 0.00. If the
 employee is salaried, you may enter the salary amount. The default is 0.00.

- PR Craft Classes - Pay rates establish the standard hourly straight time pay for
 specific classes within crafts.

- PR Craft Class Template - If unique rates are needed for
 specific jobs, you can set up special rates in this form and then assign the
 template to a job. When an employee works on a job that has been assigned a
 template, the program looks for a rate for the craft and class posted and then
 compares it to the hourly rate in PR Employees. The highest rate is used to pay
 the employee.

- Add-ons - Add-on Earnings are separate earnings codes that are automatically
 added to the posted earnings code. These are used if reporting is required that
 separates an employee’s total pay into more than one rate, for instance, a base
 rate plus vacation. It is also needed if a portion of the employee’s pay has a
 different taxable status than the base rate. Add-on Earnings are set up in the
 Craft and Craft Class tables. The processing program looks for the earnings code
 and rate using the following hierarchy:

1. PR Craft Class Template

1. PR Craft Template

1. PR Craft Class

1. PR Craft

- Automatic Earnings - The PR Automatic Earnings form is used to set up and maintain
 information about earnings that occur on a regular basis. Salary, 401(k), and car
 allowances are examples of automatic earnings. Entries made here can be used to
 generate a batch of timecards without having to manually enter each Employee’s
 earnings.
