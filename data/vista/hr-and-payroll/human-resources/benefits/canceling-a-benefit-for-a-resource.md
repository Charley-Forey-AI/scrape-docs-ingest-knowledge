---
title: "Canceling a Benefit for a Resource | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/benefits/canceling-a-benefit-for-a-resource"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/benefits/canceling-a-benefit-for-a-resource"
---

# Canceling a Benefit for a Resource

You can cancel benefits for a resource if needed in HR
 Resource Benefits.
Canceling the benefit for a resource automatically cancels the benefit for any dependents also assigned that benefit.
Note: Canceling benefits requires having at least one frequency code that is never used in PR Pay Period Control. The recommendation is that you set up a frequency code (in HQ Frequency Codes) specifically for the purpose of canceling benefits.

1. Open HR Resource
 Benefits.

1. In the Resource # field, enter the resource for whom you are canceling the benefit or press F4 to select from a list of resources.

1. In the Benefit Code field, enter the benefit code you wish to cancel. Press F4 and select the Benefit Codes for Reference option to choose from a list of benefit codes set up for the resource.

1. In the Dependent Seq # field, enter 0.

1. Click on the Deduction/Liability Codes tab.

1. For each listed deduction and liability code:

-  In the Freq field, enter the frequency code you designated for canceled benefits or enter a frequency code that is never used in Pay Period Control.

- Select the
 Update PR
 checkbox.

1. Save the record. When you run the update to PR (in HR Update
 Benefit/Salary to PR), the deductions and liabilities will be updated to PR
 with the new frequency code.
Note: Make sure that when canceling a benefit, you do not run the update until after the current payroll is processed and before processing the next payroll.
