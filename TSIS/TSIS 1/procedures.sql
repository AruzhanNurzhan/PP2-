DROP FUNCTION IF EXISTS search_contacts(text);
CREATE OR REPLACE FUNCTION search_contacts(q TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, last_name VARCHAR, email VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT 
        c.id, 
        c.first_name::VARCHAR, 
        c.last_name::VARCHAR, 
        c.email::VARCHAR
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.first_name ILIKE '%'||q||'%'
       OR c.last_name ILIKE '%'||q||'%'
       OR c.email ILIKE '%'||q||'%'
       OR p.phone ILIKE '%'||q||'%';
END; $$ LANGUAGE plpgsql;

DROP PROCEDURE IF EXISTS add_phone(text,text,text);
CREATE OR REPLACE PROCEDURE add_phone(p_name TEXT, p_phone TEXT, p_type TEXT)
LANGUAGE plpgsql AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid FROM contacts WHERE first_name ILIKE '%'||p_name||'%' LIMIT 1;
    IF cid IS NULL THEN RAISE EXCEPTION 'Contact not found'; END IF;
    INSERT INTO phones(contact_id, phone, type) VALUES (cid, p_phone, p_type);
END; $$;