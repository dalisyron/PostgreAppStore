create table "Purchases" (
    id bigint,
    package_id bigint,
    user_id bigint,
    type boolean,
    device_id varchar(20),
    token char(20),
    primary key (id),
    foreign key (package_id)
        references "Packages" (id) match simple
        on update no action
        on delete no action,
    foreign key (user_id)
        references "Users" (id) match simple
        on update no action
        on delete no action
);
