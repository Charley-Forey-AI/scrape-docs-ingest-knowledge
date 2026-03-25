---
title: "Define Spot Work Coverage on an Agreement | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/define-spot-work-coverage-on-an-agreement"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/define-spot-work-coverage-on-an-agreement"
---

# Define Spot Work Coverage on an Agreement

You can set up coverage for unscheduled (spot) work on an agreement so that costs incurred on a work order for unscheduled work are covered by the agreement.
Spot work coverage is defined by service site. You can assign coverage for any service site associated with the customer, even if the service site already has scheduled maintenance defined on the agreement (on the Work Schedule tab).
The coverage details you define for each service site determine what costs are covered by the agreement. For example, you might limit coverage for one service site to labor costs only, while another service site might be covered for all costs (labor, materials, equipment, subcontract, and miscellaneous). You can also define coverage by call type, so that costs incurred on a work order are only covered (as defined) when that call type is referenced on the work order scope.

1. From the main menu, select Service Management  >  Programs > SM Agreements.

1. In the Agreement field, enter the agreement to work with or press F4 to select from a list of valid agreements.

1. Click on the Spot Coverage tab.

1. In the Service Site field, enter the service site to cover or press F4 to select from a list of valid service sites for the customer specified on the agreement.The service site is added with a Coverage Level of None.

1. Save the line.

1. Double click in the line to set up coverage detail.The SM Agreement Site Coverage Dtl form displays.

1. Click in the Seq field. The system automatically defaults to the next sequential number.

1. If spot coverage is based on call type, enter the call type in the Call Type field or press F4 to select from a list of valid call types.If spot coverage is not based on call type, leave the Call Type field blank.

1. Select each of the costs (labor, material, equipment, subcontract, and miscellaneous) covered under the agreement. For example, if the agreement covers only labor and material costs for spot work, select only the Labor Covered and Material Covered checkboxes.

1. Save the record. Once you enter coverage details for a service site, the coverage level on the Spot Coverage tab in SM Agreements is updated to Coverage. Work orders referencing this service site will now be covered by the specified agreement based on the defined coverage details.

Related information

- [SM Agreement Site Coverage Dtl Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-site-coverage-dtl-form)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)
