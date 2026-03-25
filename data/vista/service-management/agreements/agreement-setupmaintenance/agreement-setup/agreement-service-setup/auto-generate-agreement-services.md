---
title: "Auto-Generate Agreement Services | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/auto-generate-agreement-services"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/agreement-setup/agreement-service-setup/auto-generate-agreement-services"
---

# Auto-Generate Agreement Services

You can have the system automatically generate agreement services based on maintenance tasks you have defined for the serviceable items associated with a service site.
 Before you can generate agreement services, you must have already [set up class/type maintenance tasks](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking/set-up-maintenance-tasks-for-serviceable-item-classes) and associated them with serviceable items. If you have not done so, you must do so before you can proceed here.

Auto-generating agreement services requires the use of the SM Agreement Maintenance form (accessed via SM Agreements) and the SM Maintenance Item Selection form (accessed via SM Agreement Maintenance). The following instructions detail how to auto-generate services for an agreement.

1. Launch the SM Agreements form.

1. In the Agreement field, enter the agreement (quote) to which you are adding agreement services or press F1 to select from a list of valid agreements.

1. Click Tasking. to open the SM Agreement Maintenance form.The SM Agreement Maintenance form displays.Note: For new agreements, this form is blank.

1. Click Select Serviceable Items. The SM Maintenance Item Selection form displays, showing the serviceable items for all service sites defined for the customer associated with the agreement.

1. In the grid, select the Include checkbox for each serviceable item to include on the agreement or click Check All to include all serviceable items.

1. Click Apply.The SM Maintenance Item Selection form closes and you are returned to the SM Agreement Maintenance form. The Tasks grid is populated with all class/type maintenance tasks and their related required tasks. Tasks flagged as Recommended (in SM Class Maintenance) display with the Include checkbox selected.

1. In the Tasks grid, select the Include checkbox for each task you want included on the agreement.You can also use the Check All / Uncheck All buttons to select / deselect items in the grid.

1. Review the required resource entries on the Labor, Material, and Equipment tabs. For each tab, do the following:

1. Click the appropriate tab (for example, the Labor tab).

1. Review all entries in the grid. To remove an entry, select the line and click Remove Requirement.

1. Close the SM Agreement Maintenance form to initiate auto-generation of agreement services.

The system automatically generates an agreement service for each task you selected in the grid. If multiple serviceable items share the same service site and class maintenance task, they are set up as a single agreement service.
Modify the agreement services as needed in the SM Service form. This includes [entering summarized cost estimates](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-detail-form), and adding, deleting, or modifying the related labor, material, and equipment requirements.

Related information

- [SM Agreement Maintenance Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-maintenance-form)

- [SM Maintenance Item Selection Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-maintenance-item-selection-form)

- [SM Service Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-service-form)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)

- [Set Up Equipment Tasking](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/set-up-equipment-tasking)
