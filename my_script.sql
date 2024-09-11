-- Заполнение таблицы users
INSERT INTO users (id, email, hashed_pass)
SELECT
    gen_random_uuid(),  -- Генерация случайного UUID
    CONCAT('user', i, '@example.com'),  -- Пример email
    'hashed_password'  -- Пример хеша пароля
FROM generate_series(1, 1000) AS s(i);

-- Заполнение таблицы hotels
INSERT INTO hotels (id, name, location, services, rooms_quantity, image_id)
SELECT
    gen_random_uuid(),  -- Генерация случайного UUID
    CONCAT('Hotel ', i),  -- Пример имени отеля
    CONCAT('Location ', i),  -- Пример локации
    '{"wifi": true, "parking": false}',  -- Пример JSON-данных
    FLOOR(RANDOM() * 100) + 1,  -- Пример количества комнат
    gen_random_uuid()  -- Генерация случайного UUID для image_id
FROM generate_series(1, 1000) AS s(i);

-- Заполнение таблицы rooms
INSERT INTO rooms (id, hotel_id, name, description, price, services, quantity, image_id)
SELECT
    gen_random_uuid(),  -- Генерация случайного UUID
    (SELECT id FROM hotels ORDER BY RANDOM() LIMIT 1),  -- Случайный hotel_id
    CONCAT('Room ', i),  -- Пример имени комнаты
    'A nice room with all amenities',  -- Пример описания
    FLOOR(RANDOM() * 200) + 50,  -- Пример цены
    '{"wifi": true, "ac": true}',  -- Пример JSON-данных
    FLOOR(RANDOM() * 5) + 1,  -- Пример количества
    gen_random_uuid()  -- Генерация случайного UUID для image_id
FROM generate_series(1, 1000) AS s(i);

-- Заполнение таблицы bookings
INSERT INTO bookings (id, room_id, user_id, date_from, date_to, price, total_cost, total_day)
SELECT
    gen_random_uuid(),  -- Генерация случайного UUID
    (SELECT id FROM rooms ORDER BY RANDOM() LIMIT 1),  -- Случайный room_id
    (SELECT id FROM users ORDER BY RANDOM() LIMIT 1),  -- Случайный user_id
    NOW() + INTERVAL '1 day',  -- Пример даты начала
    NOW() + INTERVAL '5 days',  -- Пример даты окончания
    FLOOR(RANDOM() * 200) + 50,  -- Пример цены
    FLOOR(RANDOM() * 1000) + 100,  -- Пример общей стоимости
    FLOOR(RANDOM() * 10) + 1  -- Пример общего количества дней
FROM generate_series(1, 1000) AS s(i);
