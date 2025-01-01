-- Insert sample customers
INSERT INTO customers (name, email, phone, address, date_of_birth, ssn, credit_score, balance) VALUES
('John Smith', 'john.smith@email.com', '555-0123', '123 Main St, Anytown, ST 12345', '1985-06-15', '123-45-6789', 720, 1000.00),
('Sarah Johnson', 'sarah.j@email.com', '555-0124', '456 Oak Ave, Somewhere, ST 12346', '1990-03-22', '234-56-7890', 680, 2500.00),
('Michael Brown', 'mbrown@email.com', '555-0125', '789 Pine Rd, Elsewhere, ST 12347', '1978-11-30', '345-67-8901', 750, 5000.00);

-- Insert sample loans
INSERT INTO loans (customer_id, loan_type, amount, interest_rate, term_months, balance, status, origination_fee, disbursement_date, first_payment_date) VALUES
(1, 'PERSONAL', 10000.00, 8.50, 36, 10000.00, 'ACTIVE', 250.00, '2024-01-15', '2024-02-15'),
(2, 'AUTO', 25000.00, 6.75, 60, 25000.00, 'ACTIVE', 500.00, '2024-01-10', '2024-02-10'),
(3, 'HOME', 250000.00, 4.50, 360, 250000.00, 'ACTIVE', 2500.00, '2024-01-05', '2024-02-05');

-- Insert sample loan payments
INSERT INTO loan_payments (loan_id, amount, payment_type, principal_amount, interest_amount, payment_date, status) VALUES
(1, 315.00, 'SCHEDULED', 250.00, 65.00, '2024-02-15', 'COMPLETED'),
(2, 492.00, 'SCHEDULED', 375.00, 117.00, '2024-02-10', 'COMPLETED'),
(3, 1267.00, 'SCHEDULED', 642.00, 625.00, '2024-02-05', 'COMPLETED');

-- Insert sample payment schedule
INSERT INTO payment_schedule (loan_id, due_date, payment_amount, principal_amount, interest_amount, status) VALUES
(1, '2024-03-15', 315.00, 252.00, 63.00, 'PENDING'),
(1, '2024-04-15', 315.00, 254.00, 61.00, 'PENDING'),
(2, '2024-03-10', 492.00, 377.00, 115.00, 'PENDING'),
(2, '2024-04-10', 492.00, 379.00, 113.00, 'PENDING'),
(3, '2024-03-05', 1267.00, 644.00, 623.00, 'PENDING'),
(3, '2024-04-05', 1267.00, 646.00, 621.00, 'PENDING');

-- Insert sample loan documents
INSERT INTO loan_documents (loan_id, document_type, document_url, status) VALUES
(1, 'AGREEMENT', 'https://storage.example.com/docs/loan1/agreement.pdf', 'APPROVED'),
(1, 'ID_PROOF', 'https://storage.example.com/docs/loan1/id.pdf', 'APPROVED'),
(2, 'AGREEMENT', 'https://storage.example.com/docs/loan2/agreement.pdf', 'APPROVED'),
(2, 'VEHICLE_TITLE', 'https://storage.example.com/docs/loan2/title.pdf', 'APPROVED'),
(3, 'AGREEMENT', 'https://storage.example.com/docs/loan3/agreement.pdf', 'APPROVED'),
(3, 'PROPERTY_DEED', 'https://storage.example.com/docs/loan3/deed.pdf', 'APPROVED');
