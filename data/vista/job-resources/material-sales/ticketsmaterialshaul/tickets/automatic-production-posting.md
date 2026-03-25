---
title: "Automatic Production Posting | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/automatic-production-posting"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/automatic-production-posting"
---

# Automatic Production Posting

Automatic production posting in Material Sales allows you to have the system automatically update on-hand quantities of finished goods and raw materials each time a finished good is sold and posted in MS Ticket Entry.
This feature is most commonly used by companies who cannot store their finished goods, such as asphalt or concrete producers. Automatic production posting can only occur if:

- your company produces finished goods (such as asphalt) and stores the raw materials at one of its inventory locations.

- you have set up mix designs for production of the finished goods in IN Bill Of Materials or IN Bill of Materials Override.

- you have selected the Auto
 Production checkbox in IN Location Materials for the selected
 finished goods.

If these criteria are met, each time you post the finished good material to a ticket in MS Ticket Entry, the system automatically:

- reduces the on-hand quantities of each of the raw materials used in the production of the finished good based on the mix design (Bill of Materials) for the finished good. The system will first check to see if a Bill of Materials exists at the location level (IN Bill of Materials Override), and if so, uses it to produce the finished good and relieve Inventory. If no override Bill of Materials exists, the standard Bill of Materials for the location group is used.

If you have selected the Update Average Cost of
 Material with Sum of Component Costs checkbox for the finished good in
 IN Location Materials and the production location has a Cost Method of Average Cost, the
 system will also update the average cost of the finished good based on the sum of the
 component costs.

- adds the finished good to inventory.

- posts the sale of the finished good and relieves the finished good from inventory.

Note: The system always uses the current mix design; therefore, it you frequently change mix designs, Auto Production may not be suitable.
Because production can also be posted manually in IN Production Entry, it is important that you decide which finished goods you will post manually and which finished goods you will have the system post automatically. Materials flagged for automatic production posting should not be posted manually. The system automatically relieves the appropriate raw materials at the time the finished good is sold. Posting production manually would only duplicate the production process.

## General Ledger Implications

With production posting, the general
 ledger implications are a bit more complicated. Because there are typically multiple
 raw materials used to produce a finished good, the system must make a GL entry to
 the Inventory account for each raw material used.
The level of interface to Inventory for
 entries related to auto production is defined by company in MS Company Parameters.
 Interface levels are: None, Summary, or Detail. If you elect to update at the
 Summary level, production entries will be combined by Location, Material, and IN
 Trans Type. If interfaced at the Detail level, each ticket will generate its own set
 of transactions in IN Inventory Detail. No sales, use, or value added tax (VAT) is
 included with auto production entries.
Auto production occurs at the ticket’s
 ‘selling’ Location. If a Bill of Material exists for the finished material at the
 ‘selling’ (as defined in IN Bill of Materials Override), its components, their
 source location, and quantity will be used. If no override exists, the material’s
 standard Bill of Materials (based on location group) will be used, and its
 components will be assumed to exist at the production location (i.e. no transfer or
 sale needed).
Note: For information on how the system handles
 components of a finished good that come from locations different from the
 sales/production location, see “Using Components from Multiple Locations” in Related
 Topics below.
The amounts posted to each of the
 accounts specified above (except for the Production Qty) are based on the sales
 location, the material, and the cost method (which determines how costs are
 calculated to relieve inventory). The cost method is specified at the company level
 (IN Company Parameters), but can be overridden at the location level (IN Locations)
 or the category level (IN Location Category Override).
For example, if the cost method is
 Average Cost, the Cost of Production and Inventory accounts will be credited/debited
 based on the Average Unit Cost specified for each component material in IN Location
 Materials and the number of units of each material that was used in the production
 of the finished good (determined by the Bill of Materials).
The amounts posted to the Inventory and
 Value of Production accounts will be credited/debited based on the Average Unit Cost
 of the finished good material and the total number of units produced of the finished
 good. This will typically result in the posted amounts differing from those posted
 to the Cost of Production and Inventory accounts for the components.
Note: You must maintain the ‘costs’ of your finished
 goods. These costs should reflect the sum of component costs plus any additional
 production-related costs such as labor and equipment. Changes to the mix design or
 the costs of the components are not reflected in the debit made to Inventory for
 production of a finished good.
