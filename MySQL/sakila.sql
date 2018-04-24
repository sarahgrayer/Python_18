-- All customers inside city_id=312
SELECT customer.first_name, customer.last_name, customer.email, CONCAT_WS(' ', address.address, address.address2, address.postal_code) AS address
FROM customer
JOIN address on customer.address_id=address.address_id
WHERE city_id=312;

-- All comedy films. Return film title, description, release year, rating, special features, genre(category)
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

-- Get all the films joined by actor_id=5. Return actor id, actor name, film title, description, and release year.
SELECT actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name) AS actor_name, film.title, film.description, film.release_year
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.actor_id=5;

-- Get all the customers in store_id =1 and inside cities 1, 42, 312, 459. Return customer first_name, last_name, email, and address.
SELECT customer.first_name, customer.last_name, customer.email, CONCAT_WS(' ', address.address, address.address2, address.postal_code)
From customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE customer.store_id = 1 
AND city.city_id IN (1, 42, 312, 459);

-- Get all the films w/a "rating=G" and "special feature = behind the scenes", joind by actor_id = 15. Return the film title, description, release year, rating, and special feature.
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, actor.actor_id
FROM film 
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.rating = "G"
AND actor.actor_id = 15
AND film.special_features LIKE 'be%';

-- all drama films w/a rental rate of 2.99. Return film title, description, release year, rating, special features, and genre(category).category
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, film.rental_rate
FROM category
JOIN film_category ON category.category_id = film_category.category_id
JOIN film ON film_category.film_id = film.film_id
WHERE rental_rate = 2.99
AND category.name = 'Drama';

-- Get all actors that joined in the film_id = 369. Return film_id, title, actor_id, actor_name
SELECT film.film_id, film.title, actor.actor_id, CONCAT_WS(' ', actor.first_name, actor.last_name)
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE film.film_id = 369;

-- Get all the action films which are joined by Sandra Kilmer. Return film title, description, release year, rating, special features, genre (category), and actor's first/last name.
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, actor.first_name, actor.last_name
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE actor.first_name = 'Sandra'
AND actor.last_name = 'Kilmer'
AND category.name = 'Action';