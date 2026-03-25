---
title: "Enter Summarized Cost Estimates for Agreement Services | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/enter-summarized-cost-estimates-for-agreement-services"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/enter-summarized-cost-estimates-for-agreement-services"
---

# Enter Summarized Cost Estimates for Agreement Services

You can enter summarized cost estimates for labor, material, equipment, subcontract, and other costs associated with an agreement service using the SM Service Detail form.
You must have already [set up your agreement](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/set-up-an-agreement-in-sm-agreements) and [agreement services](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup).
The system uses the cost estimates to determine the total estimated cost for the agreement service. For agreement services using the Time of Service, Rate Template pricing method, you can also enter markup rates for cost estimates to derive pricing estimates. The system will use the cost estimates and pricing estimates to determine the estimated profit for the agreement service.

1. Open the SM Agreements form.

1. In the Agreement field, enter the agreement or press F4 to select from a list of valid agreements. Agreement must be in Quote status.

1. Click the Work Schedule tab and then double-click in the grid to open the SM Service form.

1. In the Service Seq field, enter the agreement service or use the /  buttons in the toolbar to select the desired agreement service..

1. In the Budget section, make sure the Derive checkbox is unselected.

1. Click Details. The SM Service Detail form displays.

1. In the Labor Hours field, enter the estimated labor hours.

1. If the agreement service is using a Daily, Weekly, Monthly, or Yearly scheduling option (defined on the Schedule tab in SM Service), use the Craft and Class fields to enter the craft/class to which the budget hours apply.Note: If the Task Scheduled option (on the Schedule tab in SM Service) is selected for the agreement service, these fields are disabled.

1. In the Cost Estimates fields, enter the estimated cost amounts for labor, materials, equipment, subcontracts, and other expenses.

1. For T&M, Rate Template services only, enter the markup rates / price estimates using one of the following methods:

- To use a common markup rate, select the Common Markup Rate checkbox and then enter a markup rate in the Markup field of any cost estimate. The system will set the markup rate for the remaining cost estimates equal to the value you entered and calculate the price estimate for each cost estimate accordingly.

- To set individual markup rates, leave the Common Markup Rate checkbox unselected and then enter a markup rate in the Markup field for each cost estimate. The system will automatically calculate the price estimates accordingly.

- If you do not know the markup rates, you can enter pricing estimates and have the system calculate the markup rates for you. To do this, leave the Common Markup Rate checkbox unselected and then enter the appropriate value in the Pricing Estimates field for each cost estimate.

1. Save the record.

Related information

- [SM Service Detail Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-detail-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)
