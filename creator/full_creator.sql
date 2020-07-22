
create table "Users" (
    id bigint not null, --not necessarily 8 digits
    username varchar(20) not null,
    first_name varchar(20),
    last_name varchar(20),
    email varchar(40) not null,
    phone_number char(10) not null,
    primary key(id)
);
create table "Developers" (
    id bigint not null,
    username varchar(20) not null,
    first_name varchar(20),
    last_name varchar(20),
    email varchar(40) not null,
    birthdate date,
    primary key(id)
);
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
create table "Reviews" (
    id bigint not null,
    date_created date,
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
create table "Genres" (
    id bigint not null,
    name varchar(60),
    primary key(id)
);
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
create table "Categories" (
    id bigint,
    name varchar(60),
    primary key(id)
);
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

create table "Purchases" (
    id bigint,
    package_id bigint,
    user_id bigint,
    type varchar(10),
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
