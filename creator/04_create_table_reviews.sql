create table "Reviews" (
    id bigint not null,
    data_created date,
    text varchar(200),
    rate int not null,
    package_id bigint,
    user_id bigint,
    primary key (id),
	foreign key (package_id)
		references "Packages" (id) match simple
		on update no action
		on delete no action
);
