CREATE TABLE user 
(
    Username varchar(50) NOT NULL,
    Pass varchar(100) NOT NULL,
    Email varchar(100) NOT NULL,
    PRIMARY KEY (Username) 
);

ALTER TABLE `user` ADD UNIQUE INDEX `Email_UNIQUE` (`Email` ASC) VISIBLE;

-- with unique index on the email to ignore dups

CREATE TABLE numbers 
(
    TestNumber INT NOT NULL PRIMARY KEY
);
