create table "Payments" (
    id bigint,
    purchase_id bigint,
    price int,
    status varchar(20),
    date_created date,
    date_completed date,
    primary key (id),
    foreign key (purchase_id)
        references "Purchases" (id) match simple
        on update no action
        on delete no action
);
