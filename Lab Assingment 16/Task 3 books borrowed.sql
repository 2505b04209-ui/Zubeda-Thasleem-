-- Library Management System - Task 1: Schema
-- Created with help of AI (Grok)

CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    join_date DATE
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    available BOOLEAN
);

CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    loan_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- To check tables were created
SHOW TABLES;

-- Inserting 3 Members
INSERT INTO Members (member_id, name, email, join_date) VALUES
(1, 'Rahul Sharma', 'rahul@gmail.com', '2024-01-15'),
(2, 'Priya Singh', 'priya@yahoo.com', '2024-03-22'),
(3, 'Aman Verma', 'aman@hotmail.com', '2024-06-10');

-- Inserting 3 Books
INSERT INTO Books (book_id, title, author, available) VALUES
(101, 'The Great Gatsby', 'F. Scott Fitzgerald', TRUE),
(102, '1984', 'George Orwell', TRUE),
(103, 'To Kill a Mockingbird', 'Harper Lee', FALSE);

-- Inserting 3 Loans (who borrowed what)
INSERT INTO Loans (loan_id, member_id, book_id, loan_date, return_date) VALUES
(1, 1, 101, '2025-01-05', NULL),        -- Rahul borrowed Gatsby (not returned)
(2, 2, 103, '2025-02-10', '2025-02-25'),-- Priya borrowed Mockingbird (returned)
(3, 1, 102, '2025-03-01', NULL);        -- Rahul borrowed 1984 (not returned)

-- Task 3: List all books borrowed by Rahul Sharma (member_id = 1)

SELECT 
    m.name AS Member_Name,
    b.title AS Book_Title,
    b.author AS Author,
    l.loan_date AS Borrowed_On,
    l.return_date AS Returned_On
FROM 
    Members m
    JOIN Loans l ON m.member_id = l.member_id
    JOIN Books b ON l.book_id = b.book_id
WHERE 
    m.member_id = 1;
