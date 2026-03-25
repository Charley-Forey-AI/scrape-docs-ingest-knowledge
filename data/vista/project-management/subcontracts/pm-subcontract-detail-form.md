---
title: "PM Subcontract Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form"
---

# PM Subcontract Detail Form

Use this form to set up subcontract detail information.
Note: You can only open this form if the SL in Use checkbox in [PM Company Parameters](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form) is selected.

The type of subcontract detail records displayed on the Non-Interfaced and Interfaced tabs depend on how you accessed this form.

- If accessed from the main menu or PM Project Phases, grids display original subcontract detail records (Record Type ‘O-Original’)

- If accessed from PM Approved Change Orders, grids display approved change order subcontract detail (Record Type ‘A-Approved CO’s)

- If accessed from PM Pending Change Orders, grids display pending change order subcontract detail (Record Type (P-Pending CO’s).

Note: When you access this form from the main menu, you have the option to change the Record Type from Original (default) to either Approved COs or Pending COs. Additional fields related to approved or pending change orders will display in the grids (for example, ACO and ACO Item or PCO Type, PCO, and PCO Item). Note that these additional fields do not display if PM Subcontract Detail is accessed from any of the forms listed above, since the record display will be limited to records related to the calling form.

You can set up subcontract detail manually by setting up change order phases (via PM Pending Change Orders or PM Approved Change Orders) where the cost type is equal to the cost type specified for subcontracts in PM Company Parameters, or by importing from third-party estimating software (using PM Data Import). If importing estimate detail, phases with subcontractor costs are automatically set up here.
Typically, phases entered in this program will be those assigned a Subcontract cost type. However, you can also enter phases for subcontract issue that are assigned cost types other than Subcontract. For example, you may have material orders, equipment leases, and so forth, where you require contracts containing more detail than purchase orders allow.

## Non-Interfaced/Interfaced

The Non-Interfaced tab displays all items that have not been interfaced to the accounting modules and is used to set up/edit subcontract detail. Once a subcontract detail item is interfaced, it is moved over to the Interfaced tab and cannot be edited or deleted. If you need to change the dollar amounts for an interfaced subcontract, create a subcontract change order.
In order to include subcontract detail when interfacing the project or pending/approved change orders for the project, you must select the Send box for each phase that is ready to be interfaced. Interfaced subcontract detail updates the Subcontract Ledger module.
Note: Pending or approved SL change order detail must be assigned a SCO number and flagged as ‘Send’ in order to be interfaced.

If the Allow adding new subcontract item during subcontract change order entry checkbox is selected in PM Company Parameters, you can add a new subcontract item to an approved or pending change order on this form (Non-Interfaced tab). When you add a new item record to the grid, the system displays a message asking if you want to add this item to allow for pre-billing. If you select Yes, the system adds the subcontract item with 0.00 amounts to the existing subcontract. This enables you to invoice against this item, even without the original estimate being established. When you interface to SL, the system will then record the original and current amounts to the item. If you select No, the item record remains in the grid, but the item is not added to the subcontract and you will not be able to invoice against the item.

## Available Estimate / Non-Interfaced / Remaining Estimate

These display-only fields are visible in the informational display above the Non-Interfaced and Interfaced tabs. They show estimate information for the selected subcontract detail line. These values are calculated as follows:
FieldCalculation
Available EstimateCurrent Estimated Cost - Actual Cost - Remaining Committed Cost + Non-Interfaced Estimated Cost
Non-InterfacedThis is a more complex calculation that takes a number of factors into consideration. However, in general, this calculation is the sum of the amount and taxes from PM Subcontract Detail and based on certain factors, the subtraction of some SL Item and SL Change Order detail costs (which can include taxes), plus Non-Interfaced Estimated.
Remaining EstimateAvailable Estimate - Non-Interfaced

## Subcontract Numbers

You can enter subcontract numbers manually or you can select the Initialize button to automatically generate them.

- Manually - If you are assigning a new subcontract number, you must first assign a vendor to the item. If you are assigning an existing subcontract number, the vendor number is not required because the system automatically defaults the vendor from the subcontract header set up in PM Subcontracts.

- Automatically - The Initialize button automatically generates subcontract numbers based on the Subcontract Format Options you defined in PM Company Parameters. However, for this option to work, you must assign a vendor to each applicable phase/cost type sequence. The system skips any phase/cost types that do not have a vendor assigned. If a subcontract already exists for a vendor, the system assigns the phase/cost type sequence as an item on the existing subcontract.

If the Initialize button is disabled and you are entering a change order, the Disable Initialize button for change order subcontract detail checkbox in PM Company Parameters is probably selected. This means that you have to manually enter subcontract items.
Note: A subcontract item is a change order if you select A-Approved CO's or P-Pending CO's from the Record Type drop-down.

[About Subcontract Buyout](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)
[PM Subcontracts Form](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)
[PM Company Parameters Form](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)
