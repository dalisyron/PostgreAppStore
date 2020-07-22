create table "Uploads" (
    id bigint,
    package_id bigint,
    developer_id bigint,
    date_created date,
    primary key (id),
    foreign key (package_id)
        references "Packages" (id) match simple
        on update no action
        on delete no action,
    foreign key (developer_id)
        references "Developers" (id) match simple
        on update no action
        on delete no action
);
