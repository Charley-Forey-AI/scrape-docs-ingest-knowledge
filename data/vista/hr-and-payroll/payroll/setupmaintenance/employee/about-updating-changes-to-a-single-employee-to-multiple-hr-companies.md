---
title: "About Updating Changes to a Single Employee to Multiple HR Companies | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-updating-changes-to-a-single-employee-to-multiple-hr-companies"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/about-updating-changes-to-a-single-employee-to-multiple-hr-companies"
---

# About Updating Changes to a Single Employee to Multiple HR Companies

If you make changes to an employee's information in PR Employees, and the employee exists in multiple HR companies pointing to that PR company, the system will update each applicable HR company based on the PR Update Options specified for each of the associated HR companies in HR Company Parameters.
 The PR-to-HR update is a 1-to-many update, since multiple HR companies can point to the same PR company. However, the HR-to-PR update is a 1-to-1 relationship, since each HR company can point to only one PR company; therefore, changes made for an employee in HR update the associated PR company only. No updates are made for that employee in any other HR company in which the employee resides.
For example, you may use separate HR companies for applicants and employees. In this instance, set up applicants in one HR company, update them to PR when hired, and then update them from PR to the HR company used for employees. When you change an employee's information in the PR company, the system updates both HR companies; however, if you make the change in one of the HR companies, only the PR company is updated.
