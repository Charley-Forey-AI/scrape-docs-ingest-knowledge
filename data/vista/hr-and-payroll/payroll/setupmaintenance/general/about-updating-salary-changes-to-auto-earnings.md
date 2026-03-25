---
title: "About Updating Salary Changes to Auto Earnings | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-updating-salary-changes-to-auto-earnings"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-updating-salary-changes-to-auto-earnings"
---

# About Updating Salary Changes to Auto Earnings

You can have salary changes automatically updated to an
 employee's automatic earnings in PR Automatic Earnings.
If you selected the Update Auto Earnings checkbox for an employee/earnings code in PR Employees, the system automatically updates the Rate/Amt field when changes are made to an employee's salary (via PR Employees or HR Salary History).
If there is only one auto entry for the employee's specified earnings code, the system updates the full salary amount to that earnings code. However, if there are multiple auto entries set up for an employee/earnings code, the system distributes the salary proportionally to the applicable auto entry sequences.
 ​The system bases the proportional distribution on the Rate/Amt defined for each sequence for the specified earnings code (in PR Automatic Earnings) and the Salary specified for the employee (in PR Employees).​
For example, in PR Employees, you specify Earnings Code 1, with a salary of $1,000. You then set up two sequences for Earnings Code 1 in PR Automatic Earnings: one for Job 100 with a Rate/Amt of $400 and one for Job 300 with a Rate/Amt of $600. In this case, the first entry is 40% of the employee's salary ($1,000) and the second entry is 60% of the salary.
You then change the employee's salary to $1,500. In PR Automatic Earnings, the system determines there is a difference between the employee's Salary (in PR Employees) and the total amount for the two existing auto entry sequences, and updates them as follows:​
​Earn Code 1, Seq 1: $600 ($1,500 x .40 = $600)​
​Earn Code 1, Seq 2: $900 ($1,500 x .60 = $900)​
​If the system calculation results in amounts that do not fully equal the employee's Salary, the system then adjusts the highest earnings code sequence to ensure the total amount reflects the specified Salary.​
Note: If all sequences for an employee/earnings code have Rate/Amt values of zero, the system will not distribute the new Salary amount to each sequence; rather, it will update the full salary amount to the first sequence for that earnings code. For instance, using the example above, if both entries had zero amounts, the system would apply the full $1,500 to Earn Code 1, Seq 1 and leave Earn Code 1, Seq 2 at zero.

## Changes to an Employee's Earnings Code

If you change the earnings code for an employee in PR Employees and the ​Update Auto Earnings​ checkbox is selected, the system updates PR Automatic Earnings as follows:

- If the earnings code exists for the employee in PR Automatic Earnings, the system updates the specified salary amount to the specified earnings code or distributes the amount proportionally if multiple sequences exist for the earning code.

- ​​​​If the earnings code does not exist in PR Automatic Earnings, no update occurs.

Note: The system also updates existing auto entries for an employee/earnings code if the only change you make in PR Employees is to select the ​Update Auto Earnings​ checkbox.
