CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(first_name TEXT, last_name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.first_name::TEXT, pb.last_name::TEXT, pb.phone::TEXT
    FROM phonebook pb
    WHERE pb.first_name ILIKE '%' || pattern || '%'
       OR pb.last_name ILIKE '%' || pattern || '%'
       OR pb.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_contacts_paginated(lim INT, off INT)
RETURNS TABLE(first_name TEXT, last_name TEXT, phone TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.first_name::TEXT, pb.last_name::TEXT, pb.phone::TEXT
    FROM phonebook pb
    ORDER BY pb.first_name
    LIMIT lim OFFSET off;
END;
$$ LANGUAGE plpgsql;