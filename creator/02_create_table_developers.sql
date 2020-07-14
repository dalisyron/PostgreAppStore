create table "Developers" (
    id bigint not null,
    username varchar(20) not null,
    first_name varchar(20),
    last_name varchar(20),
    email varchar(40) not null,
    birthdate date,
    primary key(id)
);
