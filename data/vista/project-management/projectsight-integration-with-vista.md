---
title: "ProjectSight Integration with Vista | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/projectsight-integration-with-vista"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/projectsight-integration-with-vista"
---

# ProjectSight Integration with Vista

Synchronize project financial data between ProjectSight and Vista with this integration, keeping your records up to date across both systems and eliminating dual entry.

## Integration Requirements

Your organization must fully complete all integration setup and configuration before you can sync and send data between Vista and ProjectSight. This includes configuring Vista companies and identifying the direction of data flow for certain workflows. Trimble Viewpoint will assist you with setup.
In order to use this integration, you must have:

- Access to both Vista and ProjectSight.

- Cloud-deployed version of Vista. (This integration is not available to on-premises customers.)

## Integrated Workflows

The integration currently supports the following workflows:
Project SetupNote: Each ProjectSight portfolio must be mapped to a single Vista company. See the ProjectSight Help on [Portfolio Linking](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/ERP/Portfolio-Linking.htm) for more details about associating a portfolio with a specific ERP company.

- [Link a Customer / Vendor from Vista to a ProjectSight Company](/en/vista/vista/project-management/projectsight-integration-with-vista/link-a-customer--vendor-from-vista-to-a-projectsight-company): Import or link customers and vendors from Vista to ProjectSight. After linking, you must maintain customer and vendor data in both systems.

- [Link a Job from Vista to
 a ProjectSight Project](/en/vista/vista/project-management/projectsight-integration-with-vista/link-a-job-from-vista-to-a-projectsight-project): Link Vista jobs with ProjectSight projects. After linking, you must maintain job / project data in both systems.

- ProjectSight prime contracts are automatically created from Vista JC Contracts when the JC Job is linked to a ProjectSight project.

Budget Management

- [Sync Budget Records Between Vista and ProjectSight](/en/vista/vista/project-management/projectsight-integration-with-vista/sync-budget-records-between-vista-and-projectsight): Create budget records in either Vista or ProjectSight, depending on your organization's preference at setup. Send budget data from one system to the other, then maintain the budget records in ProjectSight. New budget codes are sent from ProjectSight into Vista.See the ProjectSight Help on [Budgets](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/Online_Help/Records/BCM/Budgets.htm) for more information about budget records.

- All Vista HQ Units of Measure integrate into the ProjectSight portfolio-level Units of Measure. If you delete a UOM in Vista, that UOM is removed from ProjectSight.

Commitment Management

- [Send Subcontracts from Vista or ProjectSight](/en/vista/vista/project-management/projectsight-integration-with-vista/send-subcontracts-from-vista-or-projectsight): Create subcontracts in either Vista or ProjectSight, depending on your organization's preference at setup. Post the subcontract to send the data, then maintain the records in both systems.

- [Send Purchase Orders from Vista or ProjectSight](/en/vista/vista/project-management/projectsight-integration-with-vista/send-purchase-orders-from-vista-or-projectsight): Create purchase orders in either Vista or ProjectSight, depending on your organization's preference at setup. Post the PO to send the data, then maintain the records in both systems.

Change Management

- [Send Potential Change Orders from ProjectSight to Vista](/en/vista/vista/project-management/projectsight-integration-with-vista/send-potential-change-orders-from-projectsight-to-vista): Create potential change orders in ProjectSight and send these to Vista PM Pending Change Orders and JC Change Orders (authorized users only). Post the potential change order to send the data, then maintain the records in ProjectSight.

- [Send Subcontract Change Orders from ProjectSight to Vista](/en/vista/vista/project-management/projectsight-integration-with-vista/send-subcontract-change-orders-from-projectsight-to-vista): Create subcontract change orders in ProjectSight to Vista SL Change Order Entry (authorized users only). Post the subcontract change order to send the data, then maintain the records in both systems.

## ProjectSight Help

For ProjectSight-specific information about integrating with an ERP, see the ProjectSight Help on [ERP Integration](https://prod.projectsightapp.trimble.com/Web/Web%20Help/Content/ERP/Web-ERP.htm).

## Records in Vista and ProjectSight

Vista and ProjectSight use different terminology to refer to certain records, processes, and data. See the following table for the associated records.
Vista Record NameProjectSight Equivalent
AR Customers
AP Vendors
Companies
JC JobsProjects
JC ContractsPrime Contracts
JC Job PhasesBudget Code Structure
JC Original EstimatesBudget Code Original Budget

SL SubcontractsContracts (with type set as subcontract)

PO Purchase OrdersPurchase Orders
PM Pending Change Order
JC Change Order (Internal)
Potential Change Orders
SL Subcontract Change OrderSubcontract Change Orders
