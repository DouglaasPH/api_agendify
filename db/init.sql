-- CUSTOMER 
CREATE TYPE customer_status AS ENUM ('active', 'deleted');

CREATE TABLE customer (
    id SERIAL PRIMARY KEY NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    status customer_status DEFAULT 'active'
);

CREATE UNIQUE INDEX unique_active_customer_email
ON customer (email)
WHERE status = 'active';


--PROFESSIONAL
CREATE TYPE professional_status AS ENUM ('active', 'deleted');

CREATE TABLE professional (
    id SERIAL PRIMARY KEY,
    profile_avatar_id INTEGER NOT NULL,
    name VARCHAR(150) NOT NULL,
    hashed_password VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL,
    profession VARCHAR(150) NOT NULL,
    phone_number VARCHAR(150) NOT NULL,
    chat_code VARCHAR(150) NOT NULL,
    status professional_status NOT NULL DEFAULT 'active'
);

CREATE UNIQUE INDEX unique_active_professional_email
ON professional (email)
WHERE status = 'active';


-- REFRESH TOKEN
CREATE TABLE refresh_token (
    id SERIAL PRIMARY KEY,
    professional_id INTEGER NOT NULL,
    token VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE,
    is_revoked BOOLEAN NOT NULL DEFAULT FALSE,
    CONSTRAINT fk_refresh_token_professional
        FOREIGN KEY (professional_id)
        REFERENCES professional(id)
        ON DELETE CASCADE
);




-- AVAILABILITY
CREATE TYPE availability_status AS ENUM ('available', 'occupied', 'canceled', 'past', 'deleted');

CREATE TABLE availability (
    id SERIAL PRIMARY KEY,
    professional_id INTEGER NOT NULL,
    date DATE DEFAULT CURRENT_DATE,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    slot_duration_minutes INTEGER NOT NULL,
    status availability_status DEFAULT 'available',
    CONSTRAINT fk_availability_professional
        FOREIGN KEY (professional_id)
        REFERENCES professional(id)
        ON DELETE CASCADE,
    CONSTRAINT chk_time CHECK (end_time > start_time)
);


-- APPOINTMENT
CREATE TYPE appointment_status AS ENUM ('confirmed', 'canceled', 'past', 'deleted');

CREATE TABLE appointment (
    id SERIAL PRIMARY KEY,
    professional_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    availability_id INTEGER NOT NULL,
    status appointment_status DEFAULT 'confirmed',
    CONSTRAINT fk_appointment_availability
        FOREIGN KEY (availability_id)
        REFERENCES availability(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_appointment_customer
        FOREIGN KEY (customer_id)
        REFERENCES customer(id)
        ON DELETE CASCADE
);
