---
title: "Field Definitions: EM Revenue Rate Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rate-update-form/field-definitions-em-revenue-rate-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rate-update-form/field-definitions-em-revenue-rate-update-form"
---

# Field Definitions: EM Revenue Rate Update Form

The following is a list of field descriptions for the EM
 Revenue Rate Update form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Beginning/Ending Category

 Specify the beginning and ending category in a range of equipment categories for filtering, or leave blank to include all categories. Initially defaults as follows:

- If you accessed this form from EM Revenue Rates by Category, defaults the selected category.

- If you accessed this form from EM Revenue Rates by Equipment, defaults the category of the selected equipment.

##  Beginning/Ending Rev Code

 Specify the beginning and ending revenue code in a range of revenue codes for filtering, or leave blank to include all revenue codes. Initially defaults the revenue code selected in EM Revenue Rates by Category or EM Revenue Rates by Equipment.

## Rev Breakdown Code

Required.
Specify the revenue breakdown code for filtering and for which you are changing rates. Initially defaults the revenue breakdown code selected in EM Revenue Rates by Category or EM Revenue Rates by Equipment (on Rev Breakdown tab). If no specific breakdown code selected, defaults the revenue breakdown code specified in EM Company Parameters (Usage tab).

##  Rev Breakdown Rate

 Specify the revenue rate for filtering. Only revenue codes with the specified revenue breakdown code and rate combination will display in the grid.

##  Bdown Rate Type

 Specify the breakdown rate type.

- B – Both. Select this option to change revenue rates by category and equipment. The system will populate both the EM Revenue Rates by Category and EM Revenue Rates by Equipment grids based on selection criteria.

- C – Breakdown Rate by Category. Select this option to change revenue rates by category only. The system will populate the EM Revenue Rates by Category grid only, based on selection criteria.

- E – Breakdown Rate by Equipment. Select this option to change revenue rates by equipment only. The system will populate the EM Revenue Rates by Equipment grid only, based on selection criteria.

##  Update

 Check this box to update this category or equipment with the new revenue rate for the specified breakdown code. The system automatically checks this box for all categories and/or equipment meeting the selection criteria.
 Uncheck this box if you do not want the category or equipment updated with the revenue rate change.

##  Change Rate By

 Specify the method for updating the revenue rate for the selected breakdown code.

- A-Amount – Select this option to increase or decrease the rate for the selected revenue breakdown code by a specified amount. For example, if existing rate is 55.00 and you enter '10.00', rate will increase to 65.00. If you enter '-10.00', rate will decrease to 45.00.

- P-Percent – Select this option to increase or decrease the rate for the selected revenue breakdown code by a percentage. For example, if the existing rate is '55.00' and you enter 5.00%, rate will increase by 5% (to 57.75. If you enter '-5.00', rate will decrease by 5% (to 52.25).

- N-New Rate – Select this option to change the revenue rate for the specified revenue breakdown code to a fixed amount. For example, if you enter '25.00', all rate(s) will be changed to 25.00, regardless of their previous value.

##  Amount

 This field displays when the Change Rate By drop-down is set to ‘Amount’ or ‘New Rate’.
 If the rate change method is ‘Amount’, enter the amount by which to increase or decrease the rate for the specified revenue breakdown code. Enter as a positive amount to increase the rate or negative amount to decrease the rate.
 If the rate change method is ‘New Rate’, enter the new rate. All rates will be changed to this amount, regardless of their previous value.

##  Percent

 This field displays when Change Rate By drop-down is set to ‘Percentage’.
 Enter the percentage by which to increase or decrease the rate for the specified revenue breakdown code. Enter as a positive amount to increase the rate or a negative amount to decrease the rate.
