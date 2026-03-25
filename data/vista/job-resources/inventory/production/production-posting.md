---
title: "Production Posting | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/production/production-posting"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/production/production-posting"
---

# Production Posting

Overview of production posting of finished goods.
Once you have set up a bill of materials for each of
 the finished goods that your company produces, you can then post production of the
 finished goods using one of two methods:

- Manual Production Posting – Use [IN Production Entry ](/en/vista/vista/job-resources/inventory/production/about-the-in-production-entry-form) to manually post the
 production of a finished good. You specify the inventory location, the finished
 good material, and the quantity produced, and the system automatically relieves
 the raw materials from that location and updates the quantity on hand of the
 finished good for the same location.Note: You may post the
 production of several finished goods in a single batch, but all raw
 materials used in the production of the finished goods must be at the same
 location.

- Automatic Production Posting – This method is
 only used in the Material Sales module when the Auto
 Production box on the Info tab of the [IN Location Materials ](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form) form is checked. When
 this box is checked the system will automatically relieve the appropriate raw
 materials from inventory (using the bill of materials) when the finished good is
 sold from Material Sales. Auto production works the same as manual production;
 it just eliminates having to post production manually. As with manual production
 posting, the system automatically relieves the raw materials directly from
 inventory and adds the finished good to inventory. But, because the production
 is posted at the same time the sale is posted, it also immediately relieves the
 inventory of the finished good.Note: Although auto
 production can be used for any finished good, it is typically most useful
 for finished goods such as asphalt or concrete. Because you cannot store
 these types of finished goods, auto production allows you to implement
 production posting when the finished good is sold.

With production posting, the general ledger
 implications are a bit more complicated. Because there are typically multiple raw
 materials used to produce a finished good, the system must make a GL entry to the
 Inventory account for each raw material used. GL entries are summarized by account.
 Inventory accounts are set up by location and can be overridden by material category
 ([IN Location Category Override](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-category-override-form)). Regardless of how you
 set up your accounts, only one entry is made for each account affected when posting a
 production batch.
 Note that the GL entry amounts for Cost of
 Production and Inventory (Raw Materials) are different than the GL entry amounts for
 Inventory (Finished Good) and Value of Production. This is because the cost of the
 finished good (as maintained in [IN Location Materials](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form)) is used, not the total cost of
 the raw materials. You control this cost and can set it to include other costs of
 production.
