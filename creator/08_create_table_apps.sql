create table "Apps" (
    id bigint,
    display_name varchar(60),
    category_id bigint,
    package_id bigint,
    primary key(id),
    foreign key(category_id)
        references "Categories" (id) match simple
        on update no action
        on delete no action,
    foreign key(package_id)
        references "Packages" (id) match simple
        on update no action
        on delete no action
);
