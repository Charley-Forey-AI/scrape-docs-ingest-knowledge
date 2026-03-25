---
title: "Set Up Divisions for a Service Center | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-a-service-center/set-up-divisions-for-a-service-center"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-a-service-center/set-up-divisions-for-a-service-center"
---

# Set Up Divisions for a Service
 Center

Divisions allow you to categorize the different types of work done at a service center (e.g. installations, maintenance, special projects, electrical work, plumbing, and so forth).
You can set up divisions for a service center directly in SM Service Centers or via the SM Divisions form. The following are instructions for both methods.
Note: In order to set up divisions for a service center, you must have already [set up the service center](/en/vista/vista/service-management/service-management-setup/set-up-a-service-center).
Setting Up Divisions in SM Service Centers

1. From the Programs menu of Service Management, double-click on the SM Service Centers icon. This opens the SM Service Centers form.

1. In the Service Center field, enter the service center for which to set up divisions.

1. Click on the Division tab.

1. In the Division field, enter the division name (e.g. Electrical, HVAC, Installs, etc.).

1. In the Description field, enter a description of the division.

1. If you require separate GL accounting by division of work, check the Alternate Department box. Otherwise, skip to Step 8.

1. In the Department field (accessible only if you checked the Alternate Department box), enter the override department for GL accounting when entering work completed on a work order. Note: The system will only use this department if you specify the division on a work order scope.

1. In the Reviewer field, enter a reviewer’s ID in this field to enable that user to mark work orders as ready to bill. Press F4 for a list of active reviewers. Press F5 to access HQ Reviewers.

1. If the division is currently active, check the Active box. Note: Inactive divisions do not display in F4 lookups, nor can they be referenced when setting up accounting treatments (in SM Advanced Accounting Setup) or on a work order (in SM Work Orders).

1. If applicable enter any notes about the division in the Notes field.

1. Save the record.

1. To set up additional divisions for the service center, repeat Steps 4-11.

Note: You can assign call types to a division using the SM Divisions form (accessed by double-clicking in the Division grid). For instructions about assigning call types to a service center/division, see [Step 9](#ID-00043f6d--en__ID-00043fb8) in "Setting up Divisions in SM Divisions" below.
Setting Up Divisions in SM Divisions

1. From the Programs menu of Service Management, double-click on the SM Service Centers icon. This opens the SM Service Centers form.

1. In the Service Center field, enter the service center for which to set up divisions.

1. Select the Division tab and double-click in the grid. This opens the SM Divisions form.

1. In the Division field, enter the division name (e.g. Electrical, HVAC, Installs, etc.).

1. In the Description field, enter a description of the division.

1. If you require separate GL accounting by division of work, check the Alternate Department box. Otherwise, skip to Step 8.

1. In the Department field (accessible only if you checked the Alternate Department box), enter the override department for GL accounting when entering work completed on a work order. Note: The system will only use this department if you specify the division on a work order scope.

1. If the division is currently active, check the Active box. Note: Inactive divisions do not display in F4 lookups, nor can they be referenced when setting up accounting treatments (in SM Advanced Accounting Setup) or on a work order (in SM Work Orders).

1. Assign call types to divisions.

1. Click on the Call Types tab. The screen displays an Available Call Types list box and a Selected Call Types list box.

1. From the Available Call Types list box, select all call types that apply to the division (using the Shift key for consecutive selection or the Ctrl key for random selection).

1. Click Add. Selected call types are moved to the Selected Call Types list box. Note: You can use the Add All button to add all available call types to the Selected Call Types list box. You can also remove call types from the Selected Call Types list box to the Available Call Types list box using the Remove or Remove All buttons.
