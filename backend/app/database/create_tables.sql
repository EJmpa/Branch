-- create_tables.sql
-- SQL script for creating tables

-- Create the Messaging App Database
CREATE DATABASE IF NOT EXISTS messaging_app;
USE messaging_app;

-- Create the Customers Table
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    customer_name TEXT NOT NULL,
    phone TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create the Agents Table
CREATE TABLE IF NOT EXISTS agents (
    agent_id INTEGER PRIMARY KEY,
    agent_name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create the Messages Table
CREATE TABLE IF NOT EXISTS messages (
    message_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    agent_id INTEGER,
    content TEXT NOT NULL,
    sent_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
    FOREIGN KEY (agent_id) REFERENCES agents (agent_id)
);
