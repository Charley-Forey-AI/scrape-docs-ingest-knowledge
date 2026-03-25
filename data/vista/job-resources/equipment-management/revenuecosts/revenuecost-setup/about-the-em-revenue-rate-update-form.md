---
title: "About the EM Revenue Rate Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rate-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rate-update-form"
---

# About the EM Revenue Rate Update Form

Use this form to update the revenue rates for a category or equipment by changing the revenue rate for a selected revenue breakdown code.
Access this form from EM Revenue Rates by Category or EM Revenue Rates by Equipment by selecting File > EM Revenue Rate Update.
Upon entry to this form, the system automatically places focus on the tab related to the parent form (e.g. if you accessed this form via EM Revenue Rates by Category, focus will be on the EM Revenue Rates by Category tab). The selection criteria defaults based on the category or equipment, revenue code, and revenue breakdown code selected when you accessed this form, and the system automatically populates the category or equipment grid based on the default criteria.
The Bdown Rate Type field determines whether you are updating the revenue rate for breakdown codes by category, by equipment, or for both category and equipment. The option you selected controls which grid is populated and initially defaults based on the parent form. You can change the criteria as necessary and then click the Refresh button to repopulate the grid(s).
Note: The system only populates the grids with categories/equipment having the Override Rate flag checked in EM Revenue Rates by Category or EM Revenue Rates by Equipment. In addition, it automatically sets the Update flag to Yes (checked) for each record. If you are updating equipment rates, uncheck the box for any equipment you do not want updated.
Once you populate the grid with the desired category and/or equipment, use the Update Options section to specify the type of rate change:

- Amount – Increases or decreases the rate for the specified revenue breakdown code by a specified amount. For example, if existing rate is 55.00 and you enter '10.00', rate will increase to 65.00. If you enter '-10.00', rate will decrease to 45.00.

- Percent – Increases or decreases the existing rate(s) by a percentage. For example, if the existing rate is '55.00' and you enter 5.00%, rate will increase to 57.75 (55.00 x .05 + 55.00). If you enter '-5.00', rate will decrease to 52.25.

- New Rate - Changes the existing rates to a fixed amount. For example, if you enter '25.00', rate(s) will be changed to 25.00, regardless of their previous value.

When you are ready to update rates, click the Update button to initiate the rate update. The system updates the rate for the specified revenue breakdown code, which then updates the category and/or equipment rates. If multiple breakdown codes exist for the category or equipment, the system first updates the selected revenue breakdown code, then sums the amount of all breakdown codes and updates that amount to the category and/or equipment.

Related information

- [About the EM Revenue Rates by Category Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form)

- [About the EM Revenue Rates by Equipment Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form)
