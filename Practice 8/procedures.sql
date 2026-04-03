CREATE OR REPLACE PROCEDURE upsert_contact(p_first TEXT, p_last TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE phone = p_phone) THEN
        UPDATE phonebook
        SET first_name = p_first,
            last_name = p_last
        WHERE phone = p_phone;
    ELSE
        INSERT INTO phonebook(first_name, last_name, phone)
        VALUES (p_first, p_last, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_insert(first_names TEXT[], last_names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..array_length(first_names, 1) LOOP
        IF phones[i] ~ '^[0-9]{10,}$' THEN
            CALL upsert_contact(first_names[i], last_names[i], phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: % (% %)', phones[i], first_names[i], last_names[i];
        END IF;
    END LOOP;
END;
$$;

CREATE OR REPLACE PROCEDURE delete_contact(value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE first_name = value
       OR last_name = value
       OR phone = value;
END;
$$;