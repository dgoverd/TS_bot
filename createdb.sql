create table if not exists users(
    telegram_id integer primary key
);

create table if not exists categories(
    category_name text primary key
);

create table if not exists user_categories(
    id integer primary key,
    user_id integer,
    category_id text,
    FOREIGN KEY (user_id) references users (telegram_id),
    FOREIGN KEY (category_id) references categories (category_name)
);

create table if not exists timetable(
    id integer primary key,
    start_time datetime,
    end_time datetime,
    user_id integer,
    category_id text
);