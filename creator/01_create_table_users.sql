create table "Users" (
    id bigint not null, --not necessarily 8 digits
    username varchar(20) not null,
    first_name varchar(20),
    last_name varchar(20),
    email varchar(40) not null,
    phone_number char(10) not null,
    primary key(id)
);
