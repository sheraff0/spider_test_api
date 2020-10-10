import requests
from django.db.models import Q
from .models import Category, Company, Product

EXTERNAL_API_BASE_URL = 'http://otp.spider.ru/test/companies'


def get_data(url):
    data = requests.get(url)
    return data.json()


def get_companies_list():
    url = EXTERNAL_API_BASE_URL
    return get_data(url)


def get_products_list(company_id):
    url = '{0}/{1}/{2}'.format(
        EXTERNAL_API_BASE_URL, company_id, 'products')
    return get_data(url)


def get_all():
    companies = get_companies_list()
    for company in companies:
        company['products'] = get_products_list(company['id'])
    return companies


def import_products():
    print("Выполняется запрос к внешенему API...")
    try:
        data = get_all()
    except requests.exceptions.ConnectionError as e:
        print("Ошибка соединения!")
        return e
    print("Данные обрабатываются...")
    deleted = 0
    created = 0
    updated = 0
    for company in data:
        company_db, _ = Company.objects.get_or_create(
            external_id=company['id'],
            name=company['name']
        )
        products = company['products'] or []
        product_ids = [p['id'] for p in products]
        deleted += Product.objects.filter(
            ~Q(external_id__in=product_ids),
            company=company_db
        ).delete()[0]
        for product in products:
            if product:
                product_db, _ = Product.objects.get_or_create(
                    external_id=product['id'],
                    company=company_db,
                )
                created += 1 if _ else 0
                updated += 0 if _ else 1
                product_db.title = product['name']
                product_db.description = product['description']
                category = product['category']
                if category:
                    category_db, _ = Category.objects.get_or_create(
                        external_id=category['id'],
                        title=category['name']
                    )
                    product_db.category = category_db
                product_db.save()
    print("""Импорт данных произведен успешно!
Удалено  {1}{4}{0}
Создано  {2}{5}{0}
Изменено {3}{6}{0}""".format(
            "\033[0m", "\033[91m\033[1m", "\033[92m\033[1m", "\033[94m\033[1m",
            deleted, created, updated
        )
    )