create table if not exists users(
    codename varchar(255) primary key,
    telegram_id text
);

create table if not exists categories(
    codename varchar(255) primary key,
    name text
);

create table if not exists user_categories(
    user_id varchar(255),
    category_id varchar(255),
    FOREIGN KEY (user_id) references users (codename),
    FOREIGN KEY (category_id) references categories (codename)
);

create table if not exists timetable(
    time datetime,
    user_id varchar(255),
    category_id varchar(255),
    foreign key(user_id) references user_categories(user_id),
    foreign key(category_id) references user_categories(category_id)
);