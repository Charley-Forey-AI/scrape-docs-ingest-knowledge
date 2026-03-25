---
title: "Material Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/material-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/material-orders"
---

# Material Orders

You can create material orders to allocate inventory
 materials for use on specific jobs.
Material Orders are used to assign and allocate materials to jobs, creating committed
 units and costs for the specified job/phase/cost type. These costs are relieved and
 posted as actual costs once the material order is confirmed.
When creating material orders to reserve materials
 for jobs, you create committed units and costs in Job Cost and increase the allocated
 quantities in IN. Confirming a material order relieves the remaining committed units and
 costs in JC and creates actual units and costs, while also reducing the allocated and on
 hand inventory.
 Material Orders can be created in two ways.

- [IN Material Order Entry ](/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-entry-form) - All materials on a material order must
 come from the same location, but may cover more than one job.

- [PM Material Orders ](/en/vista/vista/project-management/materials/about-the-pm-material-orders-form) - You can designate
 materials from multiple locations, and when material orders are initialized, the
 system will assign a separate material order number to each location indicated.
 Multiple materials ordered from the same location will appear as sequential
 items on the material order. Although set up in PM, the actual material orders
 are not created until you use the [PM Interface](/en/vista/vista/project-management/setupmaintenance/pm-interface-form) form.

 When setting up material orders, the job
 pricing options set up in the [IN Company Parameters ](/en/vista/vista/job-resources/inventory/setup--maintenance/company/in-company-parameters-form) form determine how the materials
 are priced.
