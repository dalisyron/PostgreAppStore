create table "Downloads" (
    id bigint,
    package_id bigint,
    user_id bigint,
    date_created date,
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
