-- SQLite
-- ✅ 1. Select specific columns

-- ✅ 2. Create new database structure
-- CREATE TABLE owners(
--     id INTEGER PRIMARY KEY,
--     name TEXT,
--     email TEXT,
--     phone TEXT
-- );
-- ✅ 2a. Remove owners table
-- DROP TABLE IF EXISTS owners;
-- ✅ 2b. Create owners table
CREATE TABLE owners(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT
);
-- ✅ 2c. Create pets table
CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    breed TEXT,
    owner_id INTEGER,
        FOREIGN KEY(owner_id) REFERENCES owners(id)
)
CREATE TABLE procedures(
    id INTEGER PRIMARY KEY,
    name TEXT
);
CREATE TABLE appointments(
    id INTEGER PRIMARY KEY,
    staff TEXT,
    pet_id INTEGER,
    procedure_id INTEGER
)




-- ✅ 3. Modify pets table
-- ✅ 3a. Add image_url to pets
-- ALTER TABLE pets
-- ADD COLUMN image_url TEXT;
-- ✅ 3b. Rename column

-- ✅ 4. Create new instances
-- ✅ 4a. Use chatGPT to create random owners
-- ^ "given an sql table 'owners' with columns 'name' (text), 'address' (text), 'email' (text), 'phone' (text) create 5 instances with dummy data"
-- ✅ 4b. Use chat GPT to create sample data for pets
INSERT INTO owners (name, email, phone)
VALUES 
    ('John Doe', 'john.doe@example.com', '555-123-4567'),
    ('Jane Smith', 'jane.smith@example.com', '555-987-6543'),
    ('Robert Johnson', 'robert.j@example.com', '555-555-5555'),
    ('Alice Brown', 'alice.b@example.com', '555-321-7890'),
    ('David Lee', 'david.lee@example.com', '555-888-7777');
INSERT INTO pets (name, age, breed, owner_id)
VALUES 
    ('Fluffy', 3, 'Golden Retriever', 2),
    ('Whiskers', 2, 'Siamese', 3),
    ('Rex', 4, 'German Shepherd', 4),
    ('Mittens', 1, 'Calico', 5),
    ('Buddy', 2, 'Labrador Retriever', 1)
    ('Oreo', 5, 'Maine Coon', 2),
    ('Luna', 1, 'Poodle', 3),
    ('Max', 2, 'Bulldog', 4);

-- ✅ 5. Read data
-- ✅ 5a. Get all columns from pets
SELECT * FROM pets;
SELECT id, name, breed FROM pets;
-- ✅ 5b. Select pet by name
SELECT * FROM pets WHERE name = "Rex";
-- ✅ 5c. Select pets by favorite treats
-- ✅ 5d. Select pets by age 
SELECT * FROM pets WHERE age = 3;

-- ✅ 6. Update data
-- ✅ 6a. Update pet's age by name
UPDATE pets
SET age = 12
WHERE name = "Whiskers";
SELECT * FROM pets WHERE name = "Whiskers";

UPDATE pets
SET breed = "Old"
WHERE age > 5;

-- ✅ 6b. Update multiple pets' favorite_treats

-- ✅ 7. Delete data
DELETE FROM pets WHERE breed = "Old" OR age = 1; -- Goodnight, my sweet prince

-- ✅ 8. Join data 
-- ✅ 8a. One to many
SELECT *
FROM pets
JOIN owners
ON owner.id = pets.owner_id;

-- ✅ 8b. Many to many: create staff table 
-- ✅ 8c. Many to many: create appointments table
SELECT appointments.staff,
    appointments.pet_id,
    appointments.procedure_id,
    pets.name,
    appointments.procedure_id,
    procedures.name
FROM appointments
JOIN pets
    ON appointments.pet_id = pets.id
JOIN
    ON appointments.procedure_id = procedures.id;

SELECT pets.name, appointments.staff, procedures.name
FROM pets
JOIN appointments
    ON pets.id = appointments.pet_id
JOIN procedures
    ON appointments.procedure_id = procedures.id;

SELECT pets.name, appointments.staff
FROM pets
LEFT OUTER JOIN appointments ON pets.id = appointments.pet_id;
LEFT OUTER JOIN procedures ON appointments.procedure_id = procedures.id

-- ✅ 9. Seed data
-- ✅ 9a. Create two staff members using ChatGPT?
-- ✅ 9b. Create six appointments using ChatGPT

-- ✅ 10. Join tables
-- ✅ 10a. Basic join
-- ✅ 10b. Basic join with specific values

SELECT * FROM pets ORDER BY pets.age DESC LIMIT 5;