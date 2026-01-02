# Regex templates for common invoice fields

PDF_TEMPLATE_FIELDS = {
    # Matches "Invoice No: 12345"
    "invoice_number": r"Invoice\s+No\.?:\s*(\S+)",
    
    # Matches "Date: 2023-10-27"
    "invoice_date": r"Date:\s*(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})",
    
    # Matches "Customer: John Doe" - simplified greedy match
    "customer_name": r"Customer:\s*(.+)",
    
    # Matches "Total: $500.00" or "Total: 500.00"
    "total_amount": r"Total:\s*\$?\s*([\d,]+\.\d{2})",
}
