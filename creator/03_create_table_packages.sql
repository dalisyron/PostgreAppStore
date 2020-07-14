create table "Packages" (
    id bigint not null,
    package_name varchar(60) not null,
    size integer not null,
    file varchar(100) not null,
    primary key(id)
);
