create table "Games" (
    id bigint not null,
    display_name varchar(60),
    genre_id bigint,
    package_id bigint,
    primary key(id),
    foreign key(genre_id)
        references "Genres" (id) match simple
        on update no action
        on delete no action,
    foreign key(package_id)
        references "Packages" (id) match simple
        on update no action
        on delete no action
);
