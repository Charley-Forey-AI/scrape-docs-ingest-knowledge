---
title: "How does Spectrum price material on Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/in-depth-overview/how-does-spectrum-price-material-on-work-orders"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/in-depth-overview/how-does-spectrum-price-material-on-work-orders"
---

# How does Spectrum price material on Work Orders

Spectrum uses a variety of options to set the price of material on work orders.
How does Spectrum set the price of material on a work order?
The software identifies whether this is a stock item or not. Then it applies the following rules:

- If it is a stock item, the lowest price among a set of pricing tables is used. Many of these pricing tables can be date driven, so your pricing is automatically updated. The pricing tables include the price table on the item, customer special pricing, promotional pricing, and quantity break tables.

- If it is a non-stock item, the software first looks to see if there are any non-stock markup rules that apply. These can also be date driven. When calculating the non-stock price, the software marks up the cost, including any sales and use tax.

The Item Price Inquiry window indicates how the price was determined.
What is the Item Price Inquiry Screen?
The Item Price Inquiry window is available throughout the Work Order module. It shows the price calculations for the various pricing methods, as well as current warehouse quantity information. While this inquiry screen is located in Work Order > Inquiry > Item Price, you will use it more often while in a work order. You can access the Item Price Inquiry window by selecting the lookup icon next to the Unit price field on the Edit Material window.
Understanding the Pricing Methods
The Item Price Inquiry screen explains how the price of material was calculated. As many of the pricing tables are date driven, changing the Effective Date field will change the resulting price for the item.
The screen has sections that display the quantity available, on hand, committed and on order by warehouse. It also displays a section for the item's standard price table. If quantity breaks are offered, the middle section explains the pricing at different quantity levels. Special pricing is where any customer special pricing is stored. Promotional pricing is based on established discounts. If this was a non-stock item, you would see the marked up sales price as well.
Setting up the Pricing Methods
The following explains how to set up the various pricing methods available in the Work Order module.

## Item Price Table

This is set up on the Item Main Properties screen. Use the Sell section of this screen to assign up to five prices to each item. Customers are assigned a price level (1-5) on the Customer Defaults screen.

## Promotional Pricing

Use Inventory Control's Discounts screen to maintain discount codes to be used for promotional discount pricing. An example might be "Monthly Specials." The discount is calculated from the price table (1-5). Discounts are date-sensitive so the software will ignore the discount code after the effective date range has passed. You can also set up future-dated promotional pricing as well. Once this discount code is created, enter it on the  Inventory Items screen.
You must have Inventory Control on your system to take advantage of promotional pricing.

## Quantity Breaks

The Quantity Breaks screen in Inventory Control is used to establish and maintain quantity discounts. Quantity discounts may be offered on an item-by-item basis or for categories as a whole. The item quantity discounts may be a percentage discount or a specified price at each level of quantity break. A date range for the quantity discount is provided.
This method requires the Inventory Control module.

## Special Pricing

The Inventory Control > Customer Special Pricing screen is used to establish and maintain special pricing allowances for favored customers. The special pricing applies only to individual customer records maintained in this file. Special discounts may be established on an item-by-item basis or for categories as a whole. A date range for the special pricing is also provided. The item special pricing may be a percentage discount, a price table level code, or a specific designated amount. Category special pricing may only be entered as a price table level code or a percentage discount.
This method requires the Inventory Control module.

## Non-Stock Markups

Non-stock items can be marked up using the Work Order > Non-Stock Markup screen. Use this to mark up purchased items not included in your inventory (non-stock parts). This new feature provides the ability to set up and maintain a list of markup tables for non-stock parts as well as provide the ability to define cost basis break levels.
When adding a new work order, the following hierarchy is used to determine the non-stock markup percentage:

1. Service Contract


1. Work Order Site


1. Accounts Receivable Customer


1. Work Order Installation Screen


1. User-entered or Changed
 Markups accept values up to $99 million, and can be zero or even negative values, if desired.

## Controls

It is recommended that all special pricing rules be reviewed on a regular basis to determine whether such pricing should be continued or suspended. Some companies find this is useful on an annual basis, perhaps during a slow period of the year.

## Automation

Many of the pricing tables have effective date ranges. It is recommended that you schedule price increases rather than waiting until the new pricing becomes effective. The system uses the transaction date to determine which effective price to use.
Pricing tables with effective date ranges include:

- Customer Special Pricing

- Promotional Pricing

- Quantity Breaks

- Non-stock Markups

The only table that is not date-sensitive is the price table (1-5) for the specific item.
