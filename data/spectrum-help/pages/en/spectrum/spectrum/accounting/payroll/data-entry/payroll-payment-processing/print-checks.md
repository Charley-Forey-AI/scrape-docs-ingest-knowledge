---
title: "Print Checks | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/print-checks"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/print-checks"
---

# Print Checks

Print Checks is used to print regular payroll checks or
 automatic deposit statements, and may be printed in job order, alphabetical order or employee
 code order.
The software will not proceed with payment processing until you choose to print. This means
 that even if all the checks in the current cycle are manual or void, you must choose to
 print checks before you can proceed with a new check cycle. In this event, when you do
 print, since there are no regular checks in the cycle, nothing will print and the software
 will then allow you to proceed.
Benefit totals will be obtained from the Payroll Time Off Bank Log Table using the check date for 'YTD Earned'. The software can be set up so that accrued vacation, holiday, and sick leave totals are not printed on checks. This is a benefit for those contractors that just record the vacation taken and don't use the benefit accrual. These defaults may be set in the Payroll Installation screen. If the Set to zero anniversary? checkbox was selected on the [Time Off Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/time-off-code-maintenance) screen, the vacation, holiday and sick balances will be calculated for the current year only based on the employee's anniversary date.
For checks with add-on or deduction year-to-date balances, the software will display these balances on each check, even if there is no add-on or deduction on the current check. If there are more add-ons and deductions than will fit on the pay stub, the additional amounts will be summarized under the classification of OTHER.
State Disability Insurance (SDI) and Resident Worker's Compensation amounts will be listed separately on this report.
Note: If the "Display accumulated balance on paycheck?"
 option is selected in the [New/Edit Deduction/Add-on Code - Properties](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/deduction--add-on-code-maintenance/create-or-edit-a-deduction-or-add-on-code/newedit-deductionadd-on-code---properties) screen, the accumulated balance will display instead of the Year
 To Date amounts. The column title on the form will still say "Year To Date."
[Auto-Signature manual](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/0751eeb0-8ea9-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiIwNzUxZWViMC04ZWE5LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMzEzNzcsImp0aSI6IjNhNDVhMGVmNjU3NDRiOTY5NzE5YWJjNDRjNjk5ZDVjIiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.VM72bojKM58mw1UcsormBOBThjUtmLxkaeLwvIIbjqk&response-content-disposition=filename%3D%22Auto-Signature_Procedures_v1422.pdf%22)
[Canadian Auto-Signature manual](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/07a8e850-8ea9-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiIwN2E4ZTg1MC04ZWE5LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMzEzNzcsImp0aSI6IjM3OWU0MmFmM2VhNzRlOTNhMjJhYmEwY2QzZGVhZGM3IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.7D9eqDhL8iXH0PtqEvhNqogbEDYslTqpft7LRU18hC8&response-content-disposition=filename%3D%22Auto-Signature_Cheques_Procedures_v1422.pdf%22)
[MICR Checks Manual](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/08058740-8ea9-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiIwODA1ODc0MC04ZWE5LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMzEzNzcsImp0aSI6IjQ5ZTRhMjhlYWM1MTRjN2Q5NmRhZWI0NzY5MmYxM2I4IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.HU795ft-2R7sYTeRNodRDNn8larhTLqzsraNYoCDp6E&response-content-disposition=filename%3D%22MICR_Checks_Procedures_v1423.pdf%22)
[Canadian MICR Cheques Manual](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/087d9d70-8ea9-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiIwODdkOWQ3MC04ZWE5LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMzEzNzcsImp0aSI6IjcyNjMxYTRlZTI5OTRhZDdhYThjZDI1NWQ0MWMzZDY4IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.rJ5pIaMEhr315AlA_dpvGZR1lqvSHtUl752vDLhsTf8&response-content-disposition=filename%3D%22MICR_Cheques_Procedures_v1422.pdf%22)
