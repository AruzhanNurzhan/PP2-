-- add phone
CREATE OR REPLACE PROCEDURE add_phone(p_name TEXT, p_phone TEXT, p_type TEXT)
LANGUAGE plpgsql AS $$
DECLARE cid INT;
BEGIN
    SELECT id INTO cid FROM contacts WHERE first_name = p_name LIMIT 1;

    IF cid IS NULL THEN
        RAISE EXCEPTION 'contact not found';
    END IF;

    INSERT INTO phones(contact_id, phone, type)
    VALUES (cid, p_phone, p_type);
END;
$$;

-- move group
CREATE OR REPLACE PROCEDURE move_to_group(p_name TEXT, p_group TEXT)
LANGUAGE plpgsql AS $$
DECLARE cid INT;
DECLARE gid INT;
BEGIN
    SELECT id INTO cid FROM contacts WHERE first_name = p_name LIMIT 1;

    INSERT INTO groups(name) VALUES (p_group)
    ON CONFLICT DO NOTHING;

    SELECT id INTO gid FROM groups WHERE name = p_group;

    UPDATE contacts SET group_id = gid WHERE id = cid;
END;
$$;

-- extended search
CREATE OR REPLACE FUNCTION search_contacts(q TEXT)
RETURNS TABLE(id INT, first_name TEXT, last_name TEXT, email TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT c.id, c.first_name, c.last_name, c.email
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.first_name ILIKE '%'||q||'%'
       OR c.last_name ILIKE '%'||q||'%'
       OR c.email ILIKE '%'||q||'%'
       OR p.phone ILIKE '%'||q||'%';
END;
$$ LANGUAGE plpgsql;