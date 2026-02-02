CREATE TABLE dwh_retail_transactions (
    id SERIAL PRIMARY KEY,               
    customer_id INT NOT NULL,
    last_status VARCHAR(50),             
    pos_origin VARCHAR(100),
    pos_destination VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW(),  
    updated_at TIMESTAMP DEFAULT NOW(),  
    deleted_at TIMESTAMP                 
);
