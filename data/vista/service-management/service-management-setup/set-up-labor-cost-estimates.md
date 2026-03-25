---
title: "Set Up Labor Cost Estimates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-labor-cost-estimates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-labor-cost-estimates"
---

# Set Up Labor Cost Estimates

You can use the SM Labor Cost Estimate form to set up labor cost estimates by technician, craft, class and/or effective date.
The rates defined here will be used to default the cost rate for manually and auto-added labor requirements on a work order quote or work order, as well to determine the cost rate to use when calculating allocated amounts for labor allocations on an agreement.
Note: It is not necessary to set up labor cost estimates here unless you want to override the standard employee/technician or craft/class rates.
To determine the cost rate for labor requirements and allocations, the system reviews the labor cost estimate records entered here and, using a [specific hierarchy](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-labor-cost-estimate-form), finds the closest match based on the current date and the information specified on the labor requirement or allocation entry.
The following details how to set up labor cost rates.

1. In the Seq field, enter N, New, or +.

1. In the PR Co field, enter a payroll company.

1. Optionally, you can use the Technician, Craft, and Class fields to define additional criteria for applying this labor cost rate to a detailed labor cost estimate. If you enter a value in any of these fields, the equivalent fields in the detailed labor cost estimate record must exactly match for the system to use the rate that you set up here.

1. In the Cost Rate field, enter the labor cost rate.

1. Save the record as normal.

Enter Effective Date cost rates if applicable.

1. Optionally use this tab to define cost rate changes by effective date. For more information about effective dates, see [Effective Dates](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-labor-cost-estimate-form) in the online help for SM Labor Cost Estimates.

1. Click the Effective Date tab.

1. In the Effective Date field, enter the date the specified cost rate becomes effective.

1. In the Cost Rate field, enter the new cost rate.

1. Save the record. Note: You cannot create identical labor cost rate records in this form. If you create an identical record and attempt to save it, the system will display a warning and will not save the record.

Related information

- [Set up Labor Requirements](/en/vista/vista/service-management/work-orders/about-work-order-scope-budgets/required-resources-for-work-orders/set-up-labor-requirements)

- [SM Agreement Labor Allocation Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-labor-allocation-form)
