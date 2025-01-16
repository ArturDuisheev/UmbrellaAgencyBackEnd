FROM php:8.2-fpm

# Установим необходимые зависимости
RUN apt-get update && apt-get install -y \
    libicu-dev \
    libpq-dev \
    libzip-dev \
    unzip \
    git \
    && docker-php-ext-install intl pdo pdo_pgsql zip

# Установка Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

# Установка рабочей директории
WORKDIR /var/www/html

# Установка прав на директорию проекта
RUN chown -R www-data:www-data /var/www/html

CMD ["php-fpm"]
