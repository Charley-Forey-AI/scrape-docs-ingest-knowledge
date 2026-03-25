---
title: "Initialize the Physical Count Worksheet | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/initialize-the-physical-count-worksheet"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/initialize-the-physical-count-worksheet"
---

# Initialize the Physical Count Worksheet

You can initialize materials to the IN Physical Count Worksheet form based on selected criteria, select File > Initialize to initialize worksheets for all locations where a physical count will be performed. This launches the IN Physical Count Initialize form.

1. In the IN Physical Count Worksheet form, select File > Initialize.The IN Physical Count Worksheet Initialize form displays.

1. In the Beginning Category and Ending Category fields, enter the desired category range. Press F4 to select from a list of valid categories. Leave blank if not restricting by category.

1. In the Beginning Material and Ending Material fields, enter the desired material range. Press F4 to select from a list of valid materials.Leave blank if selecting all materials in the selected category/categories.

1. If the worksheet should include all inventory locations, select the Select all Inventory Locations checkbox. Leave the checkbox unselected if you want to manually select locations (using the Available Inventory Locations list) or if you want to also want to filter by physical location.

1. If you want to include physical locations, select the Include Physical Locations checkbox. Then, either select the Select all Inventory Locations checkbox to include all inventory and physical locations or leave the Select all Inventory Locations checkbox unselected and manually select the inventory/physical locations to include using the Available Inventory Locations list.

1. (Optional) In the Count Date field, specify a default count date for all entries on the worksheet.Entering a count date enables the Initialize System Count checkbox.

1. If you want the system to include a count for each material and location, select the Initialize System Count checkbox.The system count is compared with the physical count and any discrepancies (negative or positive) are displayed in the Adj Units column (in the IN Physical Count form). For more information on processing a physical count, see [IN Physical Count Worksheet Form](/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-worksheet-form#ID-00014565--en__ID-00014565).

1. If you want the system to include activity for the date in the Count Date field, select the Include Count Date Activity checkbox.

1. Select Update.The system begins initialization. Once complete, you are prompted to initialize more entries.

1. Select Yes to enter new selection criteria and initialize more entries or No to exit the form and return to the IN Physical Count Worksheet form.

 The system populates the worksheet grid with all materials meeting your selection criteria.
 Print the IN Physical Count Worksheet report (accessed by selecting File > Physical Count Worksheet Report) and perform a physical count. Once your physical count is complete, update the Physical Count, Counted By, and Adj Units fields in the IN Physical Count Worksheet form accordingly.
