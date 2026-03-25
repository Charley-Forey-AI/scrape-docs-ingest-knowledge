---
title: "Due Dates, Discount Dates, & Cutoff Dates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/payment-terms-setup/due-dates-discount-dates--cutoff-dates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/payment-terms-setup/due-dates-discount-dates--cutoff-dates"
---

# Due Dates, Discount Dates, & Cutoff Dates

When setting up payment terms, you must specify how the system calculates due dates and discount dates.
You can specify the number of days past the invoice date by which to calculate discount and due dates, or you can specify a set date each month.
If you specify the 'number of days' for discount date/due date calculations, the system will add the number of days to the invoice date to determine the discount date and due date.
For example:
Days Until Discount:15
Days Until Due:30
Inv Date Disc Date Due Date
02/10/09 02/25/09 03/12/09
03/10/09 03/25/09 04/09/09
04/10/09 04/25/09 05/10/09
If you specify a set day for due dates and discount dates, indicate which day of the month invoices are due or discounts can be taken. With this method, you must designate a 'cutoff day' and specify how the system determines the month in which the due date and/or discount date will fall.
The # Months to Roll Ahead After Cutoff Day drop-down determines whether to roll the discount/due dates 1, 2, or 3 months ahead of the cutoff day when the invoice date falls after the cutoff day. Based on the number of months specified, the discount and due dates calculate as follows (blue represents ‘before’ cutoff day, green represents ‘after’ cutoff day):
Due Day: 30
Discount Day: 10
Cutoff Day: 20

Roll Ahead Mths
Inv Date
Disc Date
Due Date

1
02/05/09
02/10/09
02/28/09

02/21/09
03/10/09
03/30/09

2
02/05/09
03/10/09
03/30/09

02/21/09
04/10/09
04/30/09

3
02/05/09
04/10/09
04/30/09

02/21/09
05/10/09
05/30/09

Once you have defined the discount date and due date information for the payment terms, you can use the Check Date Defaults section to test discount and due date defaults for a specific invoice date. You can also review the Sample Defaults grid for a list of sample discount and due date defaults for invoices posted on each day of a month (in the current year). Note: You can override due dates and discount dates when posting invoices, regardless of the method

Related information

- [About the HQ Payment Terms Form](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form)
