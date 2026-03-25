---
title: "How the System Uses a Quote | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/quotes/how-the-system-uses-a-quote"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/quotes/how-the-system-uses-a-quote"
---

# How the System Uses a Quote

Once a quote is set up, the system will use the quote to determine pricing, payment discounts (customer sales only), and haul charges each time a ticket is posted in MS Ticket Entry for the specified customer, job, or inventory location.
Additionally, customer quotes are used by the system to aid in the creation of invoices. When posting tickets, the system automatically checks the quote files to see if a quote has been set up for that customer, job, or inventory company/location. If the ticket is posted to a customer, the quote level will determine how the quote files are searched. For example, if the ticket specifies a customer, customer job, and PO#, the system first checks to see if a quote exists for that customer/customer job/customer PO# combination. If not, then it checks to see if a quote exists for the customer/customer job, and if no quote found at that level, it checks for a quote at the customer level.
