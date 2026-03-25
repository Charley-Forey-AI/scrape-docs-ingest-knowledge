---
title: "Field Definitions: SM Work Order to New Quote Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-to-new-quote-form/field-definitions-sm-work-order-to-new-quote-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-order-to-new-quote-form/field-definitions-sm-work-order-to-new-quote-form"
---

# Field Definitions: SM Work Order to New Quote Form

The following is a list of field descriptions for the SM Work
 Order to New Quote form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Quote ID

Quote ID field on the SM Work Order to New Quote form.
 Enter
 a quote ID or enter N, New, or
 + to have the system
 automatically assign the next sequential quote number.

Related information

- [Create a Quote from a Work Order](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote/create-a-quote-from-a-work-order)

- [Enter an SM Work Order Quote](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote)

- [SM Work Order Quotes Form](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form)

## Create New Work Order

Include checkbox on the SM Work Order to New Quote form.

##  Description

Description field on the SM Work Order to New Quote form.
Enter a description for the quote. This field appears when the New Work Order  checkbox has not been selected.

Related information

- [Create a Quote from a Work Order](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote/create-a-quote-from-a-work-order)

- [SM Work Order Quotes Form](/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form)

- [Enter an SM Work Order Quote](/en/vista/vista/service-management/work-order-quotes/enter-an-sm-work-order-quote)

## Include

Include checkbox on the SM Work Order to New Quote form.

Select this checkbox to include a scope of work into a quote. Appears when the  New Work Order checkbox has not been selected.

## Scope

Scope field on the SM Work Order to New Quote form.
Enter the work scope that represents the work to be done on this work order sequence. Press F4 for a list of valid work scopes. This field appears when the New Work Order checkbox has not been selected.

## Description

Description field on the SM Work Order to New Quote form.
Enter a description for the quote. This field appears when the New Work Order checkbox has not been selected.

## Price Method

Price Method drop-down list on the SM Work Order to New Quote form.
This field appears when the New Work Order checkbox has not been selected.

Select the price method for this quote sequence:

- F-Flat Price - Select this option if the work covered by this quote sequence will be included in the flat amount specified in the  Price field (to the right).

- T-Time and Material  - Select this option if the work covered by this quote sequence will be billed using the rate template specified in the Rate Template field below.

- D-Derived Flat Price  - Select this option if you want the work covered by this quote sequence to calculate the flat price based on equipment, labor, misc and material entries using the rate template. Upon approval, this type of quote sequence becomes a flat-price work order.

## Rate Template

Rate Template field on the SM Work Order to New Quote form.

This field appears when the New Work Order checkbox has not been selected.

Enter the rate template for this quote sequence. Press F4 for a list of valid rate templates.

The rate template defaults from the service site. If the rate is not defined in the service site, it defaults from SM Customers; if the rate is not defined in SM Customers, this field is blank.

The rate template specified here will be used to determine equipment, labor, and material rates for work completed on work orders generated from this work order quote.

## Price

New Work Order checkbox on the SM Work Order to New Quote form.
This field appears when the New Work Order checkbox has not been selected.

For Flat Price scopes only, enter the price that will be charged for the work covered by this quote sequence.

For Derived Flat Price scopes, this field is disabled and defaults a value based on required equipment, labor, misc and material entries.

Enter the price that will be charged for the work covered by this quote sequence.

When a work order is generated from this quote, all work completed lines associated with this sequence will have a Pricing Method of No Charge; the Billable Rate and Total Billable fields will be blank and cannot be changed.
