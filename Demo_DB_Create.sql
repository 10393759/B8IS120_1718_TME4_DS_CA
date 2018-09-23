#Create DB & Table
CREATE DATABASE booking;
USE booking;
CREATE TABLE bookings (seatID INT NOT NULL AUTO_INCREMENT,seatName VARCHAR(255),
seatBooked TINYINT(1) not null default 0, bookedBy VARCHAR(255),PRIMARY KEY(seatID));