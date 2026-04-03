---
title: "Renew Service Contract | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/maintenance-overview/service-contracts/renew-service-contract"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/maintenance-overview/service-contracts/renew-service-contract"
---

# Renew Service Contract

Use the Renew Service Contract
 window to renew expired contracts one at a time.
To access this window, click Renew in the Service
 Contracts screen. To renew contracts in bulk, use [Contract Renewal Management](/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/data-entry-overview/contract-renewal-management).
Renewing a contract copies contract properties, equipment, tasks,
 images, notes and exceptions set up for the expired contract to the new contract. The
 budget hours and budget cost values are set equal to the budget totals on the expired
 contract. If the current standard task budget values are needed instead of the
 contract-specific budget from the expired contract, use the calculate feature on the
 Edit Service Contract window.
This update will compile any warnings (ex. visits not copied) and present the list at the end of the update. You will then be offered the option to roll back the update, if feasible.
Note: This update will not copy billing schedules. You will
 need to navigate to the Edit Service Contract > Billing tab to generate billing schedules for the renewed contract.
Fields/Buttons
Descriptions

From expired contract

The fields in this section will default
 from the selected contract on the Service Contracts
 screen. These fields are view-only.
To renewal contract

Site
The site code and description from the
 expired contract will display in this field. No changes are allowed.
Contract
Enter a new contract code in this
 field. This field will only accept a contract code that does not yet exist.
 After entering a new contract code the software will prompt for a contract
 description and type. If the Service Contract
 Installation for 'Use auto-sequenced service contract numbers?' checkbox is
 selected, then when you leave the 'Contract #' field blank, the next
 available contract number will default automatically. If a non-sequenced
 code is desired, the simply type the alternate code here.

Contract type
This field will default from the
 expired contract.
Start date
This view-only field will display the
 next day after the 'End date' of the expired contract.
End date
Enter a new end date in this field. The
 new end date must be equal to or later than the new start date. If the date is
 outside the G/L fiscal calendar date range a warning will appear, but you will
 be allowed to continue.
Contract amount
Enter a contract amount for the new
 contract in this field. Note: This field will
 be disabled if the billing source is set to Work Order.

# scheduled visits
Enter the number of scheduled visits
 for the contract in this field. The default number of visits will be the same
 as the expired contract, but you will be able to change this value.
# scheduled billings
Enter the number of scheduled billings
 for the new contract in this field. The default number of billings will be the
 same as the expired contract, but you will be able to change this value. Note: This field will be disabled if the billing
 source is set to Work Order.

Earned calculation
Select an earned calculation basis for
 the renewed contract in this required-entry field. This field will default from
 the expired contract, unless set to 'Other'. If the expired contract basis is
 set to 'Other', the renewal will default based on the setting in [Contract Type File Maintenance](/en/spectrum/spectrum/service/service-contracts/spectrum-menus-overview/maintenance-overview/contract-type-file-maintenance).
 Protection will be incorporated into this window to assure that the specified
 contract type is allowed for the selected earned calculation basis, and vice
 versa. During the contract renewal update, the software
 will automatically build the Earned Revenue Schedule in the new contract
 based on the earned calculation specified in this field.
Note: This field will be disabled if the billing
 source is set to Work Order.

Copy scheduled billings from expired contract?
Select this checkbox to copy scheduled
 billings from the expired contract. When a billing is copied, the work summary
 and alert text will be stored in the new contract, and the scheduled date of
 the billing is incremented based on the number of months specified in the
 Increment scheduled billing
 dates by field. The system will read for
 billing records assigned to the expiring contract and calculate the new
 scheduled date by adding the number of months specified here to the stored
 date in the expiring contract.

Copy scheduled visits from expired contract?
Select this checkbox to copy scheduled
 visits from the expired contract. When a visit is copied, the work summary and
 alert text will be stored in the new contract, and the scheduled date of the
 visit is incremented based on the number of months specified in the Increment scheduled visit dates
 by field. The software will validate the
 number of scheduled visits does not exceed those within the current contract
 date range. When the maximum number of visits is reached, no more visits
 will be copied from the expired contract. Visits in the expired contract
 that do not contain equipment codes set up in the new site are not copied to
 the new contract, and will not impact the number of scheduled visits within
 the contract period.
As each visit is copied to
 the new contract, the price of the visit will be copied from the source
 visit and the new contract amount will be calculated and stored if the
 billing source is set to Work Order. The newly calculated Contract price will
 display in the list box.
