---
title: "Customer Sales | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/customer-sales"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/ticket-entry/customer-sales"
---

# Customer Sales

This type of transaction is used to post sales of materials to
 a customer.
When entering tickets (MS Ticket Entry), you have the option to specify the customer, customer job, and/or customer PO number. The values you enter are important if you have previously set up quotes for the selected customer. Quotes are generally used to define special pricing on materials, as well as overrides to discounts, haul rates, and pay rates. They can be set up at the customer, customer job, and/or customer PO levels; therefore, how you post a ticket for that customer will determine how the system determines which quote to use for pricing, discounts, and haul information. For example, if you have defined special pricing information at the customer PO# level, then you must specify the purchase order number on the ticket to ensure the appropriate quote will be used. Otherwise, the system will locate the quote that is closest to the information provided and use it for prices, etc.
If no quote exists, the system uses the pricing
 template assigned to the customer in AR Customers. If no pricing template is assigned,
 or no entry within the price template exists for the material, the Pricing Option for
 Customer sales (IN Company) is used, along with the markup/discount rates assigned in AR
 Customers. If there is no markup/discount rate specified for the customer in AR
 Customers, the Markup/Discount Rate for Customers in IN Location Materials is used.
 These options are then applied to the standard prices in IN Location Materials (if the
 material is stocked) or HQ Materials (if the material is non-stocked).
When a ticket or hauler time sheet is entered, its payment discount will be calculated based on the payment terms assigned to the Customer. If the payment terms are 'rate based', discounts will be calculated using the rate specified in HQ Payment Terms. If a customer’s payment terms are 'material based' (Discount Based on Material option checked in HQ Payment Terms), the system will perform a hierarchical search to determine what discount rate/amount to use. See Discounts in Related Topics below for more information.
Once you have posted a batch of customer sales tickets, the detail is then stored in the Material Sales Ticket Detail table where it can later be accessed to create invoices (MS Invoice Edit). Once the invoices have been created, edited, and printed, they are interfaced to Accounts Receivable.
Note: It is important to remember that once you have interfaced an invoice to AR, it can no longer be edited. Make sure all changes and corrections have been made prior to interfacing. If you should need to correct an invoice that has already been interfaced, a correcting entry can be made. See Correcting Invoiced Transactions in Related Topics below for instructions on how to implement this process.
You also have the option to void an invoice, which
 reopens the transaction and makes it available for payment. Once a transaction is
 reopened, it can be edited as necessary.

## General Ledger Implications

Each time you post a sale to a customer,
 entries are made to the appropriate accounts in General Ledger for the “sell from”
 company. The Cost of Goods and Accounts Receivable accounts are debited as follows:

- If an override Cost of Goods
 account is specified for the “selling” location in IN Location Category
 Override, it will be used. Otherwise, the system will use the Cost of Goods
 account specified in IN Locations.

- The Accounts Receivable account
 used is determined by the transaction’s receivable type. Receivable types
 may be defined at the location/category, location, and customer levels (i.e.
 IN Location Category Override, IN Locations, and AR Customers). When
 determining which receivable type to use, the system first checks at the
 location/category level. If no value is found at the location/category
 level, it then checks at the location level, and finally, at the customer
 level.

The Accts Rec account will be debited
 for all charges on the transaction. Tax amounts are credited to the GL Account
 specified for the tax code in HQ Tax Codes and haul amounts are updated to the
 “selling” location’s haul revenue account. The haul revenue and customer sales
 accounts can be assigned by location, with overrides by location/category. The
 following diagram illustrates the General Ledger updates that occur when 'sales to
 customers' transactions are posted.
* Revenue is not recognized until
 invoiced
