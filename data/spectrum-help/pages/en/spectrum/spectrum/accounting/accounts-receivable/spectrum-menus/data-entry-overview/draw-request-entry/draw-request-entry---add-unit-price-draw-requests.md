---
title: "Draw Request Entry - Add Unit Price Draw Requests | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/draw-request-entry---add-unit-price-draw-requests"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/draw-request-entry/draw-request-entry---add-unit-price-draw-requests"
---

# Draw Request Entry - Add Unit Price Draw Requests

When items bid for a job are made up of a number of components, and the job uses unit pricing for draw requests, the details portion of the screen allows you to enter individual components for each bid item. When adding new billing items for unit price jobs, the pricing logic defaults the special price first by customer/job, then customer only (if the job field is left blank) as the second priority, and finally the standard company pricing (if the customer field is left blank) as the last resort. The billing item lookup windows also reflect this customer/job option.
Draw Request Billing Entry and reports for unit price contracts use the default unit price and quantity displays masks from Contracts. This is useful in designating how unit price and quantity figures appear on these reports, on a line-by-line basis, particularly when tracking very large or very small amounts.
After a job has been set up, it is recommended that billing items be entered in the Contracts screen before phases are set up in the Phases screen.
To add materials stored but not yet placed in service for a unit price contract, a separate line for the stored materials should be added to the draw request. Use a zero contract amount and enter the amount of the stored materials in the Quantity this period column. Then as the work is completed, move the quantities/dollars from the stored line to the actual bid item line. As the materials are moved, the negative quantity to the stored materials and the positive quantity to the bid item will create a zero quantity/dollar difference, but the amount will move to the bid item.
Important: If no information appears in the detail lines after the initial fields have been completed, do not change the job contract amount in the Jobs screen which will not be reset. If there are detail lines, the software will automatically set the original contract to the sum of the detail.
Field
Description

Group
Enter a unique code for this group of billing items. This code is used to distinguish one item record from all other item records in the file. Refer to the [Example: Setting Up Bill Groups](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/example-setting-up-bill-groups) topic for examples.
The corresponding Group description displays to the right of this field. If an existing row is edited, the bill group description will be changed to all rows assigned to the bill group of this row.

Bill item
Enter the billing item for this line. Standard items may be selected from those previously set up in Set Up Standard Fixed Billing Items, new standard items may be added through the Billing Item Code Window, or non-standard items may be typed directly into this field. Entry in this field is required.
Ideally, billing items were entered in Contracts when the job was first set up. In that case, if the Create detail from draw request master (contract detail) file checkbox was selected, click OK. All billing items specified in the contract will display.
If billing items were not entered in the contract, or if the Create detail from draw request master (contract detail) file checkbox was not selected, enter the billing item for this line. Standard items may be selected from those previously set up in Set Up Standard Fixed Billing Items, new standard items may be added through the Billing Item Code window, or non-standard items may be typed directly into this field. Entry in this field is required. A lookup window is available for viewing valid billing items.
Note: A note about use of numeric coding: Because many users prefer alphabetic or combination alpha and numeric coding, this code is not a numeric-only field. Because of this, the code left-justifies when entered. Users preferring a strictly numeric coding should be advised to use leading zeros when adding codes in order to produce desired sort results on screens and reports. Without leading zeros, "1", "10", "100" will appear before "2", "20", "200". Instead, codes should be set up "001", "002", and so forth. If more than 1000 codes are anticipated, instead enter "0001", "0002", and so forth.

Item description
The description associated with the selected item number automatically displays. Press Enter to accept the software default or manually enter a new description. The description entered here will be saved by the software for use in subsequent bills for this contract.
Use the Add'l description field to enter additional description details.

Taxable?
During initial creation of a draw request, select this checkbox if the component is taxable, or leave the checkbox clear if it is not taxable. On subsequent draw requests generated by the software, this will be a display-only field and may not be changed.

Um
During initial creation of a draw request, enter the unit of measure for the component. For example, road paving might be measured per mile; shrubs for landscaping might be measured per each. It is also possible to enter components with a lump sum cost. In this case, enter LS in the unit-of-measure field (LS = lump sum). On subsequent draw requests generated by the software, this will be a display-only field and may not be changed.
If the unit of measure has a price method of 'fixed price', the Unit price and Contract quantity fields will be blank.

Unit price
Enter the unit price for the item. For example, price per mile of road, or price per shrub. If the unit-of-measure is Lump Sum, then this field will be skipped.

Contract quantity
If the item's unit-of-measure is Lump Sum, the total contract price for this item displays. If the item has a different unit-of-measure, the number of units specified on the contract displays.

This period quantity
Enter the quantity of the selected item for this period. Press F4 or double-click on this field to view the item's pre-billing quantity history.

JTD quantity
The total number of units (or dollar amount against a lump sum) completed to-date for the job display.

Contract $
The contract amount for the item for this line displays. If the item's unit of measure is Lump Sum, enter the dollar amount to be billed on this draw request or press Enter to accept the default based on the current period percent complete.
The Period amount and Job-to-date amount display to the right of this column.

Override retention?
Select this checkbox to record a job-to-date retention override, and then enter a Retention % and Retention amount for this item.
If you select this checkbox, the percent or amount of retention you enter for this line item will override the summary retention amount or percentage. For example, you might select this checkbox if the contract has a 10% retention rate, but a change order for the contract has a zero retention rate. For that change order, enter the line item details, select this checkbox, and enter 0 (zero) in the Retention % field. The percentage entered in this field will override the summary retention figure.

G/L account
Enter the General Ledger sales account number for this billing item. A lookup window is available for viewing valid General Ledger account codes. If the G/L status code you select has a status of Not used, you cannot proceed using this code. If the G/L status code you select has a status of Inactive, a warning will display.
