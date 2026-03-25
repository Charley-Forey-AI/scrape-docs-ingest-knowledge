---
title: "SMWorkCompletedInventory | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/smworkcompletedinventory"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/smworkcompletedinventory"
---

# SMWorkCompletedInventory

This is a direct import (that is, data is uploaded directly to the data table) that allows for inserting new records and updating existing ones.

Imported work completed inventory lines are set with a status of Provisional in SM Work Orders. This means that unlike manually entered work completed lines, posting will not occur automatically; they must be batched and processed using SM Work Order Cost Posting.
Cost Tax TypeWhen importing records from the text file, if the Cost Tax Type identifier (in Template Detail) is set to Use Viewpoint Default, the system defaults the Cost Tax Type based on the work completed line's taxability status. The taxability of a Work Completed Inventory line is determined by the SM Cost Type assigned to the line and the associated scope's Material Tax Override and Tax Option Override selected options. For detailed information about the tax type default behavior, see [Cost Tax Type](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-5d19be6a-77c6-475f-bccf-2710bc2177f1--en).
Bill Tax TypeThe system uses the same default process for the Bill Tax Type identifier except that if the work completed line is taxable, the system uses the Tax Type defined for the work order scope rather than the tax type specified in the Material Tax Override field. For more information about the tax type default behavior, see [Bill Tax Type](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-completed-purchase-form/field-definitions-sm-work-completed-purchase-form#ID-00045c05--en).

For both the Cost Tax Type and Bill Tax Type fields, if you do not select the Use Viewpoint Default option and the Tax Type for the import record does not match what the system would default, the system allows the entry as long as it is a valid tax type.
For example, the system will not allow an imported Cost Tax Type of 1-Sales for Inventory lines with a Location specified. Likewise, it will not allow an imported Bill Tax Type of 2-Use, as Use tax is not valid as a bill tax type for Inventory lines.
