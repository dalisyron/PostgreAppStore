create table "Packages" (
    id bigint not null,
    package_name varchar(60) not null,
    dev_id bigint,
    size integer not null,
    file varchar(100) not null,
    primary key(id),
    foreign key (dev_id)
        references "Developers" (id) match simple
        on update no action
        on delete no action
);
