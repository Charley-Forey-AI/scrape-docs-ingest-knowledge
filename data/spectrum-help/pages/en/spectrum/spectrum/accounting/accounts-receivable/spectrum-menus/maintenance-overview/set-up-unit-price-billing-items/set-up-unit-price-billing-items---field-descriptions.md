---
title: "Set Up Unit Price Billing Items - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/set-up-unit-price-billing-items/set-up-unit-price-billing-items---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/set-up-unit-price-billing-items/set-up-unit-price-billing-items---field-descriptions"
---

# Set Up Unit Price Billing Items - Field Descriptions

Use this table for reference when completing the fields on this screen.
Field
Description

Customer code
Enter a customer code for customer special pricing. This field may be left blank for standard items. If the customer's status is set to Not used, no entry is allowed.
During unit price Contracts and Draw Request Billing Entry, the software will look to this file and default the description, additional description, unit of measure, and price when adding new entries.

Job
This field is only available if a customer code is entered above, and allows for pre-defining billing items for specific contracts. If this field is left blank, then the pricing will be for the particular customer entered.
Enter a job number, if desired, when designating the standard billing items. The lookup window available at this prompt will show only those jobs that are already set up as A/R contracts.
If both the customer and job are entered, the software will validate this combination against the Contracts screen.

Billing item
Enter a billing item code.
A note about use of numeric coding: Because many users prefer alphabetic or combination alpha and numeric coding, this code is not a numeric-only field. Because of this, the code left-justifies when entered. Users preferring a strictly numeric coding should be advised to use leading zeros when adding codes in order to produce desired sort results on screens and reports. Without leading zeros, "1", "10", "100" will appear before "2", "20", "200". Instead, codes should be set up "001", "002", and so forth. If more than 1000 codes are anticipated, instead enter "0001", "0002", and so forth.

Description
Enter a default billing item code description.

Um
Enter a unit of measure for this item (a lookup window is available at this prompt to view valid units of measure).

Unit price
Enter the default unit price for this billing item.

Additional description
Enter an additional description for the billing item in this field.

G/L account
Enter a G/L account code for the billing item. The Account description will display in the field to the right.
