create table "Games" (
    id bigint not null,
    display_name varchar(60),
    genre_id bigint,
    package_id bigint,
    primary key(id),
    foreign key(id)
        references "Genres" (id) match simple
        on update no action
        on delete no action
)
